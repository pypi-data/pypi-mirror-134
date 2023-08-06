"""
A light jinja-like tool for basic templating.

Parses a text file with fields to be filled in the format '{{ key }}', to fill them with a key-value
pair described as a Yaml file.

Example template:
```
Hi, my name is {{ name }} and I am {{ age }} years old.
```

Example key-value pairs:
``` yaml
name: foo
age: 100
```

Usage:
>>> templater template.txt key-values.yaml

This will print a text such as:

Hi, my name is foo and I am 100 years old.

For a more advanced use, also the .yaml file with the mapping can be templated with the same syntax.
Then, before using the .yaml values to fill the final template, key-value pairs can be passed
dynamically to pre-fill the values .yaml file, and then the generated yaml file will be used as
usual to fill the template.

Example:
We want to automate the deployments of a certain version of our software on a certain environment,
in the same way for a lot of customers. Instead of having a value mapping which is exactly the same
for every customer, we can pass dynamically the customer name to generate the template.

Template:
```
Hi, my name is {{ name }} and I am using the {{ version }} version of optimal bid.
I want to automate the deployments for the {{ env }} environment.
```

Dynamic key-value pairs:
``` yaml
name: {{ customer_name }}
version: v0.5.0
env: production
```

Usage:
>>> templater template.txt key-values.yaml customer_name=axpo

So it's easier to automate the generation of the same template for a lot of customers, just with a
for loop.
"""
import re
from argparse import ArgumentParser, Namespace
from collections import Counter
from io import StringIO
from typing import Dict, List, Tuple, Union

import yaml

Value = Union[str, List[str]]
ValuesMap = Dict[str, Value]

TOKEN_PATTERN = r"{{[a-zA-Z0-9\._ ]*}}"  # nosec


def get_argument_parser() -> ArgumentParser:
    argument_parser = ArgumentParser(
        description="A light jinja-like tool for basic templating.",
        usage="templater template.txt key-values.yaml",
    )
    argument_parser.add_argument("template", help="The path of the template text file.")
    argument_parser.add_argument(
        "values", help="The path of the .yaml file with the values to fill."
    )
    argument_parser.add_argument(
        "extra_mappings",
        help="Command line mappings like <key>=<value>, to fill a templated" " values yaml file.",
        nargs="*",
    )
    return argument_parser


def get_arguments() -> Namespace:
    argument_parser = get_argument_parser()
    arguments = argument_parser.parse_args()
    return arguments


def extract_key_from_token(token: str) -> str:
    if re.match(TOKEN_PATTERN, token):
        return token.replace("}", "").replace("{", "").strip()
    raise ValueError(f"{token} does not match the pattern for tokens, {TOKEN_PATTERN}.")


def write_list_to_string_double_quotes(value: List[str]) -> str:
    comma_separated_values = ", ".join([f'"{val}"' for val in value])
    return f"[{comma_separated_values}]"


def parse_extra_mapping(key_value: str) -> Tuple[str, str]:
    """Crash if an extra mapping is not in the format <key>=<value>"""
    character_counts = Counter(key_value)
    if character_counts["="] != 1:
        raise ValueError("Extra mapping arguments should be in the format <key>=<value>")
    key, value = tuple(key_value.split("="))
    return key, value


def parse_extra_mappings(extra_mappings: List[str]) -> ValuesMap:
    parsed_couples = list(map(parse_extra_mapping, extra_mappings))
    return {key: value for key, value in parsed_couples}


def fill_values(template: str, values: ValuesMap) -> str:
    raw_tokens = re.findall(TOKEN_PATTERN, template)
    for raw_tok in raw_tokens:
        key = extract_key_from_token(raw_tok)
        if key in values:
            value = values[key]
            if isinstance(value, list):
                value = write_list_to_string_double_quotes(value)
            template = template.replace(raw_tok, value)
        else:
            raise KeyError(f"The values YAML does not contain {key}.")
    return template


def main():
    args = get_arguments()
    dynamic_value_map = parse_extra_mappings(args.extra_mappings)
    if dynamic_value_map:
        with open(args.values) as raw_yam:
            raw_content = raw_yam.read()
            filled_yaml_content = fill_values(raw_content, dynamic_value_map)
        values = yaml.safe_load(StringIO(filled_yaml_content))
    else:
        with open(args.values) as yaml_file:
            values = yaml.safe_load(yaml_file)
    with open(args.template) as file_handle:
        template = file_handle.read()
    print(fill_values(template, values))
