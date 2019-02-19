#!/usr/bin/python3
from collections import namedtuple
from jinja2 import Template
import htmlmin
import sass


Menu = namedtuple('Menu', ['name', 'route'])
menu_items = [
    Menu('Getting started', 'getting-started.html'),
    Menu('Syntax', 'syntax.html'),
    Menu('Tools', 'tools.html'),
    Menu('Documentation', 'documentation.html'),
]
styles = [
    'body',
    'menu',
    'banner',
]


def build_styles():
    """Generate CSS file from sass files."""
    css = ''
    for style in styles:
        css += sass.compile(
            filename='styles/{}.scss'.format(style),
            output_style='compressed'
        )
    with open('main.css', 'w') as f:
        f.write(css)


def build_pages():
    """Generate html content."""
    banner = render_page('templates/banner.html.jinja')
    index = render_page(
        'templates/index.html.jinja',
        {
            "banner": banner,
            "menu": render_page(
                'templates/menu.html.jinja',
                {
                    "current_page": "Home",
                    "menu_items": menu_items,
                }
            ),
            "content": render_page('templates/home.html.jinja'),
        }
    )
    with open('index.html', 'w') as f:
        f.write(htmlmin.minify(index))


def render_page(path, args={}):
    """Convert a jinja template to an html file."""
    with open(path, 'r') as f:
        template = Template(f.read())
    return template.render(args)


def run():
    build_styles()
    build_pages()


if __name__ == "__main__":
    run()
