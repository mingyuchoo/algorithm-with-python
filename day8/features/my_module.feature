@solution @day8
Feature: Make a list consisted with start x step x count n
  As a student,
  I want to make a list consisted of numbers starting x step x and count n

  Acceptance Criteria:
  - x is between -10000000 and 10000000
  - n is 1000
  Background:
    Given I have a terminal app to run the application.

  Scenario Outline:
    Given parameters with <x>, <n>
     When I run with the parameters
     Then I'll get <answer>
    Examples:
      | x  | n | answer           |
      | 2  | 5 | [2, 4, 6, 8, 10] |
      | 4  | 3 | [4, 8, 12]       |
      | -4 | 2 | [ -4, -8 ]      |
