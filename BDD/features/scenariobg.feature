Feature: OrangeHRM Login

  Background: common steps
    Given launch my chrome browser
    When I open orange hrm homepage
    And Enter valid username and password
    And click on login button

  Scenario: Login into HRM with valid parameters
    Then user login into to dashboard page

  Scenario: Advanced search user
    Given launch my chrome browser
    When I open orange hrm homepage
    And Enter valid username and password
    And click on Login
    When navigate to advanced search page
    Then advanced search page should display