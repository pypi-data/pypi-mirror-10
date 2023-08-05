# -*- coding: utf-8 -*-
# PyMedTermino
# Copyright (C) 2012-2013 Jean-Baptiste LAMY
# LIMICS (Laboratoire d'informatique médicale et d'ingénierie des connaissances en santé), UMR_S 1142
# University Paris 13, Sorbonne paris-Cité, Bobigny, France

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Creates VCM SQL databases from the VCM ontology.

import sys, os, os.path, sqlite3
from pymedtermino.utils.mapping_db import *


HERE              = os.path.dirname(sys.argv[0])
ONTOLOGY_PATH     = os.path.join(HERE, "..", "vcm_onto")
SQLITE_FILE3      = os.path.join(HERE, "..", "vcm_concept_monoaxial_2_vcm_lexicon.sqlite3")
SQLITE_FILE4      = os.path.join(HERE, "..", "snomedct_2_vcm_concept.sqlite3")

db = create_db(SQLITE_FILE3)
Txt_2_SQLMapping(os.path.join(ONTOLOGY_PATH, "vcm_concept_monoaxial_2_vcm_lexicon.txt"), db, code1_type = "INTEGER", code2_type = "INTEGER")
close_db(db, SQLITE_FILE3)

db2 = create_db(SQLITE_FILE4)
Txt_2_SQLMapping(os.path.join(ONTOLOGY_PATH, "snomedct_2_vcm_concept_reverse.txt"), db2, code1_type = "INTEGER", code2_type = "INTEGER", reverse = 1)
close_db(db2, SQLITE_FILE4)
