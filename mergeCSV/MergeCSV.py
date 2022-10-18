left_hand = input("Input 1st file name:")
right_hand = input("Input 2nd file name:")
combine = input("Input the merged file name:")
separator = input("Input the separator:")

with open(left_hand) as LEFT, open(right_hand) as RIGHT, open(combine, "w") as COMBINE:
    for x,y in zip(LEFT,RIGHT):
        COMBINE.write(x.strip()+separator+y.strip()+'/n')