import tkinter as tk

D, W, H = 30, 20, 15
x_player = 0
y_player = 0
cells_values = [[0] * W for _ in range (H)]
# cells_values[3][4] = 1
# cells_values[4][4] = 1

root = tk.Tk()

canvas = tk.Canvas(root, width= D * W , height= D *H , bg='white')
canvas.pack(padx=10 , pady=10)

def draw_palayer():
    x1 = x_player * D
    y1 = y_player * D
    x2 = x1 + D
    y2 = y1 + D
    canvas.create_oval(x1 , y1 , x2 , y2 , fill='red')

def draw():
    canvas.delete('all')
    draw_palayer()
    for i in range(H):
        for  j in range(W):
            if cells_values[i][j] == 1:
                x1 = j * D
                y1 = i * D
                x2 = x1 + D
                y2 = y1 + D
                canvas.create_rectangle(x1 , y1 , x2, y2, fill='yellow', outline='yellow')
    for i in range(1, W):
        canvas.create_line(D * i , 0 , D * i, H *D)
    for i in range(1,H):
        canvas.create_line(0,D * i, W * D, D * i)
    if x_player  == W - 1 and y_player == H - 1:
        canvas.create_text(D * W //2 , D * H // 2 , text = 'You Win!!!' ,
                           fill='green' , font=(None ,50))

def left_click(event):
    x = event.x
    y = event.y
    # print('click', x, y)
    j = x // D
    i = y // D
    if not (i == y_player  and j == x_player):
        cells_values[i][j] = 0 if cells_values[i][j] == 1 else 1
        draw()
def key_press(event):
    # print(event.keycode)
    global  x_player , y_player
    x_next , y_next = None, None
    if event.keycode == 37 :
        x_next , y_next = x_player -1 , y_player
    if event.keycode == 39 :
        x_next, y_next = x_player + 1 , y_player
    if event.keycode == 38 :
        x_next , y_next = x_player , y_player -1
    if event.keycode == 40 :
        x_next , y_next = x_player , y_player + 1
    if x_next is None:
        return
    if x_next < 0 or y_next < 0:
        return
    if x_next == W or y_next == H:
        return
    if cells_values[y_next][x_next] == 1:
        return
    print(x_next , y_next)
    x_player , y_player = x_next , y_next
    draw()


draw()
canvas.bind('<Button-1>', left_click)
root.bind('<Key>' , key_press)
root.mainloop()