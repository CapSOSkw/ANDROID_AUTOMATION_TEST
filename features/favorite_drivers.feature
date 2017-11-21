@favorite_drivers
Feature: user can see information of favorite drivers
  @favorite_drivers_see
  Scenario: user can see drivers
    Given a user is logged in
    Then confirm english is the main language
    When user clicks the menu button
    Then user can see the menu list
    Then user clicks favorite drivers menu button
    Then user can see favorite drivers information
    Then user backs to homepage

    @favorite_drivers_add
    Scenario: add a new favorite driver
      Given a user is logged in
      Then confirm english is the main language
      When user clicks the menu button
      Then user can see the menu list
      Then user clicks favorite drivers menu button
      Then user can see favorite drivers information
      Then user clicks add a new favorite driver button
      Then user enters driver username
      Then user clicks the 1st dropdown adding request button
      Then a favorite adding request is sending
      Then user backs to homepage

      @favorite_drivers_delete
        #Default is cancel delete
      Scenario: delete a favorite driver
        Given a user is logged in
        Then confirm english is the main language
        When user clicks the menu button
        Then user can see the menu list
        Then user clicks favorite drivers menu button
        Then user can see favorite drivers information
        Then user clicks delete a favorite driver button
        Then user clicks cancel or remove button
        Then a favorite driver is deleted
        Then user backs to homepage

#        @favorite_drivers_request
#        #Scenario: request from a favorite driver
#          Given a user is logged in
#          Then confirm english is the main language
#          When user clicks the menu button
#          Then user can see the menu list
#          Then user clicks favorite drivers menu button
#          Then user can see favorite drivers information
#          Then user clicks the request button from the 1st driver
#          Then user enters pickup location in the request page
#          Then user enters destination location in the request page
#          Then user can cancel or send request
#          Then user backs to homepage