Feature: Download Historical Data for Multiple Tickers
  As a trader
  I want to download historical price data for a set of tickers
  So that I can store and analyze the data offline

  Scenario: Download data for multiple tickers within a given date range
    Given I have a set of tickers "AAPL,MSFT,GOOGL"
    And the start date is "20220101"
    And the end date is "20220131"
    When I download the historical data for these tickers
    Then I should have files named "AAPL-20220101-20220131.csv, MSFT-20220101-20220131.csv, GOOGL-20220101-20220131.csv" in the "data" folder
