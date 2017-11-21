@profile
Feature: user can see and edit user profile
  @profile_see
  Scenario: see profile
    Given a user is logged in
    Then confirm english is the main language
    When user clicks the menu button
    Then user can see the menu list
    When user clicks image profile button
    Then user can see profile information
    When user clicks QR code button
    Then user can see QR code
    Then user clicks QR code cancel button
    Then user clicks profile save button
    Then user backs to homepage


    @profile_edit
    Scenario:
      Given a user is logged in
      Then confirm english is the main language
      When user clicks the menu button
      Then user can see the menu list
      When user clicks image profile button
      Then user can see profile information
      Then user can edit first name
      Then user can edit last name
      Then user clicks profile save button
      Then user can save the change
      Then user backs to homepage