#!/usr/bin/python3
from jinja2 import Template
from collections import namedtuple


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
    menu = render_page('templates/menu.html.jinja', {"menu_items": menu_items})
    getting_started = render_page('templates/getting-started.html.jinja')
    index = render_page(
        'templates/index.html.jinja',
        {
            "banner": banner,
            "menu": menu,
            "content": getting_started,
        }
    )
    with open('index.html', 'w') as f:
        f.write(index)


if __name__ == "__main__":
    run()
