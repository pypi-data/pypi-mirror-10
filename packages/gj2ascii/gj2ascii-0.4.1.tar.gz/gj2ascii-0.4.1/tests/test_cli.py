"""
Unittests for gj2ascii CLI
"""


from collections import OrderedDict
import os
import tempfile
import unittest

import click
from click.testing import CliRunner
import emoji
import fiona as fio

import gj2ascii
from gj2ascii import cli
from . import compare_ascii
from . import POLY_FILE
from . import LINE_FILE
from . import SINGLE_FEATURE_WV_FILE
from . import EXPECTED_TWO_PROPERTIES_OUTPUT
from . import EXPECTED_ALL_PROPERTIES_OUTPUT
from . import EXPECTED_POLYGON_40_WIDE
from . import EXPECTED_LINE_40_WIDE
from . import MULTILAYER_FILE
from . import EXPECTED_STACKED
from . import EXPECTED_STACK_PERCENT_ALL
from . import SMALL_AOI_POLY_LINE_FILE
from . import EXPECTED_BBOX_POLY


class TestCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_simple(self):
        result = self.runner.invoke(cli.main, [
            POLY_FILE,
            '--width', '40',
            '--char', '+',
            '--fill', '.',
        ])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(compare_ascii(result.output.strip(), EXPECTED_POLYGON_40_WIDE.strip()))

    def test_complex(self):
        result = self.runner.invoke(cli.main, [
            LINE_FILE,
            '--width', '40',
            '--char', '+',
            '--fill', '.',
            '--no-prompt',
            '--all-touched',
            '--iterate',
            '--crs', 'EPSG:26918'
        ])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(compare_ascii(result.output.strip(), EXPECTED_LINE_40_WIDE.strip()))

    def test_bad_fill_value(self):
        result = self.runner.invoke(cli.main, ['-c toolong', POLY_FILE])
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(
            result.output.startswith('Usage:') and 'Error:' in result.output and
            'must be a single character' in result.output)

    def test_bad_rasterize_value(self):
        result = self.runner.invoke(cli.main, ['-f toolong', POLY_FILE])
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(
            result.output.startswith('Usage:') and 'Error:' in result.output and
            'must be a single character' in result.output)

    def test_different_width(self):
        fill = '+'
        value = '.'
        width = 62
        result = self.runner.invoke(cli.main, [
            '--width', width,
            POLY_FILE,
            '--fill', fill,
            '--char', value,
            '--no-prompt'
        ])
        self.assertEqual(result.exit_code, 0)
        for line in result.output.rstrip(os.linesep).splitlines():
            if line.startswith((fill, value)):
                self.assertEqual(len(line.rstrip(os.linesep).split()), width / 2)

    def test_paginate_with_all_properties(self):
        result = self.runner.invoke(cli.main, [
            SINGLE_FEATURE_WV_FILE,
            '--width', '20',
            '--properties', '%all',
            '--iterate', '--no-prompt'
        ])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(
            compare_ascii(result.output.strip(), EXPECTED_ALL_PROPERTIES_OUTPUT.strip()))

    def test_paginate_with_two_properties(self):
        result = self.runner.invoke(cli.main, [
            SINGLE_FEATURE_WV_FILE,
            '--width', '20',
            '--fill', '*',
            '--properties', 'NAME,ALAND',
            '--iterate', '--no-prompt'
        ])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(compare_ascii(
            result.output.strip(), EXPECTED_TWO_PROPERTIES_OUTPUT.strip()))

    def test_iterate_wrong_arg_count(self):
        result = self.runner.invoke(cli.main, [
            POLY_FILE,
            '--iterate',
            '--char', '1',
            '--char', '2'
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(result.output.startswith('Error:') and 'arg' in result.output and
                        'layer' in result.output)

    def test_iterate_bad_property(self):
        result = self.runner.invoke(cli.main, [
            SINGLE_FEATURE_WV_FILE,
            '--iterate',
            '--properties', 'bad-prop'
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(isinstance(result.exception, KeyError))

    def test_write_to_file(self):
        with tempfile.NamedTemporaryFile('r+') as f:
            result = self.runner.invoke(cli.main, [
                SINGLE_FEATURE_WV_FILE,
                '--width', '20',
                '--properties', 'NAME,ALAND',
                '--iterate',
                '--fill', '*',
                '--outfile', f.name
                # --no-prompt should automatically happen in this case
            ])
            f.seek(0)
            self.assertEqual(result.exit_code, 0)
            self.assertEqual(result.output, '')
            self.assertTrue(
                compare_ascii(f.read().strip(), EXPECTED_TWO_PROPERTIES_OUTPUT.strip()))

    def test_styled_write_to_file(self):
        with fio.open(SINGLE_FEATURE_WV_FILE) as src:
            expected = gj2ascii.render(src, width=20, char='1', fill='0')
        with tempfile.NamedTemporaryFile('r+') as f:
            result = self.runner.invoke(cli.main, [
                SINGLE_FEATURE_WV_FILE,
                '--width', '20',
                '--properties', 'NAME,ALAND',
                '--char', '1=red',
                '--fill', '0=blue',
                '--outfile', f.name
            ])
            f.seek(0)
            self.assertEqual(result.exit_code, 0)
            self.assertEqual(result.output, '')
            self.assertTrue(compare_ascii(f.read().strip(), expected.strip()))

    def test_stack_layers(self):
        result = self.runner.invoke(cli.main, [
            MULTILAYER_FILE + ',polygons,lines',
            '--char', '+',
            '--char', '8',
            '--fill', '.',
            '--width', '40'
        ])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(compare_ascii(result.output.strip(), EXPECTED_STACKED.strip()))

    def test_stack_too_many_args(self):
        result = self.runner.invoke(cli.main, [
            MULTILAYER_FILE + ',polygons,lines',
            '--char', '+',
            '--char', '8',
            '--char', '0'  # 2 layers but 3 values
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(
            result.output.startswith('Error:') and '--char' in result.output and 'number' in
            result.output and 'equal' in result.output)

    def test_render_one_layer_too_many_args(self):
        result = self.runner.invoke(cli.main, [
            POLY_FILE,
            '--char', '-',
            '--char', '8'
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(result.output.startswith('Error:') and 'number' in result.output and
                        '--char' in result.output)

    def test_bbox(self):
        with fio.open(SMALL_AOI_POLY_LINE_FILE) as src:
            cmd = [
                POLY_FILE,
                '--width', '40',
                '--char', '+',
                '--bbox',
            ] + list(map(str, src.bounds))
            result = self.runner.invoke(cli.main, cmd)
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(compare_ascii(
            result.output.strip(), EXPECTED_BBOX_POLY.strip()))

    def test_iterate_too_many_layers(self):
        result = self.runner.invoke(cli.main, [
            MULTILAYER_FILE,
            '--iterate', '--no-prompt'
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(result.output.startswith('Error:') and 'single layer' in result.output)

    def test_multilayer_compute_colormap(self):
        coords = []
        for layer in ('polygons', 'lines'):
            with fio.open(MULTILAYER_FILE, layer=layer) as src:
                coords += list(src.bounds)
        bbox = min(coords[0::4]), min(coords[1::4]), max(coords[2::4]), max(coords[3::4])

        rendered_layers = []
        for layer, char in zip(('polygons', 'lines'), ('0', '1')):
            with fio.open(MULTILAYER_FILE, layer=layer) as src:
                rendered_layers.append(
                    gj2ascii.render(src, width=20, fill=' ', char=char, bbox=bbox))
        expected = gj2ascii.stack(rendered_layers)

        # Explicitly define since layers are not consistently listed in order
        result = self.runner.invoke(cli.main, [
            MULTILAYER_FILE + ',polygons,lines',
            '--width', '20'
        ])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(compare_ascii(expected.strip(), result.output.strip()))

    def test_exceed_auto_generate_colormap_limit(self):
        infiles = [POLY_FILE for i in range(len(gj2ascii.ANSI_COLORMAP.keys()) + 2)]
        result = self.runner.invoke(cli.main, infiles)
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(result.output.startswith('Error:') and 'auto' in result.output and
                        'generate' in result.output and '--char' in result.output)

    def test_default_char_map(self):
        with fio.open(POLY_FILE) as src:
            expected = gj2ascii.render(src)
        result = self.runner.invoke(cli.main, [
            POLY_FILE
        ])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(compare_ascii(result.output.strip(), expected.strip()))

    def test_same_char_twice(self):
        width = 40
        fill = '.'
        char = '+'
        with fio.open(POLY_FILE) as poly, fio.open(LINE_FILE) as line:
            coords = list(poly.bounds) + list(line.bounds)
            bbox = (min(coords[0::4]), min(coords[1::4]), max(coords[2::4]), max(coords[3::4]))
            expected = gj2ascii.render_multiple(
                [(poly, char), (line, char)], width=width, fill=fill, bbox=bbox)
            result = self.runner.invoke(cli.main, [
                POLY_FILE, LINE_FILE,
                '--width', width,
                '--char', char,
                '--char', char,
                '--fill', fill
            ])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(compare_ascii(expected, result.output))


class TestCallbacks(unittest.TestCase):

    def test_cb_char_and_fill(self):
        testvals = {
            'a': [('a', None)],
            ('a', 'b'): [('a', None), ('b', None)],
            'black': [(gj2ascii.DEFAULT_COLOR_CHAR['black'], 'black')],
            ('black', 'blue'): [
                (gj2ascii.DEFAULT_COLOR_CHAR['black'], 'black'),
                (gj2ascii.DEFAULT_COLOR_CHAR['blue'], 'blue')
            ],
            ('+=red', '==yellow'): [('+', 'red'), ('=', 'yellow')],
            None: []
        }

        # The callback can return a list of tuples or a list of lists.  Force test to compare
        # list to list.
        for inval, expected in testvals.items():
            expected = [list(i) for i in expected]
            actual = [list(i) for i in cli._cb_char_and_fill(None, None, inval)]
            self.assertEqual(expected, actual)
        with self.assertRaises(click.BadParameter):
            cli._cb_char_and_fill(None, None, 'bad-color')
        with self.assertRaises(click.BadParameter):
            cli._cb_char_and_fill(None, None, ('bad-color'))

    def test_cb_properties(self):

        for v in ('%all', None):
            self.assertEqual(v, cli._cb_properties(None, None, v))

        props = 'PROP1,PROP2,PROP3'
        self.assertEqual(props.split(','), cli._cb_properties(None, None, props))

    def test_cb_multiple_default(self):

        values = ('1', '2')
        self.assertEqual(values, cli._cb_multiple_default(None, None, values))
        values = '1'
        self.assertEqual((values), cli._cb_multiple_default(None, None, values))

    def test_cb_bbox(self):

        bbox_file = 'sample-data/polygons.geojson'

        with fio.open(bbox_file) as src:

            self.assertEqual(None, cli._cb_bbox(None, None, None))
            self.assertEqual(src.bounds, cli._cb_bbox(None, None, src.bounds))

        # Bbox with invalid X values
        with self.assertRaises(click.BadParameter):
            cli._cb_bbox(None, None, (2, 0, 1, 0,))

        # Bbox with invalid Y values
        with self.assertRaises(click.BadParameter):
            cli._cb_bbox(None, None, (0, 2, 0, 1))

        # Bbox with invalid X and Y values
        with self.assertRaises(click.BadParameter):
            cli._cb_bbox(None, None, (2, 2, 1, 1,))


def test_with_emoji():
    result = CliRunner().invoke(cli.main, [
        POLY_FILE,
        LINE_FILE,
        '-c', ':water_wave:',
        '-c', ':+1:'
    ])
    assert result.exit_code is 0
    for c in (':water_wave:', ':+1:'):
        ucode = emoji.unicode_codes.EMOJI_ALIAS_UNICODE[c]
        assert ucode in result.output


def test_no_style():
    result = CliRunner().invoke(cli.main, [
        POLY_FILE,
        '-c', '+',
        '--no-style',
        '-w', '40',
        '-f', '.'
    ])
    assert result.exit_code is 0
    assert compare_ascii(result.output.strip(), EXPECTED_POLYGON_40_WIDE.strip())


def test_print_colors():
    result = CliRunner().invoke(cli.main, [
        '--colors'
    ])
    assert result.exit_code is 0
    for color in gj2ascii.DEFAULT_COLOR_CHAR.keys():
        assert color in result.output
