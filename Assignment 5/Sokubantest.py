#map
mx_width = 5
my_height = 6

#player
px = 3
py = 5
next_px = px
next_py = py
#walls
walls = [{"x": 2, "y": 5},{"x": 2, "y": 1}]

#points
points = [{"x": 0, "y": 0},
          {"x": 0, "y": 1}]
# points.append({"x": 1, "y": 0})
# points.append({"x": 1, "y": 1})
# points.append({"x": 3, "y": 0})
# points.append({"x": 3, "y": 1})
# points.append({"x": 4, "y": 0})
# points.append({"x": 4, "y": 1})

#boxes
boxes =  [{"x": 2, "y": 0},
          {"x": 1, "y": 2},]
# boxes.append({"x": 2, "y": 2})
# boxes.append({"x": 3, "y": 2})
# boxes.append({"x": 2, "y": 3})
# boxes.append({"x": 1, "y": 4})
# boxes.append({"x": 2, "y": 4})
# boxes.append({"x": 3, "y": 4})

# next_bx = ''
# next_by = ''


def check_match(list,x,y):
    for obj in list:
        if obj["x"] == x and obj["y"] == y:
            return True
    return False

def print_map(my_height,mx_width,px,py,walls,points,boxes):
    for y in range (my_height):
        for x in range (mx_width):
            if x == px and y == py:
                print("P ", end='')
            elif check_match(walls,x,y):
                print("# ",end='')
            elif check_match(boxes,x,y):
                print("B ", end='')
            elif check_match(points,x,y):
                print("o ",end='')
            else:
                print("_ ",end='')
        print()


def find_obj(list,x,y):
    for obj in list:
        if obj["x"] == x and obj["y"] == y:
            return obj
    return None

def move(x,y,dx,dy):
    return [x + dx, y + dy]

def check_map(x,y,mx_width,my_height):
    if x < 0 or x > mx_width -1 or y < 0 or y > my_height -1:
        return False
    return True

def check_win(boxes,points):
    if boxes == points:
        return True






while True:
    print_map(my_height, mx_width, px, py, walls, points, boxes)
    if check_win(boxes, points) == True:
        print("You Won!!!")
        break
    choice = input("Pls, choose (W-S-A-D): ").upper()

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

    [next_px,next_py] = move(px,py,dx,dy)
    check_map(next_px, next_py, mx_width, my_height)
    found_box = find_obj(boxes, next_px, next_py)
    if found_box is not None:
        found_box["x"] += dx
        found_box["y"] += dy
        [px, py] = [next_px, next_py]
    else:
        [px, py] = [next_px, next_py]







