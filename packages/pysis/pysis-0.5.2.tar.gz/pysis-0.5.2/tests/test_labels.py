# -*- coding: utf-8 -*-
import os
import datetime
import pytz
import six

from pysis import labels
from pysis.labels._collections import (
    Label,
    LabelGroup,
    LabelObject,
    Units,
)


DATA_DIR = os.path.join(os.path.dirname(__file__), 'data/')


def test_assignment():
    label = labels.loads('foo=bar')
    assert isinstance(label, Label)
    assert label['foo'] == 'bar'


def test_spaceing():
    label = labels.loads("""
        foo = bar
        nospace=good
          lots_of_spaceing    =    alsogood
        same = line no = problem; like=aboss
        End
    """)

    assert isinstance(label, Label)
    assert label['foo'] == 'bar'
    assert label['nospace'] == 'good'
    assert label['lots_of_spaceing'] == 'alsogood'
    assert label['same'] == 'line'
    assert label['no'] == 'problem'
    assert label['like'] == 'aboss'


def test_linewrap():
    label = labels.loads("""
        foo = bar-
              baz
        End
    """)

    assert label['foo'] == 'barbaz'


def test_special():
    label = labels.loads("""
        none1 = NULL
        none2 = Null
        true1 = TRUE
        true2 = True
        true3 = true
        false1 = FALSE
        false2 = False
        false3 = false
        End
    """)

    assert label['none1'] is None
    assert label['none2'] is None

    assert label['true1'] is True
    assert label['true2'] is True
    assert label['true3'] is True

    assert label['false1'] is False
    assert label['false2'] is False
    assert label['false3'] is False


def test_integers():
    label = labels.loads("""
        integer = 42
        positive_integer = +123
        negitive_integer = -1
        invalid_integer = 1a2
        End
    """)

    assert isinstance(label['integer'], int)
    assert label['integer'] == 42

    assert isinstance(label['integer'], int)
    assert label['positive_integer'] == 123

    assert isinstance(label['negitive_integer'], int)
    assert label['negitive_integer'] == -1

    assert isinstance(label['invalid_integer'], six.text_type)
    assert label['invalid_integer'] == '1a2'


def test_floats():
    label = labels.loads("""
        float = 1.0
        float_no_decimal = 2.
        float_no_whole = .3
        float_leading_zero = 0.5
        positive_float = +2.0
        negative_float = -1.0
        invalid_float = 1.2.3
        End
    """)
    assert isinstance(label['float'], float)
    assert label['float'] == 1.0

    assert isinstance(label['float_no_decimal'], float)
    assert label['float_no_decimal'] == 2.0

    assert isinstance(label['float_no_whole'], float)
    assert label['float_no_whole'] == 0.3

    assert isinstance(label['float_leading_zero'], float)
    assert label['float_leading_zero'] == 0.5

    assert isinstance(label['positive_float'], float)
    assert label['positive_float'] == 2.0

    assert isinstance(label['negative_float'], float)
    assert label['negative_float'] == -1.0

    assert isinstance(label['invalid_float'], six.text_type)
    assert label['invalid_float'] == '1.2.3'


def test_exponents():
    label = labels.loads("""
        capital = -1.E-3
        lower = -1.e-3
        small = -0.45e6
        int = 31459e1
        invalid = 1e
        End
    """)

    assert isinstance(label['capital'], float)
    assert label['capital'] == -1.0E-3

    assert isinstance(label['lower'], float)
    assert label['lower'] == -1.0E-3

    assert isinstance(label['small'], float)
    assert label['small'] == -0.45E6

    assert isinstance(label['int'], float)
    assert label['int'] == 31459e1

    assert isinstance(label['invalid'], six.text_type)
    assert label['invalid'] == '1e'


def test_objects():
    label = labels.loads("""
        Object = test_object
          foo = bar

          Object = embedded_object
            foo = bar
          End_Object

          Group = embedded_group
            foo = bar
          End_Group
        End_Object
        End
    """)
    test_object = label['test_object']
    assert isinstance(test_object, LabelObject)
    assert test_object['foo'] == 'bar'

    embedded_object = test_object['embedded_object']
    assert isinstance(embedded_object, LabelObject)
    assert embedded_object['foo'] == 'bar'

    embedded_group = test_object['embedded_group']
    assert isinstance(embedded_group, LabelGroup)
    assert embedded_group['foo'] == 'bar'


