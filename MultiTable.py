# -*- coding: utf-8 -*-

#  ╔ ╦ ╗   ║ ║ ║   ╠ ╦ ╣   ╠ ╬ ╣   ╚ ╩ ╝   ═

fw = 119
w = fw//4*4
borders = [ 
            [ "╔", "╦", "╗" ], [ "║", "║",  "║" ], 
            [ "╠", "╦", "╣" ], [ "╠", "╬", "╣" ],  
            [ "╚", "╩", "╝" ] 
        ]

def p( btype = 0, c = " ", *cells ) :
    if len( cells ) == 0 : 
        cells = [ "" ]
    elif len( cells ) == 1 and type(cells[0]) is list:
        cells = cells[0]
    pass

    lents = len( cells )
    tw = w // lents
    
    for i, cell in enumerate( cells ) : 
        b = borders[btype]
        t = ""

        if i == 0 : 
            t += b[0]
        else :
            t += b[1]
        
        t += cell.center( tw - len(cell) - 1 + len(cell.encode("ascii", "ignore")), c ) 

        if i == lents - 1 : 
            t += b[-1] 
        pass
        
        print( t, end="" )
    pass
    print()
pass

print()
p( 0, "═" ) 
p( 1, " ", "구구단" )
for i in range( 2, 7, 4 ) :
    p( [3, 2][ i == 2 ], "═", [""] * 4 )
    p( 1, " ", [ f"{i + c} 단" for c in range(4) ] )
    p( 3, "═", [""] * 4 )
    for r in range( 1, 10 ) :
        cells = [ f"{i + c} x {r} = {(i+c)*r:2}" for c in range(4) ]
        p( 1, " ", cells )
    pass
pass
p( 4, "═", [""] * 4 )
