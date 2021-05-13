Feature: Greeting

  Scenario: There isn't a name.
    Given no name
    When call greeting
    Then it should print nothing


  Scenario Outline: There is a name.
    Given a <name>
    When call greeting
    Then it should print <response>

    Examples: Name list
      | name   | response      |
      | Mingyu | Hello, Mingyu |
      | Tom    | Hello, Tom    |

