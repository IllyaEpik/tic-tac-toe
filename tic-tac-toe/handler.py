import modules.data_base as m_data
import modules.main_loop as m_loop
import modules.win as m_win
def handler(cell):
    if m_data.list_cell[cell].CELL == 2 and not m_data.win: 
        if m_data.step == 0:
            m_data.list_cell[cell].load_image("zero")
        if m_data.step:
            m_data.list_cell[cell].load_image("cross")
        m_data.list_cell[cell].CELL = m_data.step
        m_data.update = True
        m_data.step = not m_data.step
        m_win.win()
    