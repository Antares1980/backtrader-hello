from behave import given, when, then
import backtrader as bt
import datetime
from trading.hello_world_strategy import HelloWorldStrategy
import io
import sys
from contextlib import redirect_stdout

@given(u'I have historical price data')
def step_impl(context):
    context.cerebro = bt.Cerebro()
    context.data = bt.feeds.YahooFinanceData(dataname='data/AAPL.csv',
                                             fromdate=datetime.datetime(2011, 1, 1),
                                             todate=datetime.datetime(2012, 12, 31))
    context.cerebro.adddata(context.data)
    # Initialize output to an empty string to ensure it always exists.
    context.output = ""

@when(u'I run the Hello World strategy')
def step_impl(context):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        context.cerebro.addstrategy(HelloWorldStrategy)
        context.cerebro.run()
    context.output = buffer.getvalue()

@then(u'I should see a "Hello World" message in the output')
def step_impl(context):
    # Check if "Hello World" is in the captured output
    assert "Hello World" in context.output, (
        f"Expected 'Hello World' in output, but got:\n{context.output}"
    )