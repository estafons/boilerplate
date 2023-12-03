import filecmp
import os
from pathlib import Path

from click.testing import CliRunner

from boilerplate.boilerplate import create


def test_create():
    input_folder = Path(os.path.abspath(__file__)).parent.parent / "data/template1/"
    output_file = Path("/tmp/output.txt")
    expected_output_file = input_folder / "expected_out.txt"
    runner = CliRunner()
    result = runner.invoke(
        create, ["--template-path", input_folder, "--output", output_file]
    )
    assert result.exit_code == 0
    assert filecmp.cmp(output_file, expected_output_file, shallow=False)
