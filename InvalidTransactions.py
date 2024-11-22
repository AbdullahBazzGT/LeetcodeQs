class Transaction:
    def __init__(self, input):
        split = input.split(",")
        self.name = split[0]
        self.time = int(split[1])
        self.amount = int(split[2])
        self.city = split[3]

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        invalids = []  # Stores invalid transactions
        transaction_map = {}  # Maps name to a list of transactions

        # Populate the map with transactions
        for transaction in transactions:
            t = Transaction(transaction)
            if t.name not in transaction_map:
                transaction_map[t.name] = []
            transaction_map[t.name].append(t)

        # Check each transaction for validity
        for transaction in transactions:
            t = Transaction(transaction)
            if not self.isValid(t, transaction_map.get(t.name, [])):
                invalids.append(transaction)

        return invalids

    def isValid(self, t, indivTransactions):
        # Check if the transaction amount exceeds 1000
        if t.amount > 1000:
            return False
        
        # Check for transactions with the same name in different cities within 60 minutes
        for transaction in indivTransactions:
            if abs(t.time - transaction.time) <= 60 and t.city != transaction.city:
                return False

        return True
            