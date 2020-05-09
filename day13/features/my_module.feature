@solution @day13
Feature:
  As a student,
  I want add two matrix
  So that I solve the problem.

  Acceptance Criteria:
  - columns and rows's count of the matrix should be smaller than 500.

  Background:
    Given two matrix to add.

  Scenario Outline:
    Given two matrix <a>, <b>,
    When run to add <a> and <b>
    Then return valid <sum>
    Examples:
      | a              | b               | c              |
      | [[1,2], [2,3]] | [[3, 4], [5,6]] | [[4,6], [7,9]] |
      | [[1], [2]]     | [[3], [4]]      | [[4], [6]]     |
