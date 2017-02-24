clothes = ["T-Shirt", "Sweater"]
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)?").upper()
    if n=="C":
        new_item = input("Enter new item?")
        clothes.append(new_item)
        print("Our items:", end=' ')
        for j in range(len(clothes)):
             print(clothes[j],end=" ,")
        print()
    elif n=="R":
        print("Our items:", end=' ')
        for j in range(len(clothes)):
             print(clothes[j],end=" ,")
        print()
    elif n=="U":
        position = int(input("Update position?"))
        new_item = input("New item?")
        clothes[position]= new_item
        print("Our items:", end=' ')
        for j in range(len(clothes)):
             print(clothes[j],end=" ,")
        print()
    elif n=="D":
        position = int(input("Delete position?"))
        del clothes[position]
        print("Our items:", end=' ')
        for j in range(len(clothes)):
             print(clothes[j],end=" ,")
        print()

