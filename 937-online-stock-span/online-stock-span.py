class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            old_price, old_span = self.stack.pop()
            span += old_span

        self.stack.append((price, span))

        return span