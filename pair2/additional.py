height = int(input("Enter height"))
width = int(input("Enter width"))

if height < 3 or width < 3:
    print('Enter bigges size')
else:
    for h in range(1,height + 1):
        for w in range(1, width + 1):
            if h >= w:
                print("#", end='')
        print()