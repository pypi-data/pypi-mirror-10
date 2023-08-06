from __future__ import print_function, absolute_import
__author__ = 'katharine'

from six import with_metaclass, iteritems

from binascii import hexlify
import collections
import logging
import struct

from .types import Field, DEFAULT_ENDIANNESS

__all__ = ["PebblePacket"]

logger = logging.getLogger("libpebble2.protocol")

_PacketRegistry = {}


class PacketType(type):
    def __new__(mcs, name, bases, dct):
        mapping = []
        # If we have a _Meta property, delete it.
        if '_Meta' in dct:
            del dct['_Meta']
        # If we have a Meta property, move it to _Meta. This effectively prevents it being inherited.
        if 'Meta' in dct:
            dct['_Meta'] = dct['Meta'].__dict__
            del dct['Meta']

        # For each Field, add it to our mapping, then set the exposed value to its default value.
        # We go through the classes we inherited from to add anything in there.
        # This means that inheritance works, with inherited classes appending their fields to the end.
        dct['_type_mapping'] = collections.OrderedDict()
        for base in bases:
            if hasattr(base, '_type_mapping'):
                dct['_type_mapping'].update(getattr(base, '_type_mapping'))
        for k, v in iteritems(dct):
            if not isinstance(v, Field):
                continue
            v._name = k
            mapping.append((k, v))
            dct[k] = v._default
        # Put the results into an ordered dict. We sort on field_id to ensure that our dict ends up
        # in the correct order.
        dct['_type_mapping'].update(collections.OrderedDict(sorted(mapping, key=lambda x: x[1].field_id)))
        return super(PacketType, mcs).__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        # At this point we actually have a references to the class, so we can register it
        # in our packet type registry for later decoding.
        if hasattr(cls, '_Meta'):
            if 'endpoint' in cls._Meta and cls._Meta.get('register', True):
                _PacketRegistry[cls._Meta['endpoint']] = cls
        # Fill in all of the fields with a reference to this class.
        # TODO: This isn't used any more; remove it?
        for k, v in iteritems(cls._type_mapping):
            v._parent = cls
        super(PacketType, cls).__init__(name, bases, dct)


class PebblePacket(with_metaclass(PacketType)):
    def __init__(self, **kwargs):
        for k, v in iteritems(kwargs):
            if k.startswith('_'):
                raise AttributeError("You cannot set internal properties during construction.")
            getattr(self, k)  # Throws an exception if the property doesn't exist.
            setattr(self, k, v)

    def serialise(self, default_endianness=None):
        # Figure out an endianness.
        endianness = (default_endianness or DEFAULT_ENDIANNESS)
        if hasattr(self, '_Meta'):
            endianness = self._Meta.get('endianness', endianness)

        # Some fields want to manipulate other fields that appear before them (e.g. Unions)
        for k, v in iteritems(self._type_mapping):
            v.prepare(self, getattr(self, k))

        message = b''
        for k, v in iteritems(self._type_mapping):
            message += v.value_to_bytes(self, getattr(self, k), default_endianness=endianness)
        return message

    def serialise_packet(self):
        if not hasattr(self, '_Meta'):
            raise ReferenceError("Can't serialise a packet that doesn't have an endpoint ID.")
        serialised = self.serialise()
        return struct.pack('!HH', len(serialised), self._Meta['endpoint']) + serialised

    @classmethod
    def parse_message(cls, message):
        length = struct.unpack_from('!H', message, 0)[0] + 4
        command, = struct.unpack_from('!H', message, 2)
        if command in _PacketRegistry:
            return _PacketRegistry[command].parse(message[4:length])[0], length
        else:
            return None, length

    @classmethod
    def parse(cls, message, default_endianness=DEFAULT_ENDIANNESS):
        obj = cls()
        offset = 0
        if hasattr(cls, '_Meta'):
            default_endianness = cls._Meta.get('endianness', default_endianness)
        for k, v in iteritems(cls._type_mapping):
            try:
                value, length = v.buffer_to_value(obj, message, offset, default_endianness=default_endianness)
            except Exception:
                logger.warning("Exception decoding {}.{}".format(cls.__name__, k))
                raise
            offset += length
            setattr(obj, k, value)
        return obj, offset

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__,
                           ', '.join('%s=%s' % (k, self._format_repr(getattr(self, k))) for k in self._type_mapping.keys()))

    def _format_repr(self, value):
        if isinstance(value, bytes):
            if len(value) < 20:
                return hexlify(value).decode()
            else:
                return hexlify(value[:17]).decode() + '...'
        else:
            return value