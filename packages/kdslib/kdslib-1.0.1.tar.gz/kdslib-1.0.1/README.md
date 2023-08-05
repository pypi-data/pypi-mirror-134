DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

################################################# INSTRUCTIONS #########################################################
# In your program always import the entire kdsutil module first, to properly set the local variables.                  #
# from kdslib import kdsutil                                                                                           #
# The main class can be instantiated like this: loggingutil = kdsutil.Generate_Logger(**kwargs)                        #
# The class variables can be accessed in this format: loggingutil.logger.info('Hello World')                           #
# The class methods can be accessed in this format: loggingutil.log_info('Hello World')                                #
########################################################################################################################