def test_groups():
    label = labels.loads("""
        Group = test_group
          foo = bar
          Object = embedded_object
            foo = bar
          End_Object

          Group = embedded_group
            foo = bar
          End_Group
        End_Group
        End
    """)
    test_group = label['test_group']
    assert isinstance(test_group, LabelGroup)
    assert test_group['foo'] == 'bar'

    embedded_object = test_group['embedded_object']
    assert isinstance(embedded_object, LabelObject)
    assert embedded_object['foo'] == 'bar'

    embedded_group = test_group['embedded_group']
    assert isinstance(embedded_group, LabelGroup)
    assert embedded_group['foo'] == 'bar'


def test_alt_group_style():
    label = labels.loads("""
        OBJECT               = TEST1
          FOO                = BAR
        END_OBJECT           = TEST1

        GROUP                = TEST2
          FOO                = BAR
        END_GROUP            = TEST2

        END
    """)
    test_group = label['TEST1']
    assert isinstance(test_group, LabelObject)
    assert test_group['FOO'] == 'BAR'

    embedded_object = label['TEST2']
    assert isinstance(embedded_object, LabelGroup)
    assert embedded_object['FOO'] == 'BAR'


def test_binary():
    label = labels.loads("""
        binary_number = 2#0101#
        positive_binary_number = +2#0101#
        negative_binary_number = -2#0101#
        End
    """)

    assert isinstance(label['binary_number'], int)
    assert label['binary_number'] == 5

    assert isinstance(label['positive_binary_number'], int)
    assert label['positive_binary_number'] == 5

    assert isinstance(label['negative_binary_number'], int)
    assert label['negative_binary_number'] == -5


def test_octal():
    label = labels.loads("""
        octal_number = 8#0107#
        positive_octal_number = +8#0107#
        negative_octal_number = -8#0107#
        End
    """)

    assert isinstance(label['octal_number'], int)
    assert label['octal_number'] == 71

    assert isinstance(label['positive_octal_number'], int)
    assert label['positive_octal_number'] == 71

    assert isinstance(label['negative_octal_number'], int)
    assert label['negative_octal_number'] == -71


def test_hex():
    label = labels.loads("""
        hex_number_upper = 16#100A#
        hex_number_lower = 16#100b#
        positive_hex_number = +16#100A#
        negative_hex_number = -16#100A#
        End
    """)

    assert isinstance(label['hex_number_upper'], int)
    assert label['hex_number_upper'] == 4106

    assert isinstance(label['hex_number_lower'], int)
    assert label['hex_number_lower'] == 4107

    assert isinstance(label['positive_hex_number'], int)
    assert label['positive_hex_number'] == 4106

    assert isinstance(label['negative_hex_number'], int)
    assert label['negative_hex_number'] == -4106


def test_quotes():
    label = labels.loads("""
        foo = 'bar'
        empty = ''
        space = '  test  '
        double = "double'quotes"
        single = 'single"quotes'
        number = '123'
        date = '1918-05-11'
        multiline = 'this is a
                     multi-line string'
        continuation = "The planet Jupi-
                        ter is very big"
        formating = "\\n\\t\\f\\v\\\\\\n\\t\\f\\v\\\\"
        End
    """)

    assert isinstance(label['foo'], six.text_type)
    assert label['foo'] == 'bar'

    assert isinstance(label['empty'], six.text_type)
    assert label['empty'] == ''

    assert isinstance(label['space'], six.text_type)
    assert label['space'] == 'test'

    assert isinstance(label['double'], six.text_type)
    assert label['double'] == "double'quotes"

    assert isinstance(label['single'], six.text_type)
    assert label['single'] == 'single"quotes'

    assert isinstance(label['number'], six.text_type)
    assert label['number'] == '123'

    assert isinstance(label['date'], six.text_type)
    assert label['date'] == '1918-05-11'

    assert isinstance(label['multiline'], six.text_type)
    assert label['multiline'] == 'this is a multi-line string'

    assert isinstance(label['continuation'], six.text_type)
    assert label['continuation'] == 'The planet Jupiter is very big'

    assert isinstance(label['formating'], six.text_type)
    assert label['formating'] == '\n\t\f\v\\\n\t\f\v\\'


