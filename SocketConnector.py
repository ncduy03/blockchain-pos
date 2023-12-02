

class SocketConnector():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # check if the current SocketConnector object is equal to another 
    def equals(self, connector):
        if connector.ip == self.ip and connector.port == self.port:
            return True
        else:
            return False
