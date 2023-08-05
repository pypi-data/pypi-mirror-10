# -*- coding: utf-8 -*-
import unittest

from skoolkittest import SkoolKitTestCase
from skoolkit.ctlparser import CtlParser

CTL = """; Test control file for parse_ctl

; @start:30000
b $7530 Data at 30000
T 30002,10 Message in the data block
M 30012,15 This comment covers the following two sub-blocks
W 30012-30019
C 30020,7
  30050,5,3:T2 Complex DEFB with a blank directive
# This is a control file comment
c 30100 Routine at 30100
D 30100 Description of routine at 30100
R 30100 A Some value
R 30100 BC Some other value
; @label:$7595=LOOP
E 30100 First paragraph of the end comment for the routine at 30100
E 30100 Second paragraph of the end comment for the routine at 30100
% This is another control file comment
g 30200 Game status buffer entry at 30200
  30200,10,1 Blank directive in a 'g' block
i 30300 Ignored block at 30300
t 30400 Message at 30400
  30450,7,4:B3 Complex DEFM with a blank directive
u 30500 Unused block at 30500
  30500,2 Blank directive in a 'u' block
B 30502,3
B 30510,12,3
B 30530-30549,2*7,1*3,3
B 30560,21,6,5,4,3,2,1
; This is yet another control file comment
w 30600 Words at 30600
S 30620,7
s 30700 Zeroes at 30700
B 30720,10,1,T3:2,1:T1*2
T 30730-30744,10:B5"""

