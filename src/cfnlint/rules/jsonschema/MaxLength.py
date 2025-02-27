"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from __future__ import annotations

from typing import Any, Dict

from cfnlint.jsonschema import ValidationError, Validator
from cfnlint.rules import CloudFormationLintRule


class MaxLength(CloudFormationLintRule):
    """Check maxLength values are correct"""

    def __init__(self, approaching_limit_rule: str | None = None) -> None:
        super().__init__()
        self.config["threshold"] = 0.9

        self.approaching_limit_rule = approaching_limit_rule

        self.child_rules = {}
        if approaching_limit_rule:
            self.child_rules[approaching_limit_rule] = ""

    # pylint: disable=unused-argument
    def maxLength(
        self, validator: Validator, mL: Any, instance: Any, schema: Dict[str, Any]
    ):
        if not validator.is_type(instance, "string"):
            return

        percent = len(instance) / mL
        if percent > 1:
            yield ValidationError(f"{instance!r} is longer than {mL}")
            return

        if percent > self.config["threshold"]:
            rule = self.child_rules.get(self.approaching_limit_rule)
            if not rule:
                return

            if hasattr(rule, "maxLength") and callable(getattr(rule, "maxLength")):
                validate = getattr(rule, "maxLength")
                yield from validate(validator, mL, instance, schema)
                return

            yield ValidationError(
                f"{instance!r} is approaching the max length of {mL}",
                rule=rule,
            )
