from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        leftHost = self.addHost('h1')
        rigthHost = self.addHost('h2')
        centerSwitch = self.addSwitch('s1')

        self.addLink(leftHost,centerSwitch)
        self.addLink(centerSwitch,rigthHost)

    topos = {'myTopo': (lambda: MyTopo()) }
    