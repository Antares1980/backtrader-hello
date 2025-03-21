import backtrader as bt

class HelloWorldStrategy(bt.Strategy):
    def __init__(self):
        super().__init__()
    
    def next(self):
        print("Hello World from Backtrader Strategy. Close Price: {}".format(self.data.close[0]))