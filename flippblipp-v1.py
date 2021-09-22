n = 40
for cykel in range(n):
    x = cykel + 1
    
    if(x%3)+(x%5) == 0:
        print("flippblipp")
    elif(x%3) == 0:
        print("flipp")
    elif(x%5) == 0:
        print("blipp")
    else:
        print(x)