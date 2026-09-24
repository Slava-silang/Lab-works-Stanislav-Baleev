# Console Utility Toolkit

## About the project

This project was created as part of Laboratory Work 1.

It is a set of command-line utilities written in Python. The project contains two main tools:

* a calculator for arithmetic expressions;
* a unit converter.

The project also includes some features: calculation history, loading units from a configuration file, automated tests, Ruff code checking, and pre-commit.

## Requirements

To run the project, you need:

* Python 3.10 or higher;
* Git;
* uv for managing the project environment and dependencies.

## Installation

First, download the project and open its directory:

```PowerShell
git clone <repository-url>
cd LabPython1
```

Then install the dependencies and create the project environment:

```PowerShell
uv sync
```

The project can also be installed in editable mode:

```PowerShell
python -m pip install -e .
```

### Calculator

The calculator is started with the following command:

```PowerShell
python -m toolkit calc "2 + 3"
```

Result:

```text
5.0
```

The calculator supports:

* addition `+`;
* subtraction `-`;
* multiplication `*`;
* division `/`;
* integer division `//`;
* remainder `%`;
* positive and negative numbers;
* floating-point numbers;
* parentheses;
* operator precedence;
* spaces inside expressions.

For example:

```PowerShell
python -m toolkit calc "10 + 5 * 2"
```

Result:

```text
20.0
```

Branches can also be used:

```PowerShell
python -m toolkit calc "(10 + 5) * 2"
```

Result:

```text
30.0
```

### Unit converter

The converter is started with:

```PowerShell
python -m toolkit convert 10 --from cm --to mm
```

Result:

```text
100.0
```

The following units are supported.

#### Length

* `mm` - millimeters;
* `cm` - centimeters;
* `dm` - decimeters;
* `m` - meters;
* `km` - kilometers.

#### Mass

* `g` - grams;
* `kg` - kilograms.

#### Temperature

* `c` - Celsius;
* `f` - Fahrenheit;
* `k` - Kelvin.

For example:

```PowerShell
python -m toolkit convert 10 --from km --to m
```

Result:

```text
10000.0
```

Temperature conversion:

```PowerShell
python -m toolkit convert 0 --from c --to f
```

Result:

```text
32.0
```

Units are case-insensitive.

## Calculation history

Successful calculations are saved to:

```text
history.json
```

This file automaticly creats, when user makes first calculating.

The history is stored in JSON format. Each entry contains the expression and its result.

Example:

```json
[
    {
        "expression": "2 + 3",
        "result": 5
    }
]
```

Failed operations are not added to the history.

## Unit configuration

The units used by the converter are stored in:

```text
config/units.json
```

This makes it possible to keep the conversion table outside the main converter code.

## Error handling

The program handles incorrect user input.

For example:

* empty expressions;
* invalid symbols;
* missing operands;
* two operators in a row;
* division by zero;
* unknown units;
* incompatible units;
* temperatures below absolute zero.

When an error occurs, the program prints an error message to `stderr` and exits with code `2`.

## Help

To see information about the available commands, run:

```PowerShell
python -m toolkit --help
```

## Testing

The project uses `pytest` for automated testing.

To run all tests:

```PowerShell
python -m pytest
```

You can also use:

```PowerShell
uv run pytest
```

The tests check both the calculator and converter, including incorrect input and error handling.

There are currently 29 tests in the project.

## Code checking

Ruff is used to check the Python code:

```PowerShell
uv run ruff check .
```

## Pre-commit

Pre-commit is configured to automatically check the project before creating a Git commit.

To run all checks:

```PowerShell
pre-commit run --all-files
```

The project uses:

* Ruff for code checking;
* Ruff Format for formatting;
* pytest for running tests.

## Project structure

The main project files are organized as follows:

```text
LabPython1/
├── config/
│   └── units.json
├── src/
│   └── toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── calculator.py
│       ├── converter.py
│       ├── errors.py
│       ├── history.py
│       ├── processes.py
│       ├── check.py
│       └── make_number.py
├── tests/
│   ├── test_CLI.py
│   ├── test_calculator.py
│   └── test_converter.py
├── history.json
├── pyproject.toml
├── uv.lock
├── .pre-commit-config.yaml
└── README.md
```

## What was done in this laboratory work

During this laboratory work, I created a command-line calculator and a unit converter in Python.

The calculator supports different arithmetic operations, operator precedence, negative numbers, and branches. The calculation is performed without using `eval()` or other ready-made expression evaluation tools.

For the converter, I created a separate configuration file containing the supported units and their conversion values. I also added a JSON file for storing successful calculations.

After implementing the main functionality, I wrote automated tests, including tests for incorrect input and errors. Finally, I configured Ruff and pre-commit to automatically check the project.

The project uses uv to manage the environment and dependencies, while `uv.lock` stores the exact versions of the project dependencies.
