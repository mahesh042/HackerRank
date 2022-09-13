#text alignment
thickness = int(input())
if thickness%2 !=0:
    c = 'H'

    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness*5))
        if i == thickness-1:
            for j in range(thickness+1):
                print((c*thickness).rjust(thickness + math.floor((thickness/2)))+(c*thickness).rjust((thickness*5)-thickness))
                if j == thickness:
                    for k in range(math.ceil(thickness/2)):
                        print((c*(thickness*5)).rjust(thickness*5 + math.floor((thickness/2))))
                        if k == (math.ceil(thickness/2)-1):
                            for l in range(thickness+1):
                                print((c*thickness).rjust(thickness + math.floor((thickness/2))) + (c*thickness).rjust((thickness*5)-thickness))
                                if l == thickness:
                                    for m in range(thickness):
                                        print((c*(thickness-(m+1))).rjust((thickness*5)-1)+c+(c*(thickness-(m+1))).ljust((thickness*5)-(thickness)))
                            
else:
    thickness = int(input())
