from behave import *
from my_module import my_function

use_step_matcher("parse")


@given('no number')
def step_impl(context):
    pass


@given('a {even:d} number')
def step_impl(context, even):
    context.input = even


@given('a {odd:d} number')
def step_impl(context, odd):
    context.input = odd


@when('call my_function without a number')
def step_impl(context):
    context.output = my_function()


@when('call my_function')
def step_impl(context):
    context.output = my_function(context.input)


@then('it should return {output}')
def step_impl(context, output):
    assert (context.output == output)
