"""Journey input reader."""

##############################################################################
# General imports.
import re

##############################################################################
# Local imports.
from .state    import State, COMPASS
from .journey  import Journey
from .commands import COMMANDS

##############################################################################
# Bad state exception.
class InvalidState( Exception ):
    """Exception thrown if a state line doesn't look correct"""

##############################################################################
# Bad command exception.
class InvalidCommands( Exception ):
    """Exception thrown if a command line doesn't look correct"""

##############################################################################
# Regular expression to read a state line.
STATE_FORMAT = re.compile( rf"^(\d+) (\d+) ([{''.join(COMPASS)}])$" )

##############################################################################
# Parse the given line as state.
def parse_state( text ):
    """Parse a given line of text as a robot state.

    :param str text: The text to parse.
    :returns: A populated State object.
    :rtype: State
    :raises InvalidState:
    """

    # Does the given text parse?
    if state := STATE_FORMAT.match( text ):
        # It does! Create a new state object.
        return State(
            x_pos  = int( state.groups()[ 0 ] ),
            y_pos  = int( state.groups()[ 1 ] ),
            facing = state.groups()[ 2 ]
        )

    # We can't handle that as a state line, throw an exception to say so.
    raise InvalidState( f"'{text}' is an invalid state line" )

##############################################################################
# Regular expression to read a command line.
COMMANDS_FORMAT = re.compile( rf"^([{''.join(COMMANDS.keys())}]+)$" )

##############################################################################
# Parse a command line.
def parse_commands( text ):
    """Parse a line of text as robot commands.

    :param str text: The line of text to parse.
    :returns: A list of commands to perform.
    :rtype: list
    :raises InvalidCommands:
    """

    # Does the given text parse?
    if commands := COMMANDS_FORMAT.match( text ):
        return list( commands.groups()[ 0 ] )

    # We can't handle that as a command line, throw an exception to say so.
    raise InvalidCommands( f"'{text} is an invalid command line" )

##############################################################################
# Class for reading in the journey input.
def journeys( source ):
    """Read the journeys found in the given source.

    :param TextIOBase source: A stream that is a source of journeys.
    :returns: A journey generator.
    :rtype: Iterator[Journey]
    """

    # Reading the source line-by-line...
    for line in source:
        # ...if we've found a non-empty line...
        if line.strip():
            # ...treat it and the two lines that follow as a journey.
            yield Journey(
                start_state = parse_state( line ),
                commands    = parse_commands( source.readline() ),
                end_state   = parse_state( source.readline() )
            )

### reader.py ends here
