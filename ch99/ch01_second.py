# ch01_second.py
""" This is 
"""
import logging 

logging.basicConfig( level = logging.INFO )
logger = logging.getLogger( __name__ )

print( "Hello.. This is the second program in chapter 1." ) 
print( "name = %s" % ( __name__ ) )

logger.info( "aaaa" )
logger.debug( "bbbb" )
logger.error( "cccc" )