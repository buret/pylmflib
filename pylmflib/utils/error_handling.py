#! /usr/bin/env python

"""! @package utils
"""

class Error(Exception):
    """! Base class for exceptions in this library.
    """
    def __init__(self, msg, excp=None):
        """! @brief Constructor.
        @param msg String to be reported to user.
        @param excp Raised system exception if any: IOError, KeyboardInterrupt, SystemExit, IndexError, KeyError, AttributeError, TypeError, NameError, UnboundLocalError, ValueError.
        @return An Error instance.
        """
        self.msg = msg
        self.excp = excp
        # Retrieve caller information
        import inspect
        self.frame_info = inspect.getframeinfo(inspect.currentframe().f_back)

    def __str__(self):
        """! @brief Build the string to be displayed.
        @return A Python string.
        """
        from utils.io import EOL
        # Follow Python display error style:
        #  File "user/scenario.py", line 5, in <module>
        #    from startup import *
        result = "  File \"" + self.frame_info.filename + "\", line " + str(self.frame_info.lineno) + ", in " + str(self.frame_info.function) + EOL
        result += "    Error: " + self.msg
        return result

    def handle(self):
        """! @brief Define behavior to follow in case this error is caught: diplay error and exit program.
        """
        print self
        # If a system error occured, report it
        if self.excp is not None:
            print self.excp
        # We consider that the error is not recoverable
        import sys
        sys.exit(-1)

class InputError(Error):
    """! Exception raised for errors in the input.
    """
    def __init__(self, msg, expr=None):
        """! @brief Constructor.
        @param msg Explanation of the error.
        @param expr Input expression in which the error occurred.
        @return An InputError instance.
        """
        self.msg = msg
        self.expr = expr
        # Retrieve caller information
        import inspect
        self.frame_info = inspect.getframeinfo(inspect.currentframe().f_back)

    def handle(self):
        """! @brief Define behavior to follow in case this error is caught: display error and exit program.
        """
        print self
        # If there is input expression, report it
        if self.expr is not None:
            print "    Input:", self.expr
        else:
            print "    Input:", self.frame_info.code_context[self.frame_info.index]
        # We consider that the error is not recoverable
        import sys
        sys.exit(-1)

class OutputError(Error):
    """! Exception raised for errors in the output.
    """
    def __init__(self, msg, expr=None):
        """! @brief Constructor.
        @param msg Explanation of the error.
        @param expr Output expression in which the error occurred.
        @return An OutputError instance.
        """
        self.msg = msg
        self.expr = expr
        # Retrieve caller information
        import inspect
        self.frame_info = inspect.getframeinfo(inspect.currentframe().f_back)

    def handle(self):
        """! @brief Define behavior to follow in case this error is caught: display error and exit program.
        """
        print self
        # If there is output expression, report it
        if self.expr is not None:
            print "    Output:", self.expr
        else:
            print "    Output:", self.frame_info.code_context[self.frame_info.index]
        # We consider that the error is not recoverable
        import sys
        sys.exit(-1)

class Warning(UserWarning):
    """! Base class for warnings in this library.
    """
    def __init__(self, msg):
        """! @brief Constructor.
        @param msg String to be reported to user.
        @return A Warning instance.
        """
        self.msg = msg
        # Retrieve caller information
        import inspect
        self.frame_info = inspect.getframeinfo(inspect.currentframe().f_back)

    def __str__(self):
        """! @brief Build the string to be displayed.
        @return A Python string.
        """
        from utils.io import EOL
        # Follow Python display error style
        #  File "user/scenario.py", line 5, in <module>
        #    from startup import *
        result = "  File \"" + self.frame_info.filename + "\", line " + str(self.frame_info.lineno) + ", in " + str(self.frame_info.function) + EOL
        result += "    Warning: " + self.msg
        return result
