from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor

def doCrawl(url,re=""):
    return None

class GetTask(Protocol):
    def connectionMade(self):
        self.transport.write("Hi, server")
        #self.transport.loseConnection()

    def dataReceived(self,url):
        print url
        crawresult = doCrawl(url)
        if crawresult is not None:
            self.transport.write(crawresult)

class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print "Connection starting..."
    def buildProtocol(self, addr):
        print addr
        return GetTask()
    def clientConnectionLost(self, connector, reason):
        print "lose reason ",reason
    def clientConnectionFailed(self, connector, reason):
        print "failed reason ",reason



reactor.connectTCP("127.0.0.1",8001,EchoClientFactory())
reactor.run()