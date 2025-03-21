from behave import given, when, then
import backtrader as bt
import datetime

@given(u'I have a set of tickers "AAPL,MSFT,GOOGL"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a set of tickers "AAPL,MSFT,GOOGL"')


@given(u'the start date is "20220101"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the start date is "20220101"')


@given(u'the end date is "20220131"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the end date is "20220131"')


@when(u'I download the historical data for these tickers')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I download the historical data for these tickers')


@then(u'I should have files named "AAPL-20220101-20220131.csv, MSFT-20220101-20220131.csv, GOOGL-20220101-20220131.csv" in the "data" folder')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should have files named "AAPL-20220101-20220131.csv, MSFT-20220101-20220131.csv, GOOGL-20220101-20220131.csv" in the "data" folder')