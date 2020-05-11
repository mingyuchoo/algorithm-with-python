@solution @day15
Feature: Minimal sum of two lists.

  Acceptance Criteria:

  Background:
    Given a terminal app to run.

  Scenario Outline:
    Given two lists <data1> and <data2>
    When run with them
    Then return <minimal-sum>
    Examples:
      | data1   | data2   | minimal-sum |
      | [1,4,2] | [5,4,4] | 29          |
      | [1,2]   | [3,4]   | 10          |
