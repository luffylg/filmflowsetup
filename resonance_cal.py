class Resonance:
    def __init__(self):
        self.low=1
        self.high=100
        self.add=100

    def set_params(self):
        pass


    def cpmodel(self):
        pass


    def findpoint(self):
        pass


    def calinterfoam(self):
        pass


    def getfuzhi(self,Re):
        self.calinterfoam()


    def get_resonancepoint(self,niandu,jiaodu):
        self.set_params()
        self.cpmodel()
        self.findpoint()
