from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class SmartFigure(SphinxDirective):
    required_arguments = 1  # image path without extension
    has_content = True
    option_spec = {
        'width': lambda x: x,
        'align': lambda x: x,
    }

    def run(self):
        env = self.state.document.settings.env
        builder = env.app.builder.name
        img_base = self.arguments[0]
        ext = '.svg' if builder == 'html' else '.pdf'
        img_path = f"{img_base}{ext}"

        fig = nodes.figure()
        if 'width' in self.options:
            fig['width'] = self.options['width']
        if 'align' in self.options:
            fig['align'] = self.options['align']

        image_node = nodes.image(uri=img_path)
        fig += image_node

        self.state.nested_parse(self.content, self.content_offset, fig)
        return [fig]

def setup(app):
    app.add_directive("smartfigure", SmartFigure)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
