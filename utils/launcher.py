import os
import subprocess
import ctypes


def launch_app(path: str):

    if not path:
        return

    if not os.path.exists(path):
        return

    folder = os.path.dirname(path)

    try:
        subprocess.Popen(path, cwd=folder)

    except OSError as e:

        # WinError 740 = Requires elevation
        if getattr(e, "winerror", None) == 740:

            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                path,
                None,
                folder,
                1
            )

        else:
            raise