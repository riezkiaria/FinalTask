Feature: Login to website
  As a user
  I want to be able to login to the website
  So that I can access my account

Scenario: Successful login
  Given I am on the login page
  When I enter valid login credentials
  And I click the login button
  Then I should be redirected to homepage

Scenario: Invalid login
  Given I am on the jubelio login page
  When I enter my email and leave the password field empty
  And I click the masuk button
  Then an error should appear telling me that password must be filled