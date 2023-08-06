import os
import pathlib
import logging
import uuid

import re
import string
import sys

from slugify import slugify
import jinja2
import click


try:
    MODEL_CONFIG = pathlib.Path(os.environ['MODEL_CONFIG_LIST_FILEPATH_YAML'])
except KeyError:
    raise ValueError('Environment vairable `MODEL_CONFIG_LIST_FILEPATH_YAML` is not set!')


TEMPLATE = '''{% for name in labels -%}
{{name}}:
  1:
    py_model_path: {{ paths[loop.index-1] }}
    py_interpreter_path: {{ py_interpreter }}
    py_model_interface_filepath: {{ this_file }}
    py_model_interface_class_name: Model
    __cpu_affinity_friendly__: true
    __do_not_do_cpu_affinity_friendly_eval__: true
{% endfor %}'''
template = jinja2.Template(TEMPLATE)


def retrieve_model_type_and_path(path, separator='//'):
    t, s, p = path.partition(separator)
    if s == separator:
        if len(t) == 0:
            t = None
    else:
        p = t
        t = None
    return t, p


@click.command()
@click.argument('models_string')
@click.option('--check/--no-check', 'check', default=True)
@click.option('--pass-unknown-paths', is_flag=True, default=False)
def create_model_config(models_string: str, check: bool, pass_unknown_paths: bool):
    labels = []
    paths = []
    class_names = []
    for s in models_string.split(':'):
        if len(s) == 0:
            continue
        model_type, s = retrieve_model_type_and_path(s)
        label = re.search(r'\[(.*?)\]',s)
        if label is not None:
            path = s.replace(label.group(), '')
            path = pathlib.Path(path)
            label = slugify(label.group()[1:-1])
            if len(label) == 0:
                label = None
        if label is None:
            path = pathlib.Path(s)
            label = slugify(path.stem)
        label = label.lstrip(string.digits)
        class_name = re.sub("[^0-9a-zA-Z_]+", "", label.replace('-', '_').lstrip(string.digits))
        if check and not path.exists() and not pass_unknown_paths:
            logging.warning(f'Path `{path}` does not exist!')
            break
        elif not path.exists() and pass_unknown_paths:
            txt_file = MODEL_CONFIG.parent / pathlib.Path(f'{uuid.uuid1()}.model_string')
            with txt_file.open('w') as stream:
                stream.write(str(path))
            path = txt_file
        if label not in labels and class_name not in class_names:
            path_str = path if not model_type else f'{model_type}//{path}'
            paths.append(path_str)
            labels.append(label)
            class_names.append(class_name)
    with MODEL_CONFIG.open('w') as stream:
        stream.write(template.render(labels=labels,
                                     paths=paths,
                                     class_names=class_names,
                                     py_interpreter=sys.executable,
                                     this_file=pathlib.Path(__file__).absolute()))


if __name__ == "__main__":
    create_model_config()
