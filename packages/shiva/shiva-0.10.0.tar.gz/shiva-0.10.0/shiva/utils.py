# -*- coding: utf-8 -*-
from contextlib import contextmanager
import datetime
import logging
import logging.config
import os
import random
import re
import string
import traceback

from flask.ext.restful.utils import unpack as _unpack
import dateutil.parser
import mutagen

import shiva
from shiva.exceptions import MetadataManagerReadError


def parse_bool(value):
    """
    This utility takes a string or a boolean, and return a boolean value. The
    possible False strings are 'false', '0' and '', any other string will
    evaluate to True. Raises ValueError if the value is not either boolean nor
    string.

    """

    if value is None:
        return False

    if isinstance(value, bool):
        return value

    if not isinstance(value, basestring):
        raise ValueError

    false_values = ('false', '0', '')

    return value.lower() not in false_values


def get_shiva_path():
    return os.path.dirname(os.path.abspath(shiva.__file__))


def get_logger():
    logging_conf = os.path.join(get_shiva_path(), 'logging.conf')
    logging.config.fileConfig(logging_conf)

    return logging.getLogger('shiva')


def randstr(length=32):
    """
    Generates a random string of the given length. Defaults to 32 characters.

    """

    if not isinstance(length, int):
        raise ValueError

    if length < 1:
        return ''

    invalid_chars_re = re.compile(r'[\'"\\]*')

    chars = string.digits + string.letters + string.punctuation
    chars = ''.join(invalid_chars_re.split(chars))

    return ''.join(random.choice(chars) for _ in range(length))


def _import(class_path):
    """ Imports a module or class from a string in dot notation. """

    bits = class_path.split('.')
    mod_name = '.'.join(bits[:-1])
    cls_name = bits[-1]

    mod = __import__(mod_name, None, None, cls_name)

    return getattr(mod, cls_name)


@contextmanager
def ignored(*exceptions, **kwargs):
    """Context manager that ignores all of the specified exceptions. This will
    be in the standard library starting with Python 3.4."""

    log = get_logger()
    try:
        yield
    except exceptions:
        if kwargs.get('print_traceback'):
            log.debug(traceback.format_exc())


class MetadataManager(object):
    """A format-agnostic metadata wrapper around Mutagen.

    This makes reading/writing audio metadata easy across all possible audio
    formats by using properties for the different keys.

    In order to persist changes to the metadata, the ``save()`` method needs to
    be called.

    """

    def __init__(self, filepath):
        self._original_path = filepath
        try:
            self.reader = mutagen.File(filepath, easy=True)
        except Exception, e:
            raise MetadataManagerReadError(e.message)

    @property
    def title(self):
        return self._getter('title')

    @property
    def artist(self):
        """The artist name."""
        return self._getter('artist')

    @artist.setter
    def artist(self, value):
        self.reader['artist'] = value

    @property
    def album(self):
        """The album name."""
        return self._getter('album')

    @album.setter
    def album(self, value):
        self.reader['album'] = value

    @property
    def release_year(self):
        """The album release year."""
        default_date = datetime.datetime(datetime.MINYEAR, 1, 1)
        default_date = default_date.replace(tzinfo=None)
        date = self._getter('date', '')
        try:
            parsed_date = dateutil.parser.parse(date, default=default_date)
        except ValueError:
            return None

        parsed_date = parsed_date.replace(tzinfo=None)
        if parsed_date != default_date:
            return parsed_date.year

        return None

    @release_year.setter
    def release_year(self, value):
        self.reader['year'] = value

    @property
    def track_number(self):
        """The track number."""

        try:
            _number = int(self._getter('tracknumber'))
        except (TypeError, ValueError):
            _number = None

        return _number

    @track_number.setter
    def track_number(self, value):
        self.reader['tracknumber'] = value

    @property
    def genre(self):
        """The music genre."""
        return self._getter('genre')

    @genre.setter
    def genre(self, value):
        self.genre = value

    @property
    def length(self):
        """The length of the song in seconds."""
        return int(round(self.reader.info.length))

    @property
    def bitrate(self):
        """The audio bitrate."""
        if hasattr(self.reader.info, 'bitrate'):
            return self.reader.info.bitrate / 1000

    @property
    def sample_rate(self):
        """The audio sample rate."""
        return self.reader.info.sample_rate

    @property
    def filename(self):
        """The file name of this audio file."""
        return os.path.basename(self.reader.filename)

    @property
    def filepath(self):
        """The absolute path to this audio file."""
        return os.path.abspath(self.reader.filename)

    @property
    def origpath(self):
        """The original path with which this class was instantiated. This
        function avoids a call to ``os.path``.  Usually you'll want to use
        either :meth:`.filename` or :meth:`.filepath` instead."""
        return self._original_path

    @property
    def filesize(self):
        """The size of this audio file in the filesystem."""
        return os.stat(self.reader.filename).st_size

    # Helper functions

    def _getter(self, attr, fallback=None):
        """Return the first list item of the specified attribute or fall back
        to a default value if attribute is not available."""
        return self.reader[attr][0] if attr in self.reader else fallback

    def save(self):
        """Save changes to file metadata."""
        self.reader.save()


def unpack(value):
    """Return a three tuple of data, code, and headers"""
    if isinstance(value, tuple):
        if len(value) == 0:
            return '', 200, {}

    data, code, headers = _unpack(value[0])

    if isinstance(data, tuple):
        return data[0], code, headers

    return data, code, headers


def get_list(model, id_list):
    for _id in id_list:
        artist = model.query.get(_id)

        if not artist:
            raise ValueError

        yield artist


def get_by_name(model, name):
    instance = model.query.filter_by(name=name).first()

    if not instance:
        instance = model(name=name)

    return instance