class CtlParserTest(SkoolKitTestCase):
    def _get_ctl_parser(self, ctl):
        ctl_parser = CtlParser()
        ctlfile = self.write_text_file(ctl)
        ctl_parser.parse_ctl(ctlfile)
        return ctl_parser

    def test_parse_ctl(self):
        ctl_parser = self._get_ctl_parser(CTL)

        exp_ctls = {
            30000: 'b',
            30100: 'c',
            30200: 'g',
            30300: 'i',
            30400: 't',
            30500: 'u',
            30600: 'w',
            30700: 's'
        }
        self.assertEqual(exp_ctls, ctl_parser.ctls)

        exp_subctls = {
            30002: 't',
            30012: 'w',
            30020: 'c',
            30027: None,
            30050: 'b',
            30055: None,
            30100: None,
            30200: 'b',
            30210: None,
            30450: 't',
            30457: None,
            30500: 'b',
            30502: 'b',
            30505: None,
            30510: 'b',
            30522: None,
            30530: 'b',
            30532: 'b',
            30534: 'b',
            30536: 'b',
            30538: 'b',
            30540: 'b',
            30542: 'b',
            30544: 'b',
            30545: 'b',
            30546: 'b',
            30547: 'b',
            30550: None,
            30560: 'b',
            30566: 'b',
            30571: 'b',
            30575: 'b',
            30578: 'b',
            30580: 'b',
            30581: None,
            30620: 's',
            30627: None,
            30720: 'b',
            30721: 'b',
            30726: 'b',
            30728: 'b',
            30730: 't',
            30745: None
        }
        self.assertEqual(exp_subctls, ctl_parser.subctls)

        exp_titles = {
            30000: 'Data at 30000',
            30100: 'Routine at 30100',
            30200: 'Game status buffer entry at 30200',
            30300: 'Ignored block at 30300',
            30400: 'Message at 30400',
            30500: 'Unused block at 30500',
            30600: 'Words at 30600',
            30700: 'Zeroes at 30700'
        }
        self.assertEqual(exp_titles, ctl_parser.titles)

        exp_instruction_comments = {
            30002: 'Message in the data block',
            30012: None,
            30020: None,
            30050: 'Complex DEFB with a blank directive',
            30200: "Blank directive in a 'g' block",
            30450: 'Complex DEFM with a blank directive',
            30500: "Blank directive in a 'u' block",
            30502: None,
            30510: None,
            30530: None,
            30560: None,
            30620: None,
            30720: None,
            30730: None
        }
        self.assertEqual(exp_instruction_comments, ctl_parser.instruction_comments)

        exp_descriptions = {
            30100: ['Description of routine at 30100']
        }
        self.assertEqual(exp_descriptions, ctl_parser.descriptions)

        exp_registers = {
            30100: [['A', 'Some value'], ['BC', 'Some other value']]
        }
        self.assertEqual(exp_registers, ctl_parser.registers)

        exp_end_comments = {
            30100: ['First paragraph of the end comment for the routine at 30100',
                    'Second paragraph of the end comment for the routine at 30100']
        }
        self.assertEqual(exp_end_comments, ctl_parser.end_comments)

        exp_lengths = {
            30050: ((3, None), (2, 'T')),
            30200: ((1, None),),
            30450: ((4, None), (3, 'B')),
            30510: ((3, None),),
            30530: ((2, None),),
            30532: ((2, None),),
            30534: ((2, None),),
            30536: ((2, None),),
            30538: ((2, None),),
            30540: ((2, None),),
            30542: ((2, None),),
            30544: ((1, None),),
            30545: ((1, None),),
            30546: ((1, None),),
            30547: ((3, None),),
            30560: ((6, None),),
            30566: ((5, None),),
            30571: ((4, None),),
            30575: ((3, None),),
            30578: ((2, None),),
            30580: ((1, None),),
            30720: ((1, None),),
            30721: ((3, 'T'), (2, None)),
            30726: ((1, None), (1, 'T')),
            30728: ((1, None), (1, 'T')),
            30730: ((10, None), (5, 'B'))
        }
        self.assertEqual(exp_lengths, ctl_parser.lengths)

        exp_multiline_comments = {
            30012: (30026, 'This comment covers the following two sub-blocks')
        }
        self.assertEqual(exp_multiline_comments, ctl_parser.multiline_comments)

        exp_entry_asm_directives = {
            30000: [('start', None)]
        }
        self.assertEqual(exp_entry_asm_directives, ctl_parser.entry_asm_directives)

        exp_instruction_asm_directives = {
            30101: [('label', 'LOOP')]
        }
        self.assertEqual(exp_instruction_asm_directives, ctl_parser.instruction_asm_directives)

    def test_invalid_lines(self):
        ctl_specs = [
            ('  30000,1',           'blank directive with no containing block'),
            ('B 30745,15,5:X10',    'invalid integer'),
            ('T 30760,5,2:Y3',      'invalid integer'),
            ('W 30765,5,1:B4',      'invalid integer'),
            ('S 30770,10,T8:2',     'invalid integer'),
            ('B 30780,10,h,5',      'invalid integer'),
            ('C 40000,Q',           'invalid integer'),
            ('; @label:EDCBA=Z',    'invalid ASM directive address'),
            ('@ FEDCB label=Z',     'invalid ASM directive address'),
            ('; @label=Z',          'invalid ASM directive declaration'),
            ('@ 49152',             'invalid ASM directive declaration'),
            ('b 50000,20',          'extra parameters after address'),
            ('b b50010',            'invalid address'),
            ('d 50020',             'invalid directive'),
            ('! 50030',             'invalid directive'),
            ('; @ignoreua:50000:f', "invalid @ignoreua directive address suffix: '50000:f'"),
            ('@ 50000 ignoreua:g',  "invalid @ignoreua directive suffix: 'g'"),
            ('L 51000',             'loop length not specified'),
            ('L 51000,10',          'loop count not specified')
        ]
        ctls = [spec[0] for spec in ctl_specs]
        ctl_parser = CtlParser()
        ctlfile = self.write_text_file('\n'.join(ctls))
        ctl_parser.parse_ctl(ctlfile)
        exp_warnings = []
        for line_no, (ctl, error_msg) in enumerate(ctl_specs, 1):
            if error_msg:
                exp_warnings.append('WARNING: Ignoring line {} in {} ({}):'.format(line_no, ctlfile, error_msg))
        warnings = self.err.getvalue().split('\n')[:-1]
        self.assertEqual(exp_warnings, warnings[0::2])
        invalid_ctls = [spec[0] for spec in ctl_specs if spec[1]]
        self.assertEqual(invalid_ctls, warnings[1::2])

    def test_comments(self):
        ctl = '\n'.join((
            '# This is a comment',
            'b 32768',
            '% This is also a comment',
            'w 32769',
            '; This is a comment too'
        ))
        ctl_parser = self._get_ctl_parser(ctl)

        self.assertEqual(self.err.getvalue(), '')
        self.assertEqual({32768: 'b', 32769: 'w'}, ctl_parser.ctls)

    def test_bases(self):
        ctl = '\n'.join((
            'c 50000 Test numeric instruction operand bases',
            '  50000,b',
            '  50002,h2',
            '  50006,hb',
            '  50010,d',
            '  50012,nb4',
            '  50016,c',
            '  50018,dc4'
        ))
        ctl_parser = self._get_ctl_parser(ctl)

        exp_lengths = {
            50000: ((None, 'b'),),
            50002: ((None, 'h'),),
            50006: ((None, 'hb'),),
            50010: ((None, 'd'),),
            50012: ((None, 'nb'),),
            50016: ((None, 'c'),),
            50018: ((None, 'dc'),)
        }
        self.assertEqual(exp_lengths, ctl_parser.lengths)

    def test_byte_formats(self):
        ctl = '\n'.join((
            'b 40000 Test byte formats',
            '  40000,b 5 bytes in binary format',
            '  40005,b5 5 more bytes in binary format',
            'B 40010,b10,5,d3,h2 5 binary, 3 decimal, 2 hex',
            'B 40020,b,2:d3:h5 2 binary, 3 decimal, 5 hex, one line',
            '  40030,,b6,3,h1 6 binary, 3 default, 1 hex',
            '  40040,10,b5:2:h3 5 binary, 2 default, 3 hex, one line',
            '  40050,10,1,T9 1 default, 9 text',
            '  40060,10,h4:T6 4 hex, 6 text, one line',
            'T 40070,10,3,b7 3 text, 7 binary',
            'T 40080,10,2:h8 2 text, 8 hex, one line',
            'T 40090,10,5,B5 5 text, 5 default'
        ))
        ctl_parser = self._get_ctl_parser(ctl)

        exp_lengths = {
            40000: ((None, 'b'),),
            40005: ((None, 'b'),),
            40010: ((5, 'b'),),
            40015: ((3, 'd'),),
            40018: ((2, 'h'),),
            40020: ((2, 'b'), (3, 'd'), (5, 'h')),
            40030: ((6, 'b'),),
            40036: ((3, None),),
            40039: ((1, 'h'),),
            40040: ((5, 'b'), (2, None), (3, 'h')),
            40050: ((1, None),),
            40051: ((9, 'T'),),
            40060: ((4, 'h'), (6, 'T')),
            40070: ((3, None),),
            40073: ((7, 'b'),),
            40080: ((2, None), (8, 'h')),
            40090: ((5, None),),
            40095: ((5, 'B'),)
        }
        self.assertEqual(exp_lengths, ctl_parser.lengths)

    def test_word_formats(self):
        ctl = '\n'.join((
            'w 40000 Test word formats',
            '  40000,10 5 default',
            '  40010,b10 5 words in binary format',
            'W 40020,b10,6,d2,h2 3 binary, 1 decimal, 1 hex',
            'W 40030,b10,4:d4:h2 2 binary, 2 decimal, 1 hex, one line',
            '  40040,10,b2,4,h4 1 binary, 2 default, 2 hex',
            '  40050,10,b2:6:h2 1 binary, 3 default, 1 hex, one line',
        ))
        ctl_parser = self._get_ctl_parser(ctl)

        exp_lengths = {
            40010: ((None, 'b'),),
            40020: ((6, 'b'),),
            40026: ((2, 'd'),),
            40028: ((2, 'h'),),
            40030: ((4, 'b'), (4, 'd'), (2, 'h')),
            40040: ((2, 'b'),),
            40042: ((4, None),),
            40046: ((4, 'h'),),
            40050: ((2, 'b'), (6, None), (2, 'h'))
        }
        self.assertEqual(exp_lengths, ctl_parser.lengths)

    def test_s_directives(self):
        ctl = '\n'.join((
            's 50000 Test s/S directives',
            '  50000,10',
            '  50010,b10',
            '  50020,d10',
            '  50030,h10',
            'S 50040,b20,5,d5,h5',
            'S 50060,d20,b5,5,h5',
            'S 50080,h20,b5,d5,5',
            '  50100,20,b5,d5,5',
            '  50120,20,d20:b%10001000',
            '  50140,20,20:h$44',
            '  50160,12,10:h10,h2:2'
        ))
        ctl_parser = self._get_ctl_parser(ctl)

        exp_lengths = {
            50010: ((None, 'b'),),
            50020: ((None, 'd'),),
            50030: ((None, 'h'),),
            50040: ((5, 'b'),),
            50045: ((5, 'd'),),
            50050: ((5, 'h'),),
            50060: ((5, 'b'),),
            50065: ((5, 'd'),),
            50070: ((5, 'h'),),
            50080: ((5, 'b'),),
            50085: ((5, 'd'),),
            50090: ((5, 'h'),),
            50100: ((5, 'b'),),
            50105: ((5, 'd'),),
            50110: ((5, None),),
            50120: ((20, 'd'), (136, 'b')),
            50140: ((20, None), (68, 'h')),
            50160: ((10, None), (10, 'h')),
            50170: ((2, 'h'), (2, None))
        }
        self.assertEqual(exp_lengths, ctl_parser.lengths)

    def test_ignoreua_directives(self):
        ctl = '\n'.join((
            '; @ignoreua:30000:t',
            'c 30000 Routine at 30000',
            'c 30001 Routine',
            '@ 30001 ignoreua:d',
            'D 30001 Description of the routine at 30001',
            '; @ignoreua:30001:r',
            'R 30001 HL 30001',
            '@ 30001 ignoreua',
            '  30001 Instruction-level comment at 30001',
            'c 30002 Routine',
            '; @ignoreua:30003:m',
            'D 30003 Mid-block comment above 30003.',
            '@ 30003 ignoreua:i',
            '  30003 Instruction-level comment at 30003',
            'c 30004 Routine',
            '; @ignoreua:30004:i',
            '  30004,1 Instruction-level comment at 30004',
            '@ 30005 ignoreua:m',
            'D 30005 Mid-block comment above 30005.',
            '; @ignoreua:30004:e',
            'E 30004 End comment for the routine at 30004.'
        ))
        ctl_parser = self._get_ctl_parser(ctl)

        exp_ignoreua_directives = {
            30000: set(['t']),
            30001: set(['d', 'i', 'r']),
            30003: set(['m', 'i']),
            30004: set(['e', 'i']),
            30005: set(['m']),
        }
        self.assertEqual(exp_ignoreua_directives, ctl_parser.ignoreua_directives)

    def test_registers(self):
        ctl = '\n'.join((
            'c 40000 Routine',
            'R 40000 BC Important value',
            'R 40000 DE',
            'R 40000',
            'R 40000 HL Another important value'
        ))
        ctl_parser = self._get_ctl_parser(ctl)
        blocks = ctl_parser.get_blocks()
        self.assertEqual(len(blocks), 1)

        exp_registers = [
            ['BC', 'Important value'],
            ['DE', ''],
            ['HL', 'Another important value']
        ]
        self.assertEqual(exp_registers, blocks[0].registers)

    def test_N_directive(self):
        ctl = '\n'.join((
            'c 40000 Routine',
            'D 40000 Description.',
            'N 40000 Paragraph 1.',
            'N 40000 Paragraph 2.',
            'N 40001 Mid-routine comment.'
        ))
        ctl_parser = self._get_ctl_parser(ctl)
        blocks = ctl_parser.get_blocks()
        self.assertEqual(len(blocks), 1)

        self.assertEqual(['Description.'], blocks[0].description)
        sub_blocks = blocks[0].blocks
        self.assertEqual(len(sub_blocks), 2)
        self.assertEqual(['Paragraph 1.', 'Paragraph 2.'], sub_blocks[0].header)
        self.assertEqual(['Mid-routine comment.'], sub_blocks[1].header)

    def test_loop(self):
        start = 30000
        length = 25
        count = 2
        end = start + length * count
        ctl = '\n'.join((
            '@ 30000 start',
            '; @org:30000=30000',
            'c 30000 This entry should not be repeated',
            'D 30000 This entry description should not be repeated',
            'R 30000 HL This register should not be repeated',
            '  30000,5 Begin',
            'B 30005,5,1,2',
            'D 30010 A mid-block comment',
            'M 30010,10 A multi-line comment',
            'S 30010,6',
            'W 30016,4,4',
            '@ 30020 label=END',
            'T 30020,5,4:B1 End',
            'E 30000 This end comment should not be repeated',
            'L {},{},{}'.format(start, length, count)
        ))
        ctl_parser = self._get_ctl_parser(ctl)
        blocks = ctl_parser.get_blocks()
        self.assertEqual(len(blocks), 1)
        block = blocks[0]
        sub_blocks = block.blocks
        sub_block_map = {b.start: b for b in sub_blocks}

        # Check B, C, S, T and W sub-blocks
        i = 0
        for a in range(start, end, length):
            for offset, subctl, lengths in (
                (0, 'C', ((None, None),)),
                (5, 'B', ((1, None),)),
                (6, 'B', ((2, None),)),
                (10, 'S', ((None, None),)),
                (16, 'W', ((4, None),)),
                (20, 'T', ((4, None), (1, 'B')),)
            ):
                address = a + offset
                self.assertIn(address, ctl_parser.subctls)
                self.assertEqual(ctl_parser.subctls[address], subctl.lower())
                self.assertEqual(lengths, sub_blocks[i].sublengths)
                i += 1

        # Check mid-block comments
        offset = 10
        for a in range(start + offset, end, length):
            self.assertEqual(['A mid-block comment'], sub_block_map[a].header)

        # Check multi-line comments
        offset = 10
        for a in range(start + offset, end, length):
            self.assertEqual((a + 9, 'A multi-line comment'), sub_block_map[a].multiline_comment)

        # Check entry-level directives (c, D, E, R)
        ctls = ctl_parser.ctls
        self.assertIn(start, ctls)
        self.assertEqual(ctls[start], 'c')
        self.assertEqual(['This entry description should not be repeated'], block.description)
        self.assertEqual([['HL', 'This register should not be repeated']], block.registers)
        self.assertEqual(['This end comment should not be repeated'], block.end_comment)
        for a in range(start + length, end, length):
            self.assertNotIn(a, ctls)

        # Check entry-level ASM directives
        self.assertEqual([('start', None), ('org', '30000')], block.asm_directives)

        # Check instruction-level ASM directives
        offset = 20
        self.assertEqual([('label', 'END')], ctl_parser.get_instruction_asm_directives(start + offset))
        for a in range(start + offset + length, end, length):
            self.assertEqual((), ctl_parser.get_instruction_asm_directives(a))

    def test_loop_including_entries(self):
        start = 40000
        length = 25
        count = 3
        end = start + length * count
        ctl = '\n'.join((
            '; @start:40000',
            '@ 40000 org=40000',
            'c 40000 This entry should be repeated',
            'D 40000 This entry description should be repeated',
            'R 40000 HL This register should be repeated',
            '  40000,5 Begin',
            'B 40005,5,1,2',
            'D 40010 A mid-block comment',
            'M 40010,10 A multi-line comment',
            'S 40010,6',
            'W 40016,4,4',
            '; @label:40020=END',
            'T 40020,5,4:B1 End',
            'E 40000 This end comment should be repeated',
            'L {},{},{},1'.format(start, length, count)
        ))
        ctl_parser = self._get_ctl_parser(ctl)
        blocks = ctl_parser.get_blocks()
        sub_block_map = {s.start: s for b in blocks for s in b.blocks}

        # Check B, C, S, T and W sub-blocks
        i = 0
        for a in range(start, end, length):
            sub_blocks = blocks[i].blocks
            j = 0
            for offset, subctl, lengths in (
                (0, 'C', ((None, None),)),
                (5, 'B', ((1, None),)),
                (6, 'B', ((2, None),)),
                (10, 'S', ((None, None),)),
                (16, 'W', ((4, None),)),
                (20, 'T', ((4, None), (1, 'B')),)
            ):
                address = a + offset
                self.assertIn(address, ctl_parser.subctls)
                self.assertEqual(ctl_parser.subctls[address], subctl.lower())
                sub_block = sub_blocks[j]
                self.assertEqual(sub_block.start, address)
                self.assertEqual(lengths, sub_block.sublengths)
                j += 1
            i += 1

        # Check mid-block comments
        offset = 10
        for a in range(start + offset, end, length):
            self.assertEqual(['A mid-block comment'], sub_block_map[a].header)

        # Check multi-line comments
        offset = 10
        for a in range(start + offset, end, length):
            self.assertIn(a, ctl_parser.multiline_comments)
            self.assertEqual((a + 9, 'A multi-line comment'), ctl_parser.multiline_comments[a])

        # Check entry-level directives (c, D, E, R)
        ctls = ctl_parser.ctls
        for i, a in enumerate(range(start, end, length)):
            self.assertIn(a, ctls)
            self.assertEqual(ctls[a], 'c')
            self.assertEqual(['This entry description should be repeated'], blocks[i].description)
            self.assertEqual([['HL', 'This register should be repeated']], blocks[i].registers)
            self.assertEqual(['This end comment should be repeated'], blocks[i].end_comment)

        # Check entry-level ASM directives
        self.assertEqual([('start', None), ('org', '40000')], blocks[0].asm_directives)
        for block in blocks[1:]:
            self.assertEqual((), block.asm_directives)

        # Check instruction-level ASM directives
        offset = 20
        self.assertEqual([('label', 'END')], ctl_parser.get_instruction_asm_directives(start + offset))
        for a in range(start + offset + length, end, length):
            self.assertEqual((), ctl_parser.get_instruction_asm_directives(a))

    def test_loop_crossing_64k_boundary(self):
        ctl = '\n'.join((
            'u 65532',
            'W 65532,2',
            'L 65532,2,3'
        ))
        ctl_parser = self._get_ctl_parser(ctl)
        warnings = self.err.getvalue().split('\n')

        # Check warning
        self.assertEqual(warnings[0], 'WARNING: Loop crosses 64K boundary:')
        self.assertEqual(warnings[1], 'L 65532,2,3')

        # Check that the W sub-block is repeated anyway
        subctls = ctl_parser.subctls
        self.assertIn(65534, subctls)
        self.assertEqual(subctls[65534], 'w')

    def test_loop_with_entries_crossing_64k_boundary(self):
        ctl = '\n'.join((
            'b 65534',
            'L 65534,1,4,1'
        ))
        ctl_parser = self._get_ctl_parser(ctl)
        warnings = self.err.getvalue().split('\n')

        # Check warning
        self.assertEqual(warnings[0], 'WARNING: Loop crosses 64K boundary:')
        self.assertEqual(warnings[1], 'L 65534,1,4,1')

        # Check that there is no block that starts past the boundary
        blocks = ctl_parser.get_blocks()
        self.assertEqual(blocks[-1].start, 65535)

if __name__ == '__main__':
    unittest.main()
