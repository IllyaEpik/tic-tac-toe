import pygame, modules.check as m_check
import modules.data_base as m_data
icon = pygame.image.load(m_data.m_clas.m_path.find_file("img/icon.ico"))
pygame.display.set_icon(icon)
pygame.display.set_caption("Хрестеки нулики")
game = True
screen = pygame.display.set_mode((600, 800))
background = m_data.m_clas.Item(0, 0, 600, 800)
background.load_image("background")
field = m_data.m_clas.Item(0, 0, 600, 600)
field.load_image("field")
restart = m_data.m_clas.Item(0, 600, 600, 200)
restart.load_image("Restart")
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           cor = pygame.mouse.get_pos()
           m_check.check(cor[0], cor[1])
        if m_check.m_data.update:
            background.blits(screen)
            restart.blits(screen)
            for count in range(9):
                if m_data.list_cell[count].CELL!=2:
                    m_data.list_cell[count].blits(screen)
            field.blits(screen)
            if m_data.win ==  True:
                m_data.line.blits(screen)
            pygame.display.flip()
            m_data.update = False 