@solution @day4
Feature: Anagram
  As a student to solve a problem,
  I want to check that two of words are anagram each other
  So that I solve my problem.

  Acceptance Criteria:
  - each word's length is smaller than and equal to 100,000.
  - a word A and a word B is anagram is True
  - a word A and a woard B is not anagram is False
  - words are only alphabet.
  - words composed with alphabet as upper ro lower cases.
  - whether two of word is anagram or not, don't care about upper or lower cases.

  Background:
    Given I have a terminal app to run.

  Scenario: Example of "listen"
    Given a word "listen"
     When run with "listen"
     Then the word can be "silent"

  Scenario Outline:
    Given <input-a>
     When run with <input-b>
     Then it return <output>

    Examples:
      | input-a | input-b | output |
      | listen  | silent  | true   |