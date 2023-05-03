import sys
import os
from typing import Type, Any

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..Dto import Dto
from ..DtoVol import DtoVol
# from dto.DtoFacture import DtoFacture

class DTOFactory:
    def create(self, dtoType: Type[Dto], *args: Any) -> Dto:
        if dtoType == DtoVol:
            return DtoVol(*args)
        # elif dtoType == DtoFacture:
        #     return DtoFacture(*args)
        else:
            raise ValueError(f"Unsupported DTO type: {dtoType}")

