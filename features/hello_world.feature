Feature: Hello World Backtrader Strategy
  As a trader
  I want to implement a simple Hello World strategy
  So that I can verify my BDD setup works with backtrader

  Scenario: Running Hello World strategy
    Given I have historical price data
    When I run the Hello World strategy
    Then I should see a "Hello World" message in the output
