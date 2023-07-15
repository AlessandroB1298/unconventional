'''
This is a c project where your focus is building
a mario tower.

What you'll learn: Loops, User input, Syntax, and some
computaation


what should it look like: 

    #
   ##
  ###
 ####
#####


'''

row = 0 
while True:
    height = int(input("Height: "))
    if height >= 1 and height <= 8:
        break
space = 1
    
for row in range(height):
    for space in range (height - row -1):
        print(" ",end='')
    for hash in range(row):
        print("#", end ='')
    print()