def flippblipp(x):
    if(x%3)+(x%5) == 0:
        return("flippblipp")
    elif(x%3) == 0:
        return("flipp")
    elif(x%5) == 0:
        return("blipp")
    else:
        return(str(x))
    
gameOn = True
n = 2
print("       1")
while gameOn == True:
    x = input("Nästa: ")
    if(flippblipp(n) != x):
        print("FEL - ", flippblipp(n), "\n\nGame Over")
        gameOn = False       
    
    
