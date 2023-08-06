
class PolicyCollection:
        
    def __init__(self):
        self.AIA = ['AIA']
        self.AXA = ['AXA']
        self.BOCG = ['BOCG']
        self.CHINALIFE = ['CHINALIFE']
        self.PRU = ['PRU']
        self.FWD = ['FWD']
        self.MANULIFE = ['MANULIFE']
        self.YFLIFE = ['YFL']
        self.SUNLIFE = ['SUNLIFE']
        self.CIGNA = ['CIGNA']
        self.totalInsurranceList = [
            self.AIA,
            self.AXA,
            self.BOCG,
            self.CHINALIFE,
            self.PRU,
            self.FWD,
            self.MANULIFE,
            self.YFLIFE,
            self.SUNLIFE,
            self.CIGNA,
        ]
        self.supportedList = ['AIA','AXA','BOCG','CHINALIFE','PRU','FWD','MANULIFE','YFL','SUNLIFE','CIGNA']
        pass
    
    def cleanAllPolicy(self):
        self.AIA = ['AIA']
        self.AXA = ['AXA']
        self.BOCG = ['BOCG']
        self.CHINALIFE = ['CHINALIFE']
        self.PRU = ['PRU']
        self.FWD = ['FWD']
        self.MANULIFE = ['MANULIFE']
        self.YFLIFE = ['YFL']
        self.SUNLIFE = ['SUNLIFE']
        self.CIGNA = ['CIGNA']
        self.totalInsurranceList = [
            self.AIA,
            self.AXA,
            self.BOCG,
            self.CHINALIFE,
            self.PRU,
            self.FWD,
            self.MANULIFE,
            self.YFLIFE,
            self.SUNLIFE,
            self.CIGNA,
        ]
    
    def getTotalList(self):
        return self.totalInsurranceList

    def getSupportedList(self):
        return self.supportedList