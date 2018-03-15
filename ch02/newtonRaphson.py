# hell.py

version = 1.1 
LINE = "#####################################################"
EPSILON = 1.0/100000000 

def f( x ) :
    
    return ( x*x ) - 4 

def derivative( x ) :
    e = x*EPSILON ;     
    drv = ( f( x + e ) - f( x - e ) )/(2*e)
    return drv 

def main() : 
    print( LINE )
    print( "Hello!" )
    print( "This program version is %.1f" % ( version ) )
    print( LINE )

    x = 6.0 
    y = 10000.0 

    index = 0 

    valid = False 

    while False == valid :
        y = f( x )
        print( "[%04d] f(%.20f) = %.20f" % ( index, x , y ) )
        x = x - ( y/(2*derivative( x )) )
        valid = abs( y ) < EPSILON 
        index += 1 

    if True == valid :   
        print( "The Solution is %.20f." % x )
        print( "The solution has been found in %d steps." % ( index + 1 ) )
    elif False == valid :
        print( "A solution has not been found." ) 

    print( LINE )
    print( "Good bye!" )
    print( LINE )

main()