#!/usr/bin/env python3
"""One-command launcher for the SkelmMC documentation hub (stdlib only)."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
ENV_DIR = ROOT / '.venv'
ENV_PYTHON = ENV_DIR / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')


def run(args: list[str]) -> int:
    try:
        return subprocess.call(args, cwd=str(ROOT))
    except OSError as error:
        print(f'Unable to run command: {error}', file=sys.stderr)
        return 1


def has_dependencies(python: Path) -> bool:
    check = [str(python), '-c', 'import yaml, jinja2, markdown_it, pygments, bs4']
    try:
        return subprocess.run(check, cwd=str(ROOT), stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL, check=False).returncode == 0
    except OSError:
        return False


def environment() -> Path | None:
    """Use already-installed dependencies or bootstrap a local, isolated environment."""
    # Avoid unnecessary installation for people who have run pip install manually.
    if ENV_PYTHON.is_file() and has_dependencies(ENV_PYTHON):
        return ENV_PYTHON
    if has_dependencies(Path(sys.executable)):
        return Path(sys.executable)
    if not ENV_PYTHON.is_file():
        print('Creating a local Python environment (.venv) ...', flush=True)
        if run([sys.executable, '-m', 'venv', str(ENV_DIR)]):
            print('Could not create .venv. Check that Python includes the venv module.', file=sys.stderr)
            return None
    print('Installing site build dependencies ...', flush=True)
    if run([str(ENV_PYTHON), '-m', 'pip', 'install', '--disable-pip-version-check', '-r', 'requirements.txt']):
        print('Dependency installation failed. Check your internet connection and Python/pip setup.', file=sys.stderr)
        return None
    if not has_dependencies(ENV_PYTHON):
        print('Installed packages could not be imported. Please check the errors above.', file=sys.stderr)
        return None
    return ENV_PYTHON


def build() -> int:
    py = environment()
    if py is None:
        return 1
    return run([str(py), 'build.py'])


def add_project(slug: str | None = None, name: str | None = None) -> int:
    if not slug:
        slug = input('Project URL slug (e.g. skelm-shop): ').strip()
    if not name:
        name = input('Project display name (e.g. SkelmShop): ').strip()
    if not slug or not name:
        print('A slug and display name are required.', file=sys.stderr)
        return 2
    py = environment()
    if py is None:
        return 1
    status = run([str(py), 'scripts/add_project.py', '--slug', slug, '--name', name])
    if status:
        return status
    print('Rebuilding documentation with the new project ...', flush=True)
    return run([str(py), 'build.py'])


def preview(port: int) -> int:
    folder = ROOT / 'dist'
    if not (folder / 'index.html').exists():
        print('Missing built site. Run `python manage.py build` first.', file=sys.stderr)
        return 1
    handler = partial(SimpleHTTPRequestHandler, directory=str(folder))
    try:
        with ThreadingHTTPServer(('127.0.0.1', port), handler) as server:
            print(f'Preview ready at http://localhost:{port}/', flush=True)
            print('Keep this terminal open while viewing the docs. Press Ctrl+C to stop.', flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print('\nPreview stopped.')
    except OSError as error:
        print(f'Cannot start preview on port {port}: {error}', file=sys.stderr)
        print('Try another port: python manage.py preview --port 8081', file=sys.stderr)
        return 1
    return 0


def menu() -> int:
    print('\nSkelmMC Documentation Hub\n' + '-' * 28)
    print('1. Preview website (no installation required)')
    print('2. Add a new SkelmMC project (automatically rebuilds)')
    print('3. Rebuild documentation')
    print('4. Install/update build dependencies')
    print('5. Exit')
    choice = input('\nChoose 1-5: ').strip()
    if choice == '1':
        return preview(8080)
    if choice == '2':
        return add_project()
    if choice == '3':
        return build()
    if choice == '4':
        return 0 if environment() else 1
    if choice == '5':
        return 0
    print('Invalid choice.')
    return 2


def main() -> int:
    parser = argparse.ArgumentParser(description='Manage the SkelmMC documentation hub')
    actions = parser.add_subparsers(dest='action')
    add = actions.add_parser('add', help='Add and build a project; prompts for missing details')
    add.add_argument('--slug', help='Lowercase URL path (e.g. skelm-shop)')
    add.add_argument('--name', help='Public project display name')
    actions.add_parser('build', help='Install dependencies if needed and generate the docs')
    serve = actions.add_parser('preview', help='View the precompiled site in your browser')
    serve.add_argument('--port', type=int, default=8080)
    actions.add_parser('setup', help='Install build dependencies into .venv')
    args = parser.parse_args()
    if args.action == 'add':
        return add_project(args.slug, args.name)
    if args.action == 'build':
        return build()
    if args.action == 'preview':
        if not 1 <= args.port <= 65535:
            parser.error('--port must be between 1 and 65535')
        return preview(args.port)
    if args.action == 'setup':
        return 0 if environment() else 1
    return menu()


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print('\nCancelled.')
        raise SystemExit(130)
