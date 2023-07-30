Feature: Enter stock
  As a user
  I want to be able to enter the stock
  So that I can change my stock

Scenario: Successful 
  Given I am on the home page
  When I click on the goods page
  And I click the stock goods button
  And I enter the name of product
  And I enter the number of product
  And I click on save button
  Then a notfication pops up that the data is saved