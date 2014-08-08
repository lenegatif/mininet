"""constrain size of subnets to /24
- place 1 mininet hosts on each subnet

To run,
$ sudo mn --custom ~/src/mininet/custom/topo-2s-2h.py --topo=topo2s2h --controller=ovsc
"""

from mininet.topo import Topo

class Topo2s2h( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        s1 = self.addSwitch( 's1' )
        s1h1 = self.addHost( 's1h1', ip="192.168.21.10/24" )
      # s1h2 = self.addHost( 's1h2', ip="192.168.21.11/24" )

        s2 = self.addSwitch( 's2' )
        s2h1 = self.addHost( 's2h1', ip="192.168.22.10/24" )
        #s2h2 = self.addHost( 's2h2', ip="192.168.22.11/24" )

        #s3 = self.addSwitch( 's3' )
        #s3h1 = self.addHost( 's3h1', ip="192.168.23.10/24" )
        #s3h2 = self.addHost( 's3h2', ip="192.168.23.11/24" )

        # Add links
        self.addLink( s1h1, s1 )
        #self.addLink( s1h2, s1 )

        self.addLink( s2h1, s2 )
        #self.addLink( s2h2, s2 )

        #self.addLink( s3h1, s3 )
        #self.addLink( s3h2, s3 )

        self.addLink( s1, s2 )
        # self.addLink( s2, s3 )

topos = { 'topo2s2h': ( lambda: Topo2s2h() ) }
