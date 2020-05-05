@solution @day11
Feature: Get results of multiple ranges of a list.
  As a student,
  I want get result of multiple range of a list
  So that I pass exam.

  Acceptance Criteria:
  - give a list to search given range.
  - ranges is consisted of a list of lists.
  - a range list sis consisted of three elements [start point, end point, search point]
  - if a range list is given, the list is have to sorted to be searched.
  -
  Background:
    Given I have a terminal app to run this application.

  Scenario Outline:
    Given two parameter of <target-list> and <range-list>
     When I run app with these parameters
     Then the app return <result-list>

    Examples:
      | target-list          | range-list  | result-list |
      | [1, 5, 2, 6, 3, 7 4] | [[2, 5, 3]] | [5]         |
