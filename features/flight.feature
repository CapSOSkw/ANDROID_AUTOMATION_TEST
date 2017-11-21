@flight
Feature: user can check flight
  @see_flight
  Scenario: user checks
    Given a user is logged in
    Then confirm english is the main language
    When user clicks the menu button
    Then user can see the menu list
    When user clicks the flight check button in menu list
    Then user can check flight
    Then user enters airline
    Then user enters airline number
    Then user opens calendar
    Then user clicks random date
    Then user clicks calendar ok button
    Then user clicks the flight check button
    Then user can see the result of flight check
    Then user backs to homepage