import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoVol import DtoVol

class VolRepository:
    def __init__(self, fileName ):
        self.fileName = os.path.abspath(os.path.dirname(__file__)) +"/"+ fileName
    
    def readVolByReferance(self, referance:str):
        with open(self.fileName, 'r') as f:
            for line in f:
                values = line.split()
                if values[0] == referance:
                    print(line)
                    return DtoVol(values[1],int(values[2]),float(values[3]),values[0])

