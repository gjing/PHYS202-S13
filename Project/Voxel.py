class Voxel:
    """A class to store the parameters of each voxel"""
    def __init__(self, data):
        self.volume = float(data.split(' ')[0])
        self.row = float(data.split(' ')[1])
        self.column = float(data.split(' ')[2])
        self.bucket = float(data.split(' ')[3])
        self.ADC = float(data.split(' ')[4])
    def getGradient(self, other):
        return (self.ADC - other.ADC)/((self.row-other.row)**2 + (self.column-other.column)**2)