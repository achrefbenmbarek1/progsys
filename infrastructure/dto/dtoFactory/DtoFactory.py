from ..Dto import Dto
from ..DtoVol import DtoVol
from ..DtoFacture import DtoFacture
from ..TransactionHistoryDto import TransactionHistoryDto

class DtoFactory:
    def create(self, dtoType: str, data:bytes) -> Dto:
        if dtoType == 'vol':
            return DtoVol.deserialize(data)
        elif dtoType == 'facture':
            return DtoFacture.deserialize(data)
        elif dtoType == 'transactionHistory':
            return TransactionHistoryDto.deserialize(data)
        else:
            raise ValueError(f"Unsupported DTO type: {dtoType}")

