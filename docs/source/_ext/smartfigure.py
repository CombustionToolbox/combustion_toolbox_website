import os
from docutils import nodes

def replace_figure_extensions(app, doctree, fromdocname):
    builder = app.builder.name
    ext = '.svg' if builder == 'html' else '.pdf'

    for node in doctree.traverse(nodes.image):
        basename, current_ext = os.path.splitext(node['uri'])
        if current_ext.lower() in ['.svg', '.pdf', '.png']:
            node['uri'] = basename + ext

def setup(app):
    app.connect('doctree-resolved', replace_figure_extensions)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
