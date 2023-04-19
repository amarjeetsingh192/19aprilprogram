## create afunction that takes the no of win draws and losses and calculate the no of points
#win get 3 point
#draws get 1 points
#losses get 0 point

def football(wins,draws,losses):
    wins=wins*3
    draws=draws*1
    losses=losses*0
    return(wins,draws,losses)
wins=int(input("enter : "))
print(football(wins,3,4))