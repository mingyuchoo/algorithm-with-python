@slow @wip @needs_database
Feature: Say hello to someone
    As a user who need to greeting someone
    I want to say "Hello, somebody's name"
    So that I make good relationship with.

    Acceptance Criteria:
        - I want to just use a name if I give.
        - I can give no name.

    Scenario Outline: Normal case
        Given a parameter as <name>
         When run with <name>
         Then return Hello, <name>

        Examples:
        | name     |
        | Mingyu   |
        | ""       |
        | null     |
