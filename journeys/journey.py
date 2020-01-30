"""Module that provides the class that holds details of a journey."""

##############################################################################
# General imports.
from dataclasses import dataclass
from typing      import List

##############################################################################
# Local imports.
from .state    import State
from .commands import perform

##############################################################################
# Class that holds details of a journey.
@dataclass
class Journey:
    """Holds details of a robot's journey.

    :ivar State start_state: The start state of the robot.
    :ivar State end_state: The end state of the robot.
    :ivar list commands: The commands for the robot.
    """

    #: The start state of the robot.
    start_state: State

    #: The end state of the robot.
    end_state: State

    #: The commands for the robot.
    commands: List[ str ]

    @property
    def is_valid( self ) -> bool:
        """Does the journey data look valid?

        :type: bool
        """
        return perform( self.commands, self.start_state ) == self.end_state

### journey.py ends here
