#! /usr/bin/env python

"""! @package utils
"""

from utils.io import open_file, EOL
from utils.error_handling import Error

def log(msg, options=None):
    """! @brief Write message into log file if any, or to standard output if verbose mode is on.
    @param msg String to log.
    @param options User options.
    """
    try:
        import sys
        ## If provided, set function variables according to user options
        if options is not None:
            # Keep log filename and verbose mode in function variables
            setattr(log, "log_filename", options.log_filename)
            setattr(log, "verbose", options.verbose)
            # Initialize log file
            if log.log_filename is not None:
                log_file = open_file(log.log_filename, 'w+')
                log_file.close()
        ## Prepare message to log: add end of line to message
        msg += EOL
        ## Depending on options, log into file or standard output
        if hasattr(log, "log_filename") and log.log_filename is not None:
            # Open log file
            log_file = open_file(log.log_filename, 'a')
            # Write message into log file
            log_file.write(msg)
            # Close log file
            log_file.close()
        # If no log filename has been specified, check if verbose mode has been set by user
        elif hasattr(log, "verbose") and log.verbose:
            sys.stdout.write(msg)
    except IOError as exception:
        raise Error("Cannot write into log file '%s'." % options.log_filename, exception)
