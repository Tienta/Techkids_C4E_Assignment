#map
m_col = 5
m_row = 5
#point
pt_x = 4
pt_y = 3
#wall
wx = 3
wy = 3
#player start
px = 1
py = 1
#box start
bx = 1
by = 3
#player new position
n_px = px
n_py = py
#box new position
n_bx = bx
n_by = by

def move(x,y,dx,dy):
    return [x + dx, y + dy]

def checkmap (n_px, n_py, n_bx, n_by):
    if n_px < 0 or n_py < 0 or n_bx < 0 or n_by < 0 \
            or n_px > m_row -1 or n_py > m_col -1 or n_bx > m_row -1 or n_by > m_col -1\
            or [n_px,n_py] == [wx,wy] or [n_bx,n_by]==[wx,wy]:
        print("Out of map, please try again: ")
        return False
    return True

def print_map(m_row, m_col,px,py,bx,by,wx,wy,pt_x,pt_y):
    for row in range(m_row):
        for col in range(m_col):
            if row == px and col == py:
                print("T ", end='')
            elif row == bx and col == by:
                print("B ", end='')
            elif row == pt_x and col == pt_y:
                print(". ", end='')
            elif row == wx and col == wy:
                print("# ", end="")
            else:
                print("_ ", end='')
        print()

def check_win(bx,by,pt_x,pt_y):
    if [bx,by] == [pt_x,pt_y]:
        return True
while True:
    print_map(m_row,m_col,px,py,bx,by,wx,wy,pt_x,pt_y)
    if check_win(bx,by,pt_x,pt_y)== True :
        print("You Won!!!")
        break
    choice = input("What do you want? W,S,A,D: ").upper()
    dx = 0
    dy = 0
    if choice == "W":
        dx = -1
    elif choice == "S":
        dx = 1
    elif choice == "D":
        dy = 1
    elif choice == "A":
        dy = -1

    [n_px, n_py] = move(px,py,dx,dy)
    if n_px == bx and n_py == by:
        [n_bx, n_by] = move(bx, by, dx, dy)

    if checkmap(n_py, n_px, n_bx, n_by)== False:
        print("Try again")
    else:
        px = n_px
        py = n_py
        bx = n_bx
        by = n_by
