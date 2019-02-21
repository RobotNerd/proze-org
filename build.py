#!/usr/bin/python3
from collections import namedtuple
from jinja2 import Template
import htmlmin
import sass


Menu = namedtuple('Menu', ['name', 'route'])
MENU_ITEMS = [
    Menu('Getting started', 'getting-started.html'),
    Menu('Syntax', 'syntax.html'),
    Menu('Tools', 'tools.html'),
    Menu('Documentation', 'documentation.html'),
]


def build_styles():
    """Generate CSS file from sass files."""
    css = sass.compile(
        filename='styles/main.scss',
        output_style='compressed'
    )
    with open('main.css', 'w') as f:
        f.write(css)


def build_pages():
    """Generate html content."""
    banner = render_page('templates/banner.html.jinja')
    generate_page_content(banner, 'Home', 'index.html')
    generate_page_content(banner, 'Getting started', 'getting-started.html')
    generate_page_content(banner, 'Syntax', 'syntax.html')
    generate_page_content(banner, 'Tools', 'tools.html')
    generate_page_content(banner, 'Documentation', 'documentation.html')


def generate_page_content(banner, page_name, filename):
    content = render_page(
        'templates/base.html.jinja',
        {
            "banner": banner,
            "menu": render_page(
                'templates/menu.html.jinja',
                {
                    "current_page": page_name,
                    "menu_items": MENU_ITEMS,
                }
            ),
            "content": render_page('templates/{}.jinja'.format(filename)),
        }
    )
    with open(filename, 'w') as f:
        f.write(htmlmin.minify(content))


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
