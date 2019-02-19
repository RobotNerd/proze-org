#!/usr/bin/python3
from collections import namedtuple
from jinja2 import Template
import htmlmin


Menu = namedtuple('Menu', ['name', 'route'])
menu_items = [
    Menu('Getting started', 'getting-started.html'),
    Menu('Syntax', 'syntax.html'),
    Menu('Tools', 'tools.html'),
    Menu('Documentation', 'documentation.html'),
]


def render_page(path, args={}):
    with open(path, 'r') as f:
        template = Template(f.read())
    return template.render(args)


def run():
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


if __name__ == "__main__":
    run()
