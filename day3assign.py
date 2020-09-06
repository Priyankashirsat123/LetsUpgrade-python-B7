num = int(input("Enter the altitude value:  "))
print(num)
if num <= 1000:
    print("Safe To Land")
elif num > 1000 and num < 5000:
    print("Bring Down To 1000")
elif num > 5000:
    print("Turn around and try later")
"""else:
    print("Turn Around")
"""

"""
output
Enter the altitude value:  899
899
Safe To Land

Enter the altitude value:  1200
1200
Bring Down To 1000

Enter the altitude value:  6500
6500
Turn around and try later
"""

print("**************************************************************************************")
print("Prime numbers are : ")
for Number in range (1, 201):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break
    if (count == 0 and Number != 1):
        print("%d" %Number, end = '  ')

"""

output
*****************************************************************************************************
Prime numbers are : 
2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97  101  103  107  109  113  127  131  137  139  149  151  157  163  167  173  179  181  191  193  197  199





