"""Module that provides a method of playing robot commands."""

##############################################################################
# Python imports.
from typing import List

##############################################################################
# Local imports.
from .state import State

##############################################################################
# Exception used to convey problems with the commands.
class CommandException( Exception ):
    """Exception thrown if there is a problem with a command."""

##############################################################################
# Command mapping.
COMMANDS = {
    "F": "forward",
    "L": "left",
    "R": "right"
}

##############################################################################
# Perform a list of commands starting with an initial state.
def perform( commands: List[ str ], state: State ) -> State:
    """Perform a list of commands for a robot.

    :param list commands: The list of commands to perform.
    :param State state: The initial state.
    :returns: The final state.
    :rtype: State
    """

    # For each of the commands...
    for command in commands:
        try:
            # Perform the command.
            state = getattr( state, COMMANDS[ command ] )()
        except KeyError:
            raise CommandException( f"Unknown command '{command}'" )

    # Finally, return the new state.
    return state

### commands.py ends here
