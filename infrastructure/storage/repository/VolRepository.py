class VolRepository:
    def __init__(self, fileName ):
        self.fileName = fileName
    
    def readVolByReferance(self, referance:str):
        with open(self.fileName, 'r') as f:
            for line in f:
                values = line.split()
                if values[0] == referance:
                    print(line)

