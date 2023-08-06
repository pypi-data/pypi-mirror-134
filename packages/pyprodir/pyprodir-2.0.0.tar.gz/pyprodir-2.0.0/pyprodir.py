import sys, pathlib, inspect


def _find_up(startdir, filename):
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

_prodir = None

_importers = [x.filename for x in inspect.stack(0)[1:] if not x.filename.startswith("<")]
if _importers:
    _profile = _find_up(_importers[0], "pyproject.toml")
    if _profile:
        _prodir = _profile.parent
        _prodirstr = str(_prodir)
        if _prodirstr not in sys.path:
            sys.path.insert(0, _prodirstr)


