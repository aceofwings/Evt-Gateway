from gateway.opencan.nmt import NMT
from gateway.can.listener import Listener

class CanOpenDevice:
    def __init__(self,nodeID,edsFile=None):
        self.nodeID = nodeID
        self.edsFile = edsFile
        self.controller = None
        self.nmt = None

    #crucial setup of listeners and functions
    def setup(self,controller):
        self.controller = controller
        self.nmt = NMT(self.nodeID,controller)
        return self.__buildListener()

    #Define and ad all cruial internal handlers to the listener.
    #This gets called to add any device specific handlers.
    def __buildListener(self):
        listener = Listener()
        listener.addHandler(self.nodeID + 0x70, self.nmt.handleheartBeat)
        listener.addHandler(0x00, self.nmt.handleNMT)
        return listener
