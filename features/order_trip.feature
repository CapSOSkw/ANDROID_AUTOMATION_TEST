@trip
Feature: user can see map homepage
  @trip_order
  Scenario: all map homepage elements exist
    Given a user is logged in
    Then confirm english is the main language
    When user clicks pickup location box
    Then user can enter pickup location
    Then user clicks the first pickup dropdown
    When user clicks destination location box
    Then user can enter destination location
    Then user clicks the first pickup dropdown
    Then user can see the pre-scheduled route
    Then user can order now or reserve trip
    Then user selects vehicle type
    Then user clicks request ride button
    Then user waits for driver response

    @trip_see
    Scenario: check my trips
      Given a user is logged in
      Then confirm english is the main language
      When user clicks the menu button
      Then user can see the menu list
      Then user clicks my trips menu
      Then user can see trips information
      Then user clicks the lastest trip
      Then user can see the lastest trip information
      Then user can add driver to favorite or blocking list
      Then user clicks report lost item
      Then user can report lost item
      Then user backs to homepage
