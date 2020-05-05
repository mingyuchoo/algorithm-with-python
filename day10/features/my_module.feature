@solution @day10
Feature: Get average value
  As a student,
  I want to get a average of a list
  So that I pass the exam.

  Acceptance Criteria:
  - list length is between 1 and 100.
  - the list consisted of integers.
  - the integer is between -10000 and 10000.

  Background:
    Given I have a terminal app to run this application.

  Scenario Outline:
    Given a parameter <list>
     When I run with <list>
     Then my application return <average>
    Examples:
      | list         | average |
      | [1, 2, 3, 4] | 2.5     |
      | [5, 5]       | 5       |

