smallest = 100
for nums in (25, 54 , 55, 12, 38, 9, 99, 22, 23):
    if nums < smallest:
        smallest = nums
    print("Currently the smallest number so far is, ", smallest)
print("After analysis, the smallest number in the loop is, ", smallest)