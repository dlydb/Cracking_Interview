class NodeWithMin(object):
    def __init__(self, data = None, next = None, min_val = None):
        self.data = data
        self.next = next
        if self.next != None:
            if data < self.next.min_val:
                self.min_val = data
            else:
                self.min_val = self.next.get_min()
        else:
            self.min_val = data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
        if self.next != None:
            if self.data < new_next.get_min():
                self.min_val = self.data
            else:
                self.min_val = new_next.get_min()
        else:
            self.min_val = self.data

    def get_min(self):
        return self.min_val
