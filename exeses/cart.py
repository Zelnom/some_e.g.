class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def calculate_total(self):
        sume = 0
        for item in self.items:
            sume += item["quantity"] * item["price"]   # sau  .get
        return sume

