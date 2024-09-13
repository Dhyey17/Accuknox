Class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __iter__(self):
        yeild {"length" : self.length}
        yeild {width : self.width}

rectangle_obj=Rectangle(2,10)
