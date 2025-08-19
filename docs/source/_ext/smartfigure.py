import os
from docutils import nodes

def replace_figure_extensions(app, doctree, fromdocname):
    builder = app.builder.name
    ext = '.svg' if builder == 'html' else '.pdf'

    for node in doctree.traverse(nodes.image):
        uri = node['uri']
        basename, current_ext = os.path.splitext(uri)

        if current_ext.lower() in ['.svg', '.pdf', '.png']:
            new_uri = basename + ext

            # For LaTeX builds, remove leading slash if present
            if builder == 'latex' and new_uri.startswith('/_static'):
                new_uri = new_uri[1:]  # remove leading "/"

            node['uri'] = new_uri

def setup(app):
    app.connect('doctree-resolved', replace_figure_extensions)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
