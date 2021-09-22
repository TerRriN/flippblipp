

def flippblipp(x):

    if(x%3)+(x%5) == 0:
        return("flippblipp")
    elif(x%3) == 0:
        return("flipp")
    elif(x%5) == 0:
        return("blipp")
    else:
        return(str(x))
    
n = 10
for _ in range(n):
    x = _+1
    print(flippblipp(x))
    
