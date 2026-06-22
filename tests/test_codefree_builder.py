import pytest
from codefree_builder import LogicEditor, Rule, Condition, Action

def test_add_rule():
    editor = LogicEditor()
    rule = Rule(Condition('field1', 'equals', 'value1'), Action('show', 'target1'))
    editor.add_rule(rule)
    assert len(editor.rules) == 1

def test_evaluate_rule():
    editor = LogicEditor()
    rule = Rule(Condition('field1', 'equals', 'value1'), Action('show', 'target1'))
    editor.add_rule(rule)
    data = {'field1': 'value1'}
    triggered_actions = editor.evaluate(data)
    assert len(triggered_actions) == 1
    assert triggered_actions[0].type == 'show'

def test_evaluate_condition_equals():
    editor = LogicEditor()
    condition = Condition('field1', 'equals', 'value1')
    data = {'field1': 'value1'}
    assert editor.evaluate_condition(condition, data)

def test_evaluate_condition_not_equals():
    editor = LogicEditor()
    condition = Condition('field1', 'not_equals', 'value1')
    data = {'field1': 'value2'}
    assert editor.evaluate_condition(condition, data)

def test_get_supported_actions():
    editor = LogicEditor()
    supported_actions = editor.get_supported_actions()
    assert len(supported_actions) == 6
    assert 'show' in supported_actions
    assert 'hide' in supported_actions
    assert 'navigate' in supported_actions
    assert 'submit' in supported_actions
    assert 'set_variable' in supported_actions
    assert 'call_api' in supported_actions

def test_get_supported_operators():
    editor = LogicEditor()
    supported_operators = editor.get_supported_operators()
    assert len(supported_operators) == 2
    assert 'equals' in supported_operators
    assert 'not_equals' in supported_operators

def test_evaluate_condition_unsupported_operator():
    editor = LogicEditor()
    condition = Condition('field1', 'unsupported', 'value1')
    data = {'field1': 'value1'}
    with pytest.raises(ValueError):
        editor.evaluate_condition(condition, data)
