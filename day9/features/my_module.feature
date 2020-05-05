@solution @day9
Feature: Get a number of square root
  As a student
  I want a square root of a number
  So that I solve my problem.

  Acceptance Criteria:
  - just give n to application.
  - n is between 1 and 50000000000000.
  - if n is a square value of a number x, app return (x+1)^2
  - if n is not a square value of a number x, app return -1

  Background:
    Given I have a terminal app to run.

  Scenario Outline:
    Given a parameter <n>
     When I run with <n>
     Then the app return <answer>
    Examples:
      | n   | answer |
      | 121 | 144    |
      | 3   | -1     |


