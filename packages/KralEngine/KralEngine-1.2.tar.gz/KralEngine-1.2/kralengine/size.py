class IMAGE_SIZE:
    def __init__(self):
        pass


class SIZE:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_height(self):
        return self.h

    def get_width(self):
        return self.w

    def get_size(self):
        return self.w, self.h
