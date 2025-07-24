Feature: OrangeHRM Login
  Scenario: Login into HRM with valid parameters
    Given launch my chrome browser
    When I open orange hrm homepage
    And Enter username "admin" and password "admin123"
    And click on login button
    Then user login into to dashboard page
    And close my browser


  Scenario Outline: Login to orhangehRM with multiple params
    Given launch my chrome browser
    When I open orange hrm homepage
    And Enter username "<username>" and password "<password>"
    And click on login button
    Then user login into to dashboard page
    And close my browser

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | arun     | kumar    |