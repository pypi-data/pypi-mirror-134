import os as __os
import subprocess
import atexit
import platform


def casafeather(cleanup=True):
    app_name = ""
    if platform.system() == "Darwin":
        app_name = "casafeather/__bin__/casafeather.app/Contents/MacOS/casafeather"
    elif platform.system() == "Linux":
        app_name = "casafeather/__bin__/casafeather-x86_64.AppImage"
    else:
        raise Exception("Unsupported platform")

    app_path = __os.path.join(
        __os.path.abspath(__os.path.join(__os.path.dirname(__file__), "..")),
        app_name,
    )

    try:
        print("Starting CASAfeather\n")
        p = subprocess.Popen(app_path)
        if cleanup:

            @atexit.register
            def stop_casafeather():
                print("Exiting CASAfeather\n")
                p.kill()

    except FileNotFoundError as error:
        print(f"Error: {error.strerror}")


if __name__ == "__main__":
    casafeather(False)
