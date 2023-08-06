#!/usr/bin/env python

#=======================================================================
# Authors: Ben Woodcroft, Joel Boyd
#
# Unit tests.
#
# Copyright
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License.
# If not, see <http://www.gnu.org/licenses/>.
#=======================================================================

import unittest
import os.path
import sys
import tempfile

path_to_script = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','bin','graftM')
path_to_data = os.path.join(os.path.dirname(os.path.realpath(__file__)),'data')

sys.path = [os.path.join(os.path.dirname(os.path.realpath(__file__)),'..')]+sys.path
from graftm.getaxnseq import Getaxnseq

class Tests(unittest.TestCase):
    
    def test_hello_world(self):
        with tempfile.NamedTemporaryFile(prefix='graftm_test_getaxnseq') as tmp_seq:
            with tempfile.NamedTemporaryFile(prefix='graftm_test_getaxnseq') as tmp_tax:
                Getaxnseq().write_taxonomy_and_seqinfo_files({'seq1': ['k__me','p__you'],
                                                              'seq2': []},
                                                             tmp_tax.name,
                                                             tmp_seq.name)
                expected = "\n".join([','.join(p) for p in [['seqname','tax_id'],
                    ['seq2','Root'],
                    ['seq1','p__you']]])+"\n"
                self.assertEqual(expected, open(tmp_seq.name).read())
                expected = '\n'.join(['tax_id,parent_id,rank,tax_name,root,kingdom,phylum,class,order,family,genus,species',
                                      'Root,Root,root,Root,Root,,,,,,,',
                                      'k__me,Root,kingdom,k__me,Root,k__me,,,,,,',
                                      'p__you,k__me,phylum,p__you,Root,k__me,p__you,,,,,'])+"\n"
                self.assertEqual(expected, open(tmp_tax.name).read())

        

if __name__ == "__main__":
    unittest.main()
