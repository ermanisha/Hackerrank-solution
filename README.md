# coursera assignments

steps="UDDDUDUU"
def countingValleys(n,steps):
    seaLevel=valley=0
    for step in steps:
       
        if step == 'U':
            seaLevel+=1
            print("seaLevel+=1",seaLevel)
        else:
            seaLevel-=1
            print("seaLevel-=1",seaLevel)
        if step=='U' and seaLevel==0:
            valley+=1
            print("valley+=1",valley)
    return valley

print(countingValleys(8,steps))
