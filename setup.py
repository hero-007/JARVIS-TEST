
from cx_Freeze import setup, Executable

base = None


executables = [Executable("sample.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "heroku",
    options = options,
    version = "12546",
    description = 'my first py2exe conversion',
    executables = executables
)

