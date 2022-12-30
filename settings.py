def init():
    global window_size
    global cols
    global rows
    global grid
    global w
    global num_bees

    window_size = 600
    cols = 20
    rows = cols
    grid = make_2D_array(cols, rows)
    w = window_size // cols
    num_bees = (cols * rows) // 10


def make_2D_array(cols, rows):
    arr = [n for n in range(cols)]
    for i, _ in enumerate(arr):
        arr[i] = [n for n in range(rows)]
    return arr