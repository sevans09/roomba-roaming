# roomba-roaming 

Python implemented Roomba-style program using reflex rules. Always checks the battery level first. If the level is below 30%, it will plan a path to its charging base (“home”), go there, and start the docking procedure. If the battery is at a sufficient level, it will start the function it was commanded to perform. The available commands are:

Spot cleaning: it will perform a 20s intensive cleaning in a specific area
General cleaning: go around the room and vacuum dust until the battery falls under 30%
Do nothing
During general cleaning, if the dust sensor detects a particularly dirty spot, the Roomba will perform a 35s spot cleaning.

Accepts a blackboard object as input (a regular hash map or dictionary).
