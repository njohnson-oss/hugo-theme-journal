'''
    journal  Generates a Gemini capsule from existing files
    Copyright (C) 2022  Nicholas Johnson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os
import shutil


if __name__ == '__main__':
    root_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)), os.pardir)), os.pardir))
    output_dir = os.path.join(root_dir, "public")
    gemini_output_dir = os.path.join(root_dir, "capsule")
    html_output_dir = os.path.join(root_dir, "website")

    # delete output directories
    shutil.rmtree(output_dir, ignore_errors=True)
    shutil.rmtree(gemini_output_dir, ignore_errors=True)
    shutil.rmtree(html_output_dir, ignore_errors=True)
