##In this challenge, a farmer is asking you to tell him how many legs can be counted among all
# his animals.
# The farmer breeds three species: chickens = 2 legs cows = 4 legs pigs = 4 legs


def farm(ch,cows,dogs):
    tch=ch*2
    tcow=cows*4
    tdog=dogs*4
    return(tch+tcow+tdog)
ch=int(input("enter : "))
print(farm(ch,3,4))

def farm(ch,cows,dogs):
    return(ch*2+(cows+dogs)*4)
print(farm(2,4,7))


