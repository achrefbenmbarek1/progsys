import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.TransactionHistoryDto import TransactionHistoryDto

class TransactionHistoryRepository:
    def __init__(self, fileName ):
        self.fileName = os.path.abspath(os.path.dirname(__file__)) +"/"+ fileName
    
    def readHistory(self):
        with open(self.fileName, 'r') as f:
            lines = f.readlines()
        transactionHistory = [tuple(line.strip().split()) for line in lines]
        transactionHistoryDto = TransactionHistoryDto(transactionHistory)

        return transactionHistoryDto
