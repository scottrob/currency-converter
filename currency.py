
class Currency:
    def __init__(self, amount, currency_code):
         self.amount = amount
         self.currency_code = currency_code
    def __str__(self):
        return str((self.amount) + ' ' + self.currency_code)
    def __add__(self, other):
        return self.value + other.value
    def __sub__(self, other):
        return self.value other.value
    def __eq__(sefl, value):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
