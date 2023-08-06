from oc4idskit.cli.__main__ import main
from tests import assert_streaming


def test_command(capsys, monkeypatch):
    assert_streaming(
        capsys,
        monkeypatch,
        main,
        ["combine-project-packages"],
        ["project_package_split.json"],
        ["project_package_combined.json"],
    )
