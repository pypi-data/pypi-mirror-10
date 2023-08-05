# -*- coding: utf-8 -*-
from os import makedirs
from os.path import join as pj, exists, isdir, dirname
import codecs

from .generator import Generator


def _write(content, filename):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(content)


def echo(string, level='info'):
    color = dict(
        info='\033[92m',
        warn='\033[93m'
    )
    end = '\033[0m'
    print '%s%s%s' % (color[level], string, end)


def write(model, base_path, appname='app', overwrite=False, ui=False):
    app_path = pj(base_path, appname)
    bp_path = pj(app_path, model.blueprint)
    api_path = pj(bp_path, 'api')
    if not isdir(api_path):
        makedirs(api_path)

    layouts = dict(
        requirements=dict(
            path=pj(base_path, 'requirements.txt'),
            overwrite=False),
        app=dict(
            path=pj(app_path, '__init__.py'),
            overwrite=False),
        blueprint=dict(
            path=pj(bp_path, '__init__.py'),
            overwrite=False),
        api=dict(
            path=pj(api_path, '__init__.py'),
            overwrite=False),
        routes=dict(
            path=pj(bp_path, 'routes.py'),
            overwrite=True),
        schemas=dict(
            path=pj(bp_path, 'schemas.py'),
            overwrite=True),
        validators=dict(
            path=pj(bp_path, 'validators.py'),
            overwrite=True),
        filters=dict(
            path=pj(bp_path, 'filters.py'),
            overwrite=True),
    )

    g = Generator(model)

    for item, info in layouts.iteritems():
        if info['overwrite'] or overwrite or not exists(info['path']):
            _write(getattr(g, 'generate_%s' % item)(), info['path'])
            echo('"' + info['path'] + '" generated.', 'warn')
        else:
            echo('"' + info['path'] + '" already exists, skipped.')

    for name, view in g.generate_views():
        path = pj(api_path, '%s.py' % name)
        if overwrite or not exists(path):
            _write(view, path)
            echo('"' + path + '" generated.', 'warn')
        else:
            echo('"' + path + '" already exists, skipped.')

    if ui:
        from distutils.dir_util import copy_tree

        ui_path = pj(app_path, 'static/swagger-ui')
        if not isdir(ui_path):
            makedirs(ui_path)
        ui_src = pj(dirname(__file__), 'templates/ui')
        copy_tree(ui_src, ui_path)
        echo('swagger ui generated', 'warn')
