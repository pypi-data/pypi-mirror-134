from .names import names
from .utils import hsl
from .utils import rgb


def get_color_name(color: str):
    color = color.upper()
    if len(color) < 3 or len(color) > 7:
        return '#000000', f'Invalid Color: {color}', False

    if len(color) % 3 == 0:
        color = f'#{color}'

    if len(color) == 4:
        color = f'#{color[1] * 2}{color[2] * 2}{color[3] * 2}'

    r, g, b = rgb(color)  # noqa: E741
    h, s, l = hsl(color)  # noqa: E741

    cl = -1
    df = -1

    for i in range(len(names)):
        if color == names[i][0]:
            return names[i][0], names[i][1], True

        ndf1 = ((r - names[i][2]) ** 2) + \
            ((g - names[i][3]) ** 2) + ((b - names[i][4]) ** 2)
        ndf2 = ((h - names[i][5]) ** 2) + \
            ((s - names[i][5]) ** 2) + ((l - names[i][5]) ** 2)
        ndf = ndf1 + ndf2 * 2

        if df < 0 or df > ndf:
            df = ndf
            cl = i

    if cl < 0:
        return '#000000', f'Invalid Color: {color}', False

    return names[cl][0], names[cl][1], False
