n=int(input("Enter input: "))

for i in range(1,n+1):
    if i%5==0:
        print(f"{i} Yes\n")
    else:
        print(f"{i} No\n")