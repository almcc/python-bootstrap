class Dummy(object):
    """docstring for Dummy"""
    def __init__(self):
        super(Dummy, self).__init__()
        self.state = True

    def getState(self):
        return self.state

    def isOff(self):
        if self.state:
            return False
        else:
            return True
