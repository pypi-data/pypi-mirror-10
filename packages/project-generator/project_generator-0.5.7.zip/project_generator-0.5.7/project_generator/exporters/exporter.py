# Copyright 2014-2015 0xc0170
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import logging

from os.path import join, dirname
from jinja2 import Template, StrictUndefined


class Exporter:

    """Just a template for subclassing"""

    TEMPLATE_DIR = join(dirname(__file__), '..','templates')
    DOT_IN_RELATIVE_PATH = False

    def get_dest_path(self, data, tool, destination, dir_name):
        dest = {
            'dest_path' : '',
            'rel_path' : '',
        }
        if destination is '':
            destination = 'generated_projects'
        if not os.path.exists(destination):
            os.makedirs(destination)
        if dir_name is '':
            dir_name = tool + '_' + data['name']
        project_dir = join(destination, dir_name)
        # else:
        #     project_dir=destination
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        # target_path = join(project_dir, target_file)

        # Get number of how far we are from root, to set paths in the project
        # correctly
        # path_from_root, filename = os.path.split(target_path)
        count = len(os.path.split(project_dir))
        rel_path_output = ''

        dest['rel_count'] = count
        while count:
            rel_path_output = join('..', rel_path_output)
            count = count - 1
        dest['dest_path'] = project_dir
        dest['rel_path'] = rel_path_output
        return dest

    def gen_file(self, template_file, data, output, dest_path):
        output = join(dest_path, output)
        logging.debug("Generating: %s" % output)

        """ Fills data to the project template, using jinja2. """
        template_path = join(self.TEMPLATE_DIR, template_file)
        template_text = open(template_path).read()
        template = Template(template_text) # TODO: undefined=StrictUndefined - this needs fixes in templates
        target_text = template.render(data)

        open(output, "w").write(target_text)
        return dirname(output), output

    def fixup_executable(self, exe_path):
        return exe_path

    def is_supported_by_default(self, target):
        return False
