@solution @day7
Feature: Mix Upper & Lower Case characters
  As a student who need to get high level,
  I want to mix characters in a sentence with upper and lower characters
  So that I fulfill the requirement.

  Acceptance Criteria:
  - a sentence is composed with some words separated by a blank.
  - change characters of even index as upper cases.
  - change characters of odd index as lower cases.
  - if index is 0, it is even index.

  Background:
    Given a console to run the application.

  Scenario Outline: examples
    Given a parameter as <sentence>
     When run with <sentence>
     Then return <manipulated-sentence>

    Examples:
      | sentence        | manipulated-sentence   |
      | a ab abc abcd   | A Ab AbC AbCd          |
      | try hello world | TrY HeLlO WoRlD        |