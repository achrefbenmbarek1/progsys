from ..Dto import Dto
from ..DtoVol import DtoVol

class DtoFactory:
    def create(self, dtoType: str, data:bytes) -> Dto:
        if dtoType == 'vol':
            return DtoVol.deserialize(data)
        # elif dtoType == DtoFacture:
        #     return DtoFacture(*args)
        else:
            raise ValueError(f"Unsupported DTO type: {dtoType}")

