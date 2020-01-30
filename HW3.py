#filled seat and not filled seat
''' here i considered 2 seat filled in first row
    3rd seat is filled in second row
    1st seat is filled in the fourth row
    other seats are empty
'''
    
rows=7
columns=4
for row in range(1,rows+1):
    for col in range(1,columns+1):
        if((row==1 and col==2) or (row==2 and col==3) or (row==4 and col==1)):
            print("$",end="")
        else:
            print("#",end="")
    print()
