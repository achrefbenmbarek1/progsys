from .VolRepository import VolRepository
from .FactureRepository import FactureRepository
from .TransactionHistoryRepository import TransactionHistoryRepository
class RepositoryFactory:
    def __init__(self, dataType ):
        self.dataType = dataType
    
    def createRepository(self):
        if self.dataType == 'vol':
            return VolRepository("vols.txt")
        elif self.dataType == 'facture':
            return FactureRepository("facture.txt")
        elif self.dataType == 'transactionHistory':
            return TransactionHistoryRepository("history.txt")
