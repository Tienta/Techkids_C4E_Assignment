size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Tien and these are my ship size\n",size)
while True:
    m = int(input("How many month has passed?"))

    new_size = [ x+50 for x in size ]
    
    print("MONTH", m)
    print("One month has passed, now here is my flock\n",new_size)
    print("Now my biggest sheep has size", max(new_size), "let's shear it")
      
    p = new_size.index(max(new_size))
    new_size[p]= 8

    print("After shearing, here is my flock\n",new_size)

    new_size,size = size,new_size
    
