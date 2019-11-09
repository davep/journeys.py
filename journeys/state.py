"""Module that provides the robot's state class."""

##############################################################################
# General imports.
from dataclasses import dataclass, replace

##############################################################################
# Exception used to convey problems with the State class.
class StateException( Exception ):
    """Exception thrown if there is a problem with a State instance."""

#: ID for facing north.
NORTH = "N"

#: ID for facing east.
EAST = "E"

#: ID for facing south.
SOUTH = "S"

#: ID for facing west.
WEST = "W"

#: The compass that the robot can turn through.
COMPASS = [
    NORTH,
    EAST,
    SOUTH,
    WEST
]

##############################################################################
# Class that holds the state of the robot.
@dataclass
class State:
    """Holds a robot's state.

    :ivar int x_pos: The X position of the robot.
    :ivar int y_pos: The Y position of the robot.
    :ivar str facing: The direction the robot is facing.
    """

    #: X position of the robot.
    x_pos: int = 0

    #: Y position of the robot.
    y_pos: int = 0

    #: Direction the robot is facing.
    facing: str = EAST

    def _turn( self, compass ):
        """Make a 90 degree turn on the given compass.

        :param list compass: List of compass directions to turn through.
        :returns: A new state.
        :rtype: State
        """
        return replace( self, facing=compass[ compass.index( self.facing ) - 1 ] )

    def left( self ):
        """Make a 90 degree turn to the left.

        :returns: A new state.
        :rtype: State
        """
        return self._turn( COMPASS )

    def right( self ):
        """Make a 90 degree turn to the right.

        :returns: A new state.
        :rtype: State
        """
        return self._turn( list( reversed( COMPASS ) ) )

    def forward( self ):
        """Move forward one position.

        :returns: self
        :rtype: State
        """

        if self.facing == NORTH:
            return replace( self, y_pos=self.y_pos + 1 )

        if self.facing == SOUTH:
            return replace( self, y_pos=self.y_pos - 1 )

        if self.facing == EAST:
            return replace( self, x_pos=self.x_pos + 1 )

        if self.facing == WEST:
            return replace( self, x_pos=self.x_pos - 1 )

        # We appear to have being facing in a direction we don't know about.
        raise StateException( f"Facing in unknown direction '{self.facing}'" )

    def __str__( self ):
        """Return a string representation of the state."""
        return f"{self.x_pos} {self.y_pos} {self.facing}"

### state.py ends here
