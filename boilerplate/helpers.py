import os
from pathlib import Path
from typing import Iterable

import yaml


def find_jinja_template(path: str):
    candidates = []
    for file in os.listdir(path):
        if file.endswith(".j2") or file.endswith(".jinja2"):
            candidates.append(file)
    if len(candidates) == 1:
        return Path(path) / candidates[0]
    if len(candidates) > 1:
        raise ValueError(f"Multiple templates found in {path}, \n {candidates}")
    raise FileNotFoundError(f"No template found in {path}")


def find_yaml_file(path: str):
    candidates = []
    for file in os.listdir(path):
        if file.endswith(".yml") or file.endswith(".yaml"):
            candidates.append(file)
    if len(candidates) == 1:
        return Path(path) / candidates[0]
    if len(candidates) > 1:
        raise ValueError(f"Multiple values found in {path}, \n {candidates}")
    raise FileNotFoundError(f"No values found in {path}")


def read_values_from_yaml(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def prompt_user(vals: Iterable[str]) -> dict[str]:
    return_val = {}
    for val in vals:
        value = input(f"Enter value for {val}: ")
        return_val[val] = value
    return return_val
