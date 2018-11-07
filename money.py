# I struggled through this assignment and will certainly need further help comprehending
# the basic logic wrapped around these concepts.


class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """

        return(self.code) or (self.symbol)

# Stuck on this one...

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name
                and self.code == other.code and self.symbol == other.symbol
                and self.digits == other.digits)
# Type and __eq__ are thowing me off here...


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        self.amount = amount
        self.currency = currency

    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """

        return f"{self.amount: .2f}

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and
                self.name == other.name and
                self.code == other.code and
                self.symbol == other.symbol and
                self.digits == other.digits)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)

        raise(DifferentCurrencyError)

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """

        return Money(self.amount * multiplier, self.currency)

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        return Money(self.amount / divisor, self.currency)
