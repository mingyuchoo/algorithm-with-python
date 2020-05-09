@solution @day12
Feature:
  Aa a John,
  So that I get treasure from Smith's treasure map
  I want to solve treasure map.

  Acceptance Criteria:
  - A side length is n.
  - n is greater than or equal to 1.
  - n is smaller than or equal to 16.
  - the two map are integer array list that is n length.
  - the item of each map; x should convert to binary. the length of the result of it smaller than or equal to n.
    (x between 0 and (2^n)-1)

  Background:
    Given three parameters is not empty

  Scenario Outline:
    Given <n>, <data1>, <data2>
     When run with <n>, <data1>, <data2>
     Then return <solved-map>
    Examples:
      | n | data1                    | data2                    | solved-map                                                   |
      | 5 | [9, 20, 28, 18, 11]      | [30, 1, 21, 17, 28 ]     | ["#####", "# # #", "### #", "#  ##", "#####"]                |
      | 6 | [46, 33, 33, 22, 31, 50] | [27, 56, 19, 14, 14, 10] | ["######", "###  #", "##  ##", " #### ", " #####", "### # "] |

