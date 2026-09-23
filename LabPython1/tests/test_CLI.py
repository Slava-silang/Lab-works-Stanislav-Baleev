import subprocess


def test_CLI_calc():
    result = subprocess.run(
        ["python", "-m", "toolkit", "calc", "2 + 3"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"


def test_CLI_division_by_zero():
    result = subprocess.run(
        ["python", "-m", "toolkit", "calc", "43 / 0"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert result.stderr


def test_CLI_convert():
    result = subprocess.run(
        ["python", "-m", "toolkit", "convert", "10", "--from", "k", "--to", "c"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == "-263.15\n"


def test_CLI_unmatched_units():
    result = subprocess.run(
        ["python", "-m", "toolkit", "convert", "22", "--from", "kg", "--to", "k"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert result.stderr
