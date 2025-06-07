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
This script generates the landing page for video lectures.
"""

marker_begin = '[comment]: # (Begin of videos landing page)'
marker_end = '[comment]: # (End of videos landing page)'

with open('build/doc/tutorials/Readme.md') as f:
    content = f.read()

assert marker_begin in content, f'Readme.md is missing "{marker_begin}"'
assert marker_end in content, f'Readme.md is missing "{marker_end}"'
video_descriptions = content.split(marker_begin)[1].split(marker_end)[0]

with open('videos_header.md', 'r') as f:
    video_header = f.read()

with open('videos.md', 'w') as f:
    f.write(video_header + video_descriptions)
