#map
mx_width = 5
my_height = 6

#walls
walls = [{"x": 2, "y": 5},{"x": 2, "y": 1}]

#player
p = {"x": 3, "y": 5 }

#points
points = [{"x": 0, "y": 0},
          {"x": 0, "y": 1}]
points.append({"x": 1, "y": 0})
points.append({"x": 1, "y": 1})
points.append({"x": 3, "y": 0})
points.append({"x": 3, "y": 1})
points.append({"x": 4, "y": 0})
points.append({"x": 4, "y": 1})

#boxes
boxes =  [{"x": 2, "y": 0},
          {"x": 1, "y": 2},]
boxes.append({"x": 2, "y": 2})
boxes.append({"x": 3, "y": 2})
boxes.append({"x": 2, "y": 3})
boxes.append({"x": 1, "y": 4})
boxes.append({"x": 2, "y": 4})
boxes.append({"x": 3, "y": 4})

def check_match(list,x,y):
    for obj in list:
        if obj["x"] == x and obj["y"] == y:
            return True

def print_map(mx_width,my_height,p,points,boxes,walls):
    for y in range (my_height):
        for x in range (mx_width):
            if x == p["x"] and y == p["y"]:
                print("P ", end='')
            elif check_match(boxes,x,y):
                print("B ", end='')
            elif check_match(points, x, y):
                print("o ", end='')
            elif check_match(walls,x,y):
                print("# ", end='')
            else:
                print("_ ", end='')
        print()

def move(obj,dx,dy):
    return {"x": obj["x"] + dx, "y": obj["y"] + dy}

def in_map(Obj,mx_width,my_height):
    if Obj["x"] < 0 or Obj["x"] > mx_width -1 or Obj["y"] < 0 or Obj["y"] > my_height -1:
        return False
    return True

def find_obj(list,check_list):
    for obj in list:
#        if obj == dict_val:
        if obj["x"] == check_list["x"] and obj["y"]== check_list["y"]:
            return obj
    return None

def check_collide(obj_dic, obj_list):
    for obj in obj_list:
        if obj["x"] == obj_dic["x"] and obj["y"] == obj_dic["y"]:
            return True
    return False

def check_win(boxes,points):
    if boxes == points:
        return True

while True:
    print_map(mx_width, my_height, p, points, boxes, walls)
    if check_win(boxes, points) == True:
        print("You Won!!!")
        break
    choice = input("Let's play (W-S-D-A): ").upper()

    dx = 0
    dy = 0
    if choice == "W":
        dy = -1
    if choice == "S":
        dy = 1
    if choice == "A":
        dx = -1
    if choice == "D":
        dx = 1

    next_p = move(p,dx,dy)
    if in_map(next_p,mx_width,my_height):
        found_box = find_obj(boxes,next_p)
        if found_box is not None:
            next_b = move(found_box,dx,dy)
            if in_map(next_b,mx_width,my_height) and not check_collide(next_b, walls):
                found_box["x"] += dx
                found_box["y"] += dy
                p = next_p
        elif not check_collide(next_p, walls):
            p = next_p
