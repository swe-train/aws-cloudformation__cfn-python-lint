"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from __future__ import annotations

import fnmatch
import json
import os
import pathlib
from typing import Any, List
from unittest import TestCase

import pytest
import regex as re

import cfnlint
from cfnlint.helpers import REGIONS, load_plugins, load_resource
from cfnlint.jsonschema import RefResolver, StandardValidator, ValidationError
from cfnlint.jsonschema._utils import ensure_list
from cfnlint.schema._pointer import resolve_pointer


@pytest.mark.data
class TestSchemaFiles(TestCase):
    """Test schema files"""

    _found_keywords: List[str] = [
        "Resources/*",
        "Parameters/*",
        "Resources/*/DependsOn",
        "Resources/*/DependsOn/*",
    ]

    def setUp(self) -> None:
        schema_path = os.path.join(os.path.dirname(cfnlint.__file__), "data", "schemas")
        self.paths = {
            "extensions": os.path.join(schema_path, "extensions"),
            "providers": os.path.join(schema_path, "providers"),
            "other": os.path.join(schema_path, "other"),
            "fixtures": os.path.join(
                os.path.dirname(__file__),
                "..",
                "fixtures",
                "schemas",
                "providers",
            ),
        }
        filename = os.path.join(
            self.paths["fixtures"], "..", "json_schema", "draft7.json"
        )
        with open(filename, "r") as fh:
            d = json.load(fh)
            self.schema_draft7 = d

        super().setUp()

    def get_files(self, dir):
        for dirpath, _, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, "*.json"):
                yield dirpath, filename

    def pattern(self, validator, patrn, instance, schema):
        try:
            re.compile(patrn)
        except Exception:
            yield ValidationError(f"Pattern doesn't compile: {patrn}")

    def validate_basic_schema_details(self, d, filepath):
        """
        Validate that readOnly, writeOnly, etc are valid
        """
        sections = [
            "readOnlyProperties",
            "writeOnlyProperties",
            "conditionalCreateOnlyProperties",
            "nonPublicProperties",
            "nonPublicDefinitions",
            "createOnlyProperties",
            "deprecatedProperties",
            "primaryIdentifier",
        ]
        for section in sections:
            for prop in d.get(section, []):
                try:
                    self.assertIsNotNone(resolve_pointer(d, prop))
                except KeyError:
                    self.fail(f"Can't find prop {prop} for {section} in {filepath}")

    def _build_keywords(self, obj: Any, spec: Any, refs: list[str] | None = None):
        if refs is None:
            refs = []
        if not isinstance(obj, dict):
            yield []
            return

        if "type" in obj:
            if "object" in ensure_list(obj["type"]):
                if "properties" in obj:
                    for k, v in obj["properties"].items():
                        for item in self._build_keywords(v, spec, refs):
                            yield [k] + item
            if "array" in ensure_list(obj["type"]):
                if "items" in obj:
                    for item in self._build_keywords(obj["items"], spec, refs):
                        yield ["*"] + item

        if "$ref" in obj:
            ref = obj["$ref"]
            if ref in refs:
                yield []
                return
            for item in self._build_keywords(
                resolve_pointer(spec, ref), spec, refs + [ref]
            ):
                yield item

        yield []

    def build_keywords(self, spec):
        self._found_keywords.append(
            "/".join(["Resources", spec["typeName"], "Properties"])
        )
        for k, v in spec.get("properties").items():
            for item in self._build_keywords(v, spec):
                print(["Resources", spec["typeName"], "Properties", k] + item)
                self._found_keywords.append(
                    "/".join(["Resources", spec["typeName"], "Properties", k] + item)
                )

    def test_data_module_specs(self):
        """Test data file formats"""

        draft7_schema = load_resource(
            "cfnlint.data.schemas.other.draft7", "schema.json"
        )
        store = {"http://json-schema.org/draft-07/schema": draft7_schema}
        dir = self.paths["fixtures"]
        for dirpath, filename in self.get_files(dir):
            with open(os.path.join(dirpath, filename), "r", encoding="utf8") as fh:
                store[filename] = json.load(fh)

        resolver = RefResolver.from_schema(
            store["provider.definition.schema.v1.json"], store=store
        )

        validator = (
            StandardValidator({})
            .extend(
                validators={
                    "cfnLint": self.cfn_lint,
                    "pattern": self.pattern,
                },
            )(schema=store["provider.definition.schema.v1.json"])
            .evolve(resolver=resolver)
        )

        for region in REGIONS:
            dir = os.path.join(
                self.paths["providers"],
                region.replace("-", "_"),
            )

            for dirpath, filename in self.get_files(dir):
                with open(os.path.join(dirpath, filename), "r", encoding="utf8") as fh:
                    d = json.load(fh)
                    # not allowed but true with this resource
                    if filename == "aws-cloudformation-customresource.json":
                        d["additionalProperties"] = False
                    errs = list(validator.iter_errors(d))
                    self.assertListEqual(
                        errs, [], f"Error with {dirpath}/{filename}: {errs}"
                    )
                    self.validate_basic_schema_details(d, f"{dirpath}/{filename}")
                    self.build_keywords(d)

    def cfn_lint(self, validator, _, keywords, schema):
        keywords = ensure_list(keywords)
        self._found_keywords.extend(keywords)

    def test_other_specs(self):
        """Test data file formats"""

        draft7_schema = load_resource(
            "cfnlint.data.schemas.other.draft7", "schema.json"
        )
        store = {"http://json-schema.org/draft-07/schema": draft7_schema}
        dir = self.paths["fixtures"]
        for dirpath, filename in self.get_files(dir):
            with open(os.path.join(dirpath, filename), "r", encoding="utf8") as fh:
                store[filename] = json.load(fh)

        resolver = RefResolver.from_schema(
            store["http://json-schema.org/draft-07/schema"], store=store
        )

        validator = (
            StandardValidator({})
            .extend(
                validators={
                    "cfnLint": self.cfn_lint,
                    "pattern": self.pattern,
                },
            )(schema=store["http://json-schema.org/draft-07/schema"])
            .evolve(resolver=resolver)
        )

        for dir_name in ["extensions", "other"]:
            dir = self.paths[dir_name]

            for dirpath, filename in self.get_files(dir):
                with open(os.path.join(dirpath, filename), "r", encoding="utf8") as fh:
                    d = json.load(fh)
                    errs = list(validator.iter_errors(d))
                    self.assertListEqual(
                        errs, [], f"Error with {dirpath}/{filename}: {errs}"
                    )
                    self.validate_basic_schema_details(d, f"{dirpath}/{filename}")

    def test_x_keywords(self):
        root_dir = pathlib.Path(__file__).parent.parent.parent / "src/cfnlint/rules"
        rules = load_plugins(
            str(root_dir),
            "CfnLintKeyword",
            "cfnlint.rules.jsonschema.CfnLintKeyword",
        )
        rules.extend(
            load_plugins(
                str(root_dir),
                "CfnLintJsonSchema",
                "cfnlint.rules.jsonschema.CfnLintJsonSchema",
            )
        )

        for rule in rules:
            for keyword in rule.keywords:
                self.assertIn(keyword, self._found_keywords, f"{keyword} not found")
