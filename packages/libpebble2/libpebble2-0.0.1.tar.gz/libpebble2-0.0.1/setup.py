__author__ = 'katharine'

from setuptools import setup, find_packages

setup(name='libpebble2',
      version='0.0.1',
      description='Library for communicating with pebbles over pebble protocol',
      url='https://github.com/pebble/libpebble2',
      author='Pebble Technology Corporation',
      author_email='katharine@pebble.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'enum34>=1.0.4',
        'websocket-client>=0.31.0',
        'six>=1.9.0',
      ],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Embedded Systems',
      ],
      zip_safe=True)