def test_comments():
    label = labels.loads("""
        /* comment on line */
        # here is a line comment
        /* here is a multi-
        line comment */
        foo = bar /* comment at end of line */
        weird/* in the */=/*middle*/comments
        baz = bang # end line comment
        End
    """)

    assert len(label) == 3

    assert isinstance(label['foo'], six.text_type)
    assert label['foo'] == 'bar'

    assert isinstance(label['foo'], six.text_type)
    assert label['weird'] == 'comments'

    assert isinstance(label['foo'], six.text_type)
    assert label['baz'] == 'bang'


def test_dates():
    label = labels.loads("""
        date1          = 1990-07-04
        date2          = 1990-158
        date3          = 2001-001
        time1          = 12:00
        time_s         = 12:00:45
        time_s_float   = 12:00:45.4571
        time_tz1       = 15:24:12Z
        time_tz2       = 01:12:22+07
        time_tz3       = 01:12:22+7
        time_tz4       = 01:10:39.4575+07
        datetime1      = 1990-07-04T12:00
        datetime2      = 1990-158T15:24:12Z
        datetime3      = 2001-001T01:10:39+7
        datetime4      = 2001-001T01:10:39.457591+7
        End
    """)

    assert isinstance(label['date1'], datetime.date)
    assert label['date1'] == datetime.date(1990, 7, 4)

    assert isinstance(label['date2'], datetime.date)
    assert label['date2'] == datetime.date(1990, 6, 7)

    assert isinstance(label['date3'], datetime.date)
    assert label['date3'] == datetime.date(2001, 1, 1)

    assert isinstance(label['time1'], datetime.time)
    assert label['time1'] == datetime.time(12)

    assert isinstance(label['time_s'], datetime.time)
    assert label['time_s'] == datetime.time(12, 0, 45)

    assert isinstance(label['time_s_float'], datetime.time)
    assert label['time_s_float'] == datetime.time(12, 0, 45, 457100)

    assert isinstance(label['time_tz1'], datetime.time)
    assert label['time_tz1'] == datetime.time(15, 24, 12, tzinfo=pytz.utc)

    assert isinstance(label['time_tz2'], datetime.time)
    assert label['time_tz2'] == datetime.time(1, 12, 22, tzinfo=pytz.FixedOffset(420))  # noqa

    assert isinstance(label['time_tz3'], datetime.time)
    assert label['time_tz3'] == datetime.time(1, 12, 22, tzinfo=pytz.FixedOffset(420))  # noqa

    assert isinstance(label['time_tz4'], datetime.time)
    assert label['time_tz4'] == datetime.time(1, 10, 39, 457500, pytz.FixedOffset(420))  # noqa

    assert isinstance(label['datetime1'], datetime.datetime)
    assert label['datetime1'] == datetime.datetime(1990, 7, 4, 12)

    assert isinstance(label['datetime2'], datetime.datetime)
    assert label['datetime2'] == datetime.datetime(1990, 6, 7, 15, 24, 12, tzinfo=pytz.utc)  # noqa

    assert isinstance(label['datetime3'], datetime.datetime)
    assert label['datetime3'] == datetime.datetime(2001, 1, 1, 1, 10, 39, tzinfo=pytz.FixedOffset(420))  # noqa

    assert isinstance(label['datetime4'], datetime.datetime)
    assert label['datetime4'] == datetime.datetime(2001, 1, 1, 1, 10, 39, 457591, pytz.FixedOffset(420))  # noqa


def test_set():
    label = labels.loads("""
        strings = {a, b, c}
        nospace={a,b,c}
        numbers = {1, 2, 3}
        mixed = {a, 1, 2.5}
        multiline = {a,
                     b,
                     c}
        empty = {}
        End
    """)

    assert isinstance(label['strings'], set)
    assert len(label['strings']) == 3
    assert 'a' in label['strings']
    assert 'b' in label['strings']
    assert 'c' in label['strings']

    assert isinstance(label['nospace'], set)
    assert len(label['nospace']) == 3
    assert 'a' in label['nospace']
    assert 'b' in label['nospace']
    assert 'c' in label['nospace']

    assert isinstance(label['numbers'], set)
    assert len(label['numbers']) == 3
    assert 1 in label['numbers']
    assert 2 in label['numbers']
    assert 3 in label['numbers']

    assert isinstance(label['mixed'], set)
    assert len(label['mixed']) == 3
    assert 'a' in label['mixed']
    assert 1 in label['mixed']
    assert 2.5 in label['mixed']

    assert isinstance(label['multiline'], set)
    assert len(label['multiline']) == 3
    assert 'a' in label['multiline']
    assert 'b' in label['multiline']
    assert 'c' in label['multiline']

    assert isinstance(label['empty'], set)
    assert len(label['empty']) == 0


