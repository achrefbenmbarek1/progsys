import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoFacture import DtoFacture

class FactureRepository:
    def __init__(self, fileName ):
        self.fileName = os.path.abspath(os.path.dirname(__file__)) +"/"+ fileName
    
    def readFactureByReferance(self, referance:str):
        with open(self.fileName, 'r') as f:
            for line in f:
                values = line.split()
                if values[0] == referance:
                    print(line)
                    return DtoFacture(values[0],values[1])
