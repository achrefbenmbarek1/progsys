import sys
import os
from .Dto import Dto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proto.transactionHistory.transactionHistory_pb2 import EntireTransactionHistory, ElementOfTransactionHistory

class TransactionHistoryDto(Dto):
    def __init__(self, transaction_history):
        self.transaction_history = transaction_history

    def serialize(self) -> bytes:
        entire_transaction_history = EntireTransactionHistory()
        for row in self.transaction_history:
            element_of_transaction_history = entire_transaction_history.transactionHistory.add()
            element_of_transaction_history.referanceVol = row[0]
            element_of_transaction_history.referenceAgence = row[1]
            element_of_transaction_history.transaction = row[2]
            element_of_transaction_history.valeur = int(row[3])
            element_of_transaction_history.resultat = row[4]
        return entire_transaction_history.SerializeToString()

    @staticmethod
    def deserialize(data: bytes) -> 'TransactionHistoryDto':
        entire_transaction_history = EntireTransactionHistory()
        entire_transaction_history.ParseFromString(data)
        transaction_history = []
        for element in entire_transaction_history.transactionHistory:
            row = (element.referanceVol, element.referenceAgence, element.transaction, str(element.valeur), element.resultat)
            transaction_history.append(row)
        return TransactionHistoryDto(transaction_history)

    def showData(self):
        for row in self.transaction_history:
            print(row)
