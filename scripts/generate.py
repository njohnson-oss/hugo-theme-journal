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
import subprocess
import shutil


if __name__ == '__main__':
    root_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)), os.pardir)), os.pardir))
    output_dir = os.path.join(root_dir, "public")
    gemini_output_dir = os.path.join(root_dir, "capsule")
    html_output_dir = os.path.join(root_dir, "website")

    # detect static Gemini files
    os.chdir(os.path.join(root_dir, "static"))
    static_gemini_files = [os.path.join(root, name) for root, dirs, files in os.walk(".") for name in files if name.endswith(".gmi")]

    # generate output directory
    os.chdir(root_dir)
    subprocess.run("hugo")

    # generate Gemini output directory
    try:
        shutil.copytree(output_dir, gemini_output_dir, ignore=shutil.ignore_patterns("*.html"), dirs_exist_ok=True)
    except shutil.Error:
        pass

    os.chdir(os.path.join(root_dir, "static"))

    os.chdir(gemini_output_dir)
    os.remove("robots.txt")
    os.remove("sitemap.xml")
    shutil.move(os.path.join("gemini_atom", "atom.xml"), "atom.xml")
    os.rmdir("gemini_atom")
    for file in static_gemini_files:
        shutil.copy(os.path.join(output_dir, file), file)

    # generate HTML output directory
    try:
        shutil.copytree(output_dir, html_output_dir, ignore=shutil.ignore_patterns("*.gmi", "gemini_atom"), dirs_exist_ok=True)
    except shutil.Error:
        pass

    os.chdir(html_output_dir)
    for file in static_gemini_files:
        shutil.copy(os.path.join(output_dir, file), file)
