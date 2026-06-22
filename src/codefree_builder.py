import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Condition:
    field: str
    operator: str
    value: str

@dataclass
class Action:
    type: str
    target: str
    value: str = None

@dataclass
class Rule:
    condition: Condition
    action: Action

class LogicEditor:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def evaluate(self, data: Dict[str, str]) -> List[Action]:
        triggered_actions = []
        for rule in self.rules:
            if self.evaluate_condition(rule.condition, data):
                triggered_actions.append(rule.action)
        return triggered_actions

    def evaluate_condition(self, condition: Condition, data: Dict[str, str]) -> bool:
        field_value = data.get(condition.field)
        if condition.operator == 'equals':
            return field_value == condition.value
        elif condition.operator == 'not_equals':
            return field_value != condition.value
        else:
            raise ValueError(f"Unsupported operator: {condition.operator}")

    def get_supported_actions(self) -> List[str]:
        return ['show', 'hide', 'navigate', 'submit', 'set_variable', 'call_api']

    def get_supported_operators(self) -> List[str]:
        return ['equals', 'not_equals']
