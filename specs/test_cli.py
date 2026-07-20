import json
import subprocess
import sys

from smartdirs import SmartDirs

from . import APP, ORG, PKG, URL

CMD: list[str] = [
    sys.executable,
    "-m", "smartdirs",
    "--pkg", str(PKG),
    "--app", APP,
    "--org", ORG,
    "--url", URL,
]

dirs = SmartDirs(
    pkg=PKG,
    app=APP,
    org=ORG,
    url=URL,
)

# Note: pass-through json for strip and compare strings

def test_stdout():
    A = json.loads(subprocess.check_output(CMD).decode())
    B = json.loads(dirs.model_dump_json())
    assert A == B

def test_schema():
    A = json.loads(subprocess.check_output(CMD + ["--schema"]).decode())
    B = dirs.model_json_schema(mode="serialization")
    assert A == B
