import os
import __main__
from reportlab.lib import colors


class ResourceLocation:
    def __init__(self, path):
        self.path = os.path.join(os.path.dirname(__main__.__file__), path)

    def getFullPath(self):
        return os.path.abspath(self.path)


def colorRanger(c0, c1, n):
    temp = []
    temp2 = []
    if n == 1: return [c0]

    if n > 1:
        lim = n - 1
        for i in range(n):
            temp.append(colors.linearlyInterpolatedColor(c0, c1, 0, lim, i))
    for i in temp:
        temp2.append(i.rgba())
    return temp2
