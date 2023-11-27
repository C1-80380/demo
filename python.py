count = 0

while(count <= 20):
    for i in range(2, 20):
        for j in range(2, i):
            if i < j:
                print("The number",i,"is prime")
            elif i % j == 0:
                break
        else:
            print("The number",i,"is prime")
            count = count + 1
            print(count)
