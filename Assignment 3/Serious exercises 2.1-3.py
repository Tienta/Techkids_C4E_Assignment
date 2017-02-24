size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Tien and these are my ship size\n",size)

print("Now my biggest sheep has size", max(size), "let's shear it")

biggest_position = size.index(max(size))
size[biggest_position]=8

print("After shearing, here is my flock",size)
