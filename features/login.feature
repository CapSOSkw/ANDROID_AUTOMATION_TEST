@login
Feature: Login 

Scenario: User can login
	Given the user is logging
	When user enters username
	And user enters password
	And user clicks the login button
	Then user should see the map
