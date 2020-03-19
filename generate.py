# generate site from static pages, loosely inspired by Jekyll
# run like this:
#   ./generate.py test/source output
# the generated `output` should be the same as `test/expected_output`

#!/usr/bin/env python3

# need json and sys too
import json
import logging
import os
import sys

import jinja2

log = logging.getLogger(__name__)


def list_files(folder_path):
    for name in os.listdir(folder_path):
        base, ext = os.path.splitext(name)
        if ext != '.rst':
            continue
        # get the name of the file too
        yield os.path.join(folder_path, name), os.path.basename(base)

def read_file(file_path):
    # see the file as utf8 coded, not binary
    with open(file_path, 'r') as f:
        raw_metadata = ""
        for line in f:
            if line.strip() == '---':
                break
            raw_metadata += line
        content = ""
        for line in f:
            content += line
    return json.loads(raw_metadata), content

def write_output(name, html):
    # TODO should not use sys.argv here, it breaks encapsulation
    # add path and create directory if not exists 
    current = os.path.join('test', sys.argv[2])
    if not os.path.exists(current):
        os.makedirs(current)
    # join name with path
    with open(os.path.join(current, name+'.html'), 'w') as f:
        f.write(html)

def generate_site(folder_path):
    log.info("Generating site from %r", folder_path)
    print("folder_path: " + folder_path)
    # FileSystemLoader its from jinja2
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(folder_path + '/layout'))
    for file_path, name in list_files(folder_path):
        metadata, content = read_file(file_path)
        # look for layout as template
        template_name = metadata['layout']
        template = jinja_env.get_template(template_name)
        data = dict(metadata, content=content)
        # render data
        html = template.render(**data)
        write_output(name, html)
        log.info("Writing %r with template %r", name, template_name)


def main():
    generate_site(sys.argv[1])


if __name__ == '__main__':
    logging.basicConfig()
    main()
