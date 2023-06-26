import modules.handler  as handler
import modules.data_base as m_data
import modules.restart as m_restart
def check(x, y):
    if x > 0 and y > 0 and x < 200 and y < 200:
        handler.handler(0)
    elif x > 200 and y > 0 and x < 400 and y < 200:
        handler.handler(1)
    elif x > 400 and y > 0 and x < 600 and y < 200:
        handler.handler(2)

    elif x > 0 and y > 200 and x < 200 and y < 400:
        handler.handler(3)
    elif x > 200 and y > 200 and x < 400 and y < 400:
        handler.handler(4)
    elif x > 400 and y > 200 and x < 600 and y < 400:
        handler.handler(5)

    elif x > 0 and y > 400 and x < 200 and y < 600:
        handler.handler(6)
    elif x > 200 and y > 400 and x < 400 and y < 600:
        handler.handler(7)
    elif x > 400 and y > 400 and x < 600 and y < 600:
        handler.handler(8)
    elif x > 0 and y > 600 and x < 600 and y < 800:
            m_restart.restart()