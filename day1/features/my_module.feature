@userstory @feature @do_not_need_database
  Feature: Judge whether a number is even or odd.
    As a user input a number to my application
    I want to get the number is even or odd number
    So that I can use a number exactly.

    Acceptance Criteria:
      - the judge result is only even or odd.
      - no input value is even.
      - zero is even.

    Background:
      Given a terminal app to me

    Scenario Outline: Normal case
      Given a <num>
       When run this application with <num>
       Then print <output>
      Examples:
        | num  | output |
        | ---- | ------ |
        | null | Even   |
        | ""   | Even   |
        | -1   | Odd    |
        | 0    | Even   |
        | 1    | Odd    |
        | 2    | Even   |
        | 3    | Odd    |