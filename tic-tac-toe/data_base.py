import modules.clas as m_clas
list_cell = []
step = False
update = True
win = False                      
line = m_clas.Item(width= 600, height= 100)
def start():
    global list_cell
    list_cell = []
    x = 15
    y = 15
    for count in range(9):
        list_cell += [m_clas.Item(x, y)]
        x += 195
        if x > 415:
            x = 15
            y += 195
start() 