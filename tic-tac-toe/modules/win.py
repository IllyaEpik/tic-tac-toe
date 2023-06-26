import modules.data_base as m_data
import pygame
import modules.main_loop as m_loop
import modules.clas as m_clas
def win_help(cell, cell1, cell2, rotate = 0):
    m_data.win =True
    m_data.list_cell[cell].load_image(m_data.list_cell[cell].IMG2 +"_win")
    if m_data.list_cell[cell].CELL == 1: 
        line = line_red
    else:
        line = line_green
    m_data.list_cell[cell1].load_image(m_data.list_cell[cell1].IMG2 +"_win")
    if  not rotate:
        m_data.line.Y = m_data.list_cell[cell].Y + 38; m_data.line.WIDTH = 550; m_data.line.X = m_data.list_cell[cell].X + 8
    elif rotate == 90:
        m_data.line.X = m_data.list_cell[cell].X + 38; m_data.line.WIDTH = 550; m_data.line.Y = m_data.list_cell[cell].Y + 10
    else:
        plus2 = 0
        if rotate > 0:
            divincion = 10
            plus = 15
        else:
            plus = 15 
            plus2 = 20
            divincion = 1
        m_data.line.X = m_data.list_cell[cell].X + plus
        m_data.line.Y = m_data.list_cell[cell].Y/divincion + plus2;m_data.line.WIDTH = 650
    m_data.line.load_image(line, rotate)
    m_data.list_cell[cell2].load_image(m_data.list_cell[cell2].IMG2 +"_win")
    m_data.update = True
def win():
    if m_data.list_cell[0].CELL==m_data.list_cell[1].CELL==m_data.list_cell[2].CELL!=2:
        win_help(0, 1, 2)   
    elif m_data.list_cell[3].CELL==m_data.list_cell[4].CELL==m_data.list_cell[5].CELL!=2:
        win_help(3, 4, 5)
    elif m_data.list_cell[6].CELL==m_data.list_cell[7].CELL==m_data.list_cell[8].CELL!=2:
        win_help(6, 7, 8)

    elif m_data.list_cell[0].CELL==m_data.list_cell[3].CELL==m_data.list_cell[6].CELL!=2:
        win_help(0, 3, 6, 90)
    elif m_data.list_cell[1].CELL==m_data.list_cell[4].CELL==m_data.list_cell[7].CELL!=2:
        win_help(1, 4, 7, 90)
    elif m_data.list_cell[2].CELL==m_data.list_cell[5].CELL==m_data.list_cell[8].CELL!=2:
        win_help(2, 5 ,8, 90)
    
    elif m_data.list_cell[0].CELL==m_data.list_cell[4].CELL==m_data.list_cell[8].CELL!=2:
        win_help(0, 4, 8, -225)
    elif m_data.list_cell[2].CELL==m_data.list_cell[4].CELL==m_data.list_cell[6].CELL!=2:
        win_help(6, 4, 2, 45)
line_red = "red_line"    
line_green = "green_line"