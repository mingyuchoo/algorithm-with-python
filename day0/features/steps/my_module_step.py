from behave import *

from my_module import greeting

use_step_matcher("parse")


@given('no name')
def step_impl(context):
    context.name = ""


@when('call greeting')
def step_impl(context):
    context.response = greeting(context.name)


@then('it should print nothing')
def step_impl(context):
    assert (context.response == "")


@given('a {name}')
def step_impl(context, name):
    context.name = name


@then('it should print {response}')
def step_impl(context, response):
    assert (context.response == response)
