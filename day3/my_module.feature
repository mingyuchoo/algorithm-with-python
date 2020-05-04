@solution @day3
Feature: Sum of divisor
  As a user to solve a problem,
  I want sum of divisor of a special number N
  So that I solve my problem.

  Acceptance Criteria:
  - the special number is greater than or equal to 0.
  - the special number is smaller than or equal to 3000.

  Background:
    Given I have a terminal app to run.

  Scenario: Example of 12
    Given 12
     When run with 12
     Then it return 28.

  Scenario: Example of 5
    Given 5
     When run with 5
     Then it return 6

  Scenario Outline:
    Given <a-number>
      When run with <a-number>
      Then it return <sum>

      Examples:
        | a-number | sum |
        | 12       | 28  |
        | 5        | 6   |
