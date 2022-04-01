"""
Custom topology for mininet based off the UH SCADA Lab
Based off of the network map as of 31 Mar 22
"""

from mininet.topo import Topo

class MyTopo( Topo ):
	"SCADA Lab topology for mininet"
	def build( self ):
		"Create custom topo."

		# Add switches
		UHUplink = self.addSwitch( 's1' )
		WAVLINK = self.addSwitch( 's2' )	
		HP_2920_24G = self.addSwitch( 's3' )
		MDSEntraNet = self.addSwitch( 's4' )
		HP_2520G_8_PoE = self.addSwitch( 's5' )

		# Add hosts
		GW_VIP1 = self.addHost( 'h1' )
		DESKTOP_V0 = self.addHost( 'h2' )
		QTpi_2 = self.addHost( 'h3' )
		QTpi_3 = self.addHost( 'h4' )
		SEL3505 = self.addHost( 'h5' )
		DL205 = self.addHost( 'h6' )
		Joseph_pi = self.addHost( 'h7' )
		QTpi_4 = self.addHost( 'h8' )
		QTpi_5 = self.addHost( 'h9' )
		QTpi_6 = self.addHost( 'h10' )  

		# Add links
		self.addLink( UHUplink, GW_VIP1 )
		self.addLink( UHUplink, WAVLINK )
		self.addLink( WAVLINK, DESKTOP_V0 )
		self.addLink( WAVLINK, HP_2920_24G )
		self.addLink( HP_2920_24G, QTpi_2 )
		self.addLink( HP_2920_24G, QTpi_3 )
		self.addLink( HP_2920_24G, MDSEntraNet )
		self.addLink( MDSEntraNet, HP_2520G_8_PoE )
		self.addLink( HP_2520G_8_PoE, SEL3505 )
		self.addLink( HP_2520G_8_PoE, DL205 )
		self.addLink( HP_2520G_8_PoE, Joseph_pi )
		self.addLink( HP_2520G_8_PoE, QTpi_4 )
		self.addLink( HP_2520G_8_PoE, QTpi_5 )
		self.addLink( HP_2520G_8_PoE, QTpi_6 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
