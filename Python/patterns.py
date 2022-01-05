def printDaimond(n):
    #prints n row of daimond pattern
    for x in range(1 , n+1):
        print("  "*(n-x)," *"*x," *"*(x-1),sep="")
    for x in range(2 , n+1):
        print("  "*(x-1) , " *"*(n-x+1)," *"*(n-x),sep="")

printDaimond(20)