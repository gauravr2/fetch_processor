class MemoryStore:
    def __init__(self):
        self.data = {}

    def add(self, receipt_id, points):
        self.data[receipt_id] = points

    def get(self, receipt_id):
        return self.data.get(receipt_id)
