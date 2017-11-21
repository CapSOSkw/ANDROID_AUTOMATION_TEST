@setting
Feature: user can check and change settings
  @setting_see
  Scenario: user can see setting options
    Given a user is logged in
    Then confirm english is the main language
    When user clicks the menu button
    Then user can see the menu list
    Then user clicks settings button menu
    Then user can see setting options
    Then user backs to homepage

    @setting_out
    Scenario: sign out
      Given a user is logged in
      Then confirm english is the main language
      When user clicks the menu button
      Then user can see the menu list
      Then user clicks settings button menu
      Then user can see setting options
      Then user clicks sign out button
      Then user can cancel or sign out
      Then user backs to homepage

      @setting_profile_see
      Scenario: edit profile see
        Given a user is logged in
        Then confirm english is the main language
        When user clicks the menu button
        Then user can see the menu list
        Then user clicks settings button menu
        Then user can see setting options
        Then user clicks edit profile button
        Then user can see profile information
        When user clicks QR code button
        Then user can see QR code
        Then user clicks QR code cancel button
        Then user clicks profile save button
        Then user backs to homepage

        @setting_profile_edit
        Scenario: edit profile edit
          Given a user is logged in
          Then confirm english is the main language
          When user clicks the menu button
          Then user can see the menu list
          Then user clicks settings button menu
          Then user can see setting options
          Then user clicks edit profile button
          Then user can see profile information
          Then user can edit first name
          Then user can edit last name
          Then user clicks profile save button
          Then user can save the change
          Then user backs to homepage

          @setting_preference
          Scenario: driver preference
            Given a user is logged in
            Then confirm english is the main language
            When user clicks the menu button
            Then user can see the menu list
            Then user clicks settings button menu
            Then user can see setting options
            Then user clicks the driver preference button
            Then user can see the preference options
            Then user can choose different preferences
            Then user can save the preference changes
            Then user backs to homepage


          @setting_language
          Scenario: language
            Given a user is logged in
            Then confirm english is the main language
            When user clicks the menu button
            Then user can see the menu list
            Then user clicks settings button menu
            Then user can see setting options
            Then user clicks the language button
            Then user can choose english or chinese
            Then the language is changed
            Then user backs to homepage