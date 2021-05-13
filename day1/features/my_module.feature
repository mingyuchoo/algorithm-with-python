Feature: Even or Odd

  Scenario: no input
    Given no number
    When call my_function without a number
    Then it should return Even


  Scenario Outline: Even numbers
    Given a <even> number
    When call my_function
    Then it should return <output>

    Examples: Number list
      | even | output |
      | 0      | Even   |
      | 2      | Even   |
      | 4      | Even   |
      | 6      | Even   |
      | 8      | Even   |

  Scenario Outline: Odd numbers
    Given a <odd> number
    When call my_function
    Then it should return <output>

    Examples: Number list
      | odd | output |
      | 1   | Odd    |
      | 3   | Odd    |
      | 5   | Odd    |
      | 7   | Odd    |
      | 9   | Odd    |