def test_sequence():
    label = labels.loads("""
        strings = (a, b, c)
        nospace=(a,b,c)
        numbers = (1, 2, 3)
        mixed = (a, 1, 2.5)
        empty = ()
        multiline = (a,
                     b,
                     c)
        End
    """)

    assert isinstance(label['strings'], list)
    assert len(label['strings']) == 3
    assert label['strings'][0] == 'a'
    assert label['strings'][1] == 'b'
    assert label['strings'][2] == 'c'

    assert isinstance(label['nospace'], list)
    assert len(label['nospace']) == 3
    assert label['nospace'][0] == 'a'
    assert label['nospace'][1] == 'b'
    assert label['nospace'][2] == 'c'

    assert isinstance(label['numbers'], list)
    assert len(label['numbers']) == 3
    assert label['numbers'][0] == 1
    assert label['numbers'][1] == 2
    assert label['numbers'][2] == 3

    assert isinstance(label['mixed'], list)
    assert len(label['mixed']) == 3
    assert label['mixed'][0] == 'a'
    assert label['mixed'][1] == 1
    assert label['mixed'][2] == 2.5

    assert isinstance(label['empty'], list)
    assert len(label['empty']) == 0

    assert isinstance(label['multiline'], list)
    assert len(label['multiline']) == 3
    assert label['multiline'][0] == 'a'
    assert label['multiline'][1] == 'b'
    assert label['multiline'][2] == 'c'


def test_units():
    label = labels.loads("""
        foo = 42 <beards>
        g = 9.8 <m/s>
        list = (1, 2, 3) <numbers>
        cool = (1 <number>)
        End
    """)
    assert isinstance(label['foo'], Units)
    assert label['foo'].value == 42
    assert label['foo'].units == 'beards'

    assert isinstance(label['g'], Units)
    assert label['g'].value == 9.8
    assert label['g'].units == 'm/s'

    assert isinstance(label['list'], Units)
    assert isinstance(label['list'].value, list)
    assert label['list'].units == 'numbers'

    assert isinstance(label['cool'], list)
    assert isinstance(label['cool'][0], Units)
    assert label['cool'][0].value == 1
    assert label['cool'][0].units == 'number'


def test_delimiters():
    label = labels.loads("""
        foo = 1;
        Object = embedded_object;
          foo = bar;
        End_Object;
        bar = 2;
        Group = embedded_group;
          foo = bar;
        End_Group;
        End;
    """)

    assert isinstance(label, Label)
    assert label['foo'] == 1
    assert label['bar'] == 2

    assert isinstance(label['embedded_object'], LabelObject)
    assert label['embedded_object']['foo'] == 'bar'

    assert isinstance(label['embedded_group'], LabelGroup)
    assert label['embedded_group']['foo'] == 'bar'


def test_cube_label():
    with open(os.path.join(DATA_DIR, 'pattern.cub'), 'rb') as fp:
        label = labels.load(fp)

    assert isinstance(label['Label'], dict)
    assert label['Label']['Bytes'] == 65536

    assert isinstance(label['IsisCube'], dict)
    assert isinstance(label['IsisCube']['Core'], dict)
    assert label['IsisCube']['Core']['StartByte'] == 65537
    assert label['IsisCube']['Core']['Format'] == 'Tile'
    assert label['IsisCube']['Core']['TileSamples'] == 128
    assert label['IsisCube']['Core']['TileLines'] == 128

    assert isinstance(label['IsisCube']['Core']['Dimensions'], dict)
    assert label['IsisCube']['Core']['Dimensions']['Samples'] == 90
    assert label['IsisCube']['Core']['Dimensions']['Lines'] == 90
    assert label['IsisCube']['Core']['Dimensions']['Bands'] == 1

    assert isinstance(label['IsisCube']['Core']['Pixels'], dict)
    assert label['IsisCube']['Core']['Pixels']['Type'] == 'Real'
    assert label['IsisCube']['Core']['Pixels']['ByteOrder'] == 'Lsb'
    assert label['IsisCube']['Core']['Pixels']['Base'] == 0.0
    assert label['IsisCube']['Core']['Pixels']['Multiplier'] == 1.0
