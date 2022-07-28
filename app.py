import argparse
import logging
import subprocess

from flask import Flask
from wrenchbox.logging import setup_log

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def root():
    s = subprocess.check_output(['git -C {} pull'.format(args.path)], shell=True)
    return s.decode('UTF-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', default=False, help='show debug information')
    parser.add_argument('--port', type=int, default=8080, help='listening port')
    parser.add_argument('path', type=str, help='monitoring git path, git will pull if triggered')
    args, _ = parser.parse_known_args()
    setup_log(level=logging.DEBUG if args.debug else logging.INFO)
    app.run('0.0.0.0', args.port)
