
===========
PyAdventure
===========

------------------------------------
Create a text-based RPG with Python!
------------------------------------

New features coming every day!

-----------------
CURRENT FEATURES:
-----------------

- player
- enemies
- map
- movement

------------
COMING SOON:
------------

- combat
- inventory

SAMPLE TO GET STARTED::

    from pyadventure import pa
    class myGame(pa.Game):
  	    def MainLoop(self, player, world):
		    while True:
			    super().MainLoop(player, world)
	    def setup(self):
	        pa.m_print("Hello and welcome to my custom game!")
		    pa.m_print("What is your name?")
		    p = pa.Player(input())
		    pa.m_print("Hello, " + p.name + "! How big should the world be?")
		    size = int(input())
		    w = super().GenerateWorld(size)
		    self.MainLoop(p, w)
    if __name__ == "__main__":
	    g = myGame()
        g.setup()


