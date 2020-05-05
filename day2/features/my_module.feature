Feature:
    As a user,
    I want to check out spring value
    So that my program is work correctly.

    Acceptance Criteria:
    - string value is composed only numeric character.
    - string value's length is 4 or 6.
    - string length is greater than 1 and smaller than 8.
    - If string value is match upper condition, print True.
    - If string value is not match upper condition, print False.

    Background:
        Given a terminal to run the application

    Scenario Outline:
        Given input value <string-value>
         When I input the value to my program
         Then the program print <return-value> the <string-value> is correct or not.
        
        Examples:
            | string-value | return-value |
            | ------------ | ------------ |
            | 123a         | False        |
            | 1234         | True         |
            | null         | False        |
            | ""           | False        |
            | -1           | False        |
            | 0000         | True         |

