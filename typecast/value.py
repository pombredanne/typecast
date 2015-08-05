import six
import sys
import decimal
import locale
from datetime import datetime, date

from typecast.converter import Converter, ConverterError


class String(Converter):
    """ String """
    result_type = six.text_type
    allow_empty = True


class Integer(Converter):
    """ Integer """
    result_type = int

    def _cast(self, value, **opts):
        try:
            value = float(value)
        except:
            return locale.atoi(value)

        if value.is_integer():
            return int(value)
        else:
            raise ConverterError('Invalid integer: %r' % value)


class Boolean(Converter):
    """ A boolean field. Matches true/false, yes/no and 0/1 by default,
    but a custom set of values can be optionally provided. """
    result_type = bool
    true_values = ('t', 'yes', 'y', '1', 'true', 'aye')
    false_values = ('f', 'no', 'n', '0', 'false', 'nay')

    def _stringify(self, value, **opts):
        return six.text_type(value).lower()

    def _cast(self, value, true_values=None, false_values=None, **opts):
        if isinstance(value, six.string_types):
            value = value.lower().strip()

            true_values = true_values or self.true_values
            if value in true_values:
                return True

            false_values = false_values or self.false_values
            if value in false_values:
                return False


class Float(Converter):
    """ Floating-point number """
    result_type = float

    def _cast(self, value, **opts):
        return float(value)


class Decimal(Converter):
    """ Decimal number, ``decimal.Decimal`` or float numbers. """
    result_type = decimal.Decimal

    def _stringify(self, value, **opts):
        return '{0:.7f}'.format(value)

    def _cast(self, value, **opts):
        try:
            return decimal.Decimal(value)
        except:
            value = locale.atof(value)
            if sys.version_info < (2, 7):
                value = str(value)
            return decimal.Decimal(value)
