@solution @day5
Feature: Get middle characters
  As a student to solve a problem,
  I want to get middle characters
  So that I solve my problem.

  Acceptance Criteria:
  - string length is greater than or equal to 1.
  - string length is smaller than or equal to 100.
  - If length of the string is odd number, just get a middle character.
  - If length of the string is even number, get two middle characters.

  Background:
    Given I have a terminal app to run.

  Scenario: Example of "abcde"
    Given a ward "abcde"
     When run with "abcde"
     Then it returns "c".

  Scenario Outline:
    Given <word>
     When run with <word>
     Then it returns <middle>

    Examples:
      | word  | middle |
      | None  | ""     |
      | ""    | ""     |
      | a     | a      |
      | ab    | ab     |
      | abc   | b      |
      | abcd  | dc     |
      | abcde | c      |

