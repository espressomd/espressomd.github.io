#
# Copyright (C) 2021 The ESPResSo project
#
# This file is part of ESPResSo.
#
# ESPResSo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ESPResSo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
This script generates the landing page for tutorials.
"""

import re

marker_begin = '[comment]: # (Begin of tutorials landing page)'
marker_end = '[comment]: # (End of tutorials landing page)'

with open('build/doc/tutorials/Readme.md') as f:
    content = f.read()

assert marker_begin in content, f'Readme.md is missing "{marker_begin}"'
assert marker_end in content, f'Readme.md is missing "{marker_end}"'
tutorial_descriptions = content.split(marker_begin)[1].split(marker_end)[0]
tutorial_descriptions = tutorial_descriptions.replace('.ipynb', '.html')
tutorial_descriptions = re.sub(r"\]\((?!https?://)", '](tutorials/', tutorial_descriptions)

with open('tutorials_header.md', 'r') as f:
    tutorial_header = f.read()

with open('tutorials.md', 'w') as f:
    f.write(tutorial_header + tutorial_descriptions)
