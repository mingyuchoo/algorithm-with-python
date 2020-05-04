@solution @day6
Feature: masking phone_number
  As a student to solve a problem,
  I want to mask phone number,
  So that protect personal information.

  Acceptance Criteria:
  - Input value's length is between 4 and 20.
  - Mask except the remaining 4 digits of the mobile phone.

  Background:
    Given a valid phone number and have a terminal app to run.

  Scenario: Example of "0290008282"
    Given a phone number as "0290008282"
     When run with the phone number "0290008282"
     Then it returns "******8282"

  Scenario Outline:
    Given <phone_number>
     When run with <phone_number>
     Then it returns <masked_phone_number>

    Examples:
      | phone_number | masked_phone_number |
      | 0290008282   | ******8282          |
      | 01012345678  | *******5678         |
