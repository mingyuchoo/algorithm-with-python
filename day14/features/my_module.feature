@solution @day14
Feature: Find the biggest number.
  As a student,
  I want to find a biggest number from a special condition,
  So that I solve the problem.

  Acceptance Criteria:
  - the length of numbers in string form is greater than or equal to 1.
  - the length of numbers is smaller than or eqaul to 1000000.
  - the length of numbers is greater than or eqaul to 1.
  - the number of digits to remove is smaller than 1000000.

  Background:
    Given a two parameters to the application.

  Scenario Outline:
    Given <number> as target and <count> as digits to remove
    When run with them
    Then return valid <biggest-number>
    Examples:
      | number     | count | biggest-number |
      | 1924       | 2     | 94             |
      | 1231234    | 3     | 3234           |
      | 4177252841 | 4     | 775841         |

