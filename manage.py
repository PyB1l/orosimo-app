# -*- coding:utf-8 -*-
"""Application manager module.

Provides script commands for deploying, testing, building.
"""

import app
import bottle
import click
import subprocess
from settings import SERVER_OPTS, DBEngine, POSTGRES, DEBUG


@click.group()
def manager():
    pass


@manager.command()
@click.option('--path', type=str, help='Success File for uploading')
@click.option('--year', type=int, help='The year of success models.')
def upload_success(path, year):
    """Upload a .txt file with successes to OROSHMO Database.

    Args:
        path (str): The path of the success file.
        year (int): The year of success.

    Returns:
        Status code (int) and message.
    """

    try:
        with open(path, 'r') as input_file:
            success_data = input_file.read()

    except (IOError, FileNotFoundError):
        print('Status 404: {} not found!'.format(path))
        return 404

    sql_command = """INSERT INTO admin.success (full_name, school_year, university, promoted) values\n"""
    sql_context = """('{}', {}, '{}', {})"""
    query_set = []

    lines = [line for line in success_data.split('\n')]

    for line in lines:
        if line.strip():
            cleaned_line = [i.strip() for i in line.split(' ') if i.strip()]
            name = '{} {}'.format(cleaned_line[0], cleaned_line[1])
            school = ' '.join(cleaned_line[2:])
            query_set.append(sql_context.format(name, year, school, 'False'))

    query_engine = DBEngine.make(**POSTGRES)

    sql_insert = sql_command + ',\n'.join(query_set) + '\n returning id'

    data = query_engine.query(sql_insert, fetch_opts='many')

    print('Inserted {} rows'.format(len(data) if data else 0))
    return 20


@manager.command()
@click.option('--host', default=SERVER_OPTS['host'], type=str, help='Set Application server host.')
@click.option('--port', default=SERVER_OPTS['port'], type=int, help='Set Application server port.')
@click.option('--server', default=SERVER_OPTS['server'], type=str, help='Set Application server wsgi container.')
@click.option('--reloader', default=True, type=bool, help='Set Application server host reloader option.')
@click.option('--debug', default=DEBUG, type=bool, help='Set Application server host debug mode.')
def run(host, port, server, reloader, debug):
    """deploy application

    Args:
        host (str): Application IP or domain name.
        port (int): Application port.
        server (str): Application wsgi server alias.
        reloader (bool): Enable Application auto-reload on change.
        debug (bool): Enable Application DEBUG mode.
    """

    bottle.debug(debug)

    bottle.run(
        app=app.wsgi,
        server=server,
        host=host,
        port=port ,
        reloader=reloader
    )


@manager.command()
def js_build():
    return subprocess.Popen(
        ('riot  --ext tag.html static/app/js/src/tags static/app/js/build/;'
         ' node_modules/babel-cli/bin/babel.js static/app/js/build/ --out-dir static/app/js/dist/tags;'
         ' node_modules/babel-cli/bin/babel.js static/app/js/src --out-dir static/app/js/dist/'),
        shell=True
    )


@manager.command()
def build():
    """Compile Web components in plain javascript.
    """
    subprocess.Popen(
        ["riot", "components/app", "static/app/components"]
    )

    subprocess.Popen(
        ["riot", "components/admin", "static/admin/components"]
    )

if __name__ == '__main__':

    manager()
