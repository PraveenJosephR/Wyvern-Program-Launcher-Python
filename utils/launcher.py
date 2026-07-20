import os
import subprocess


def launch_app(path: str):

    if not path:
        return

    if not os.path.exists(path):
        return

    folder = os.path.dirname(path)

    subprocess.Popen(path, cwd=folder)