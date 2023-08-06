import sys, pathlib

def find_up(startdir, filename):
    d = pathlib.Path(startdir)
    # 相对路径没办法一直向上 parent
    d = d.resolve()
    while True:
        attempt = d / filename
        if attempt.exists():
            return attempt
        p = d.parent
        if d == p:
            return None
        d = p

prodir = None

def _sys_path_prepend_pyproject_toml_dir():
    main = sys.modules["__main__"]
    if hasattr(main, "__file__"):
        startdir = main.__file__
    else:
        startdir = str(pathlib.Path.cwd())
    profile = find_up(startdir, "pyproject.toml")
    assert profile is not None
    global prodir
    prodir = profile.parent
    prodirstr = str(prodir)
    if prodirstr not in sys.path:
        sys.path.insert(0, prodirstr)

_sys_path_prepend_pyproject_toml_dir()
