from Currency import *

class CurrencyConverter:
    def __init__(self):
        self.dictionary_of_currency_type = {"USD" : 1, "EUR" : .88, "YIN" : 111.29}
        pass

    def convert(self, currency_object, converted_code):
        if currency_object.currency_code == converted_code:
