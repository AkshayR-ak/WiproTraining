Feature: Employee Creation

  Scenario Outline: Add Employee
    Given the user is logged into OrangeHRM
    When I enter "<FirstName>" and "<LastName>"
    Then employee should be created successfully

    Examples:
  | FirstName | LastName |
  | Akshay    | Kumar    |