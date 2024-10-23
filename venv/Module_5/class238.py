class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        #class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        value1 = self.x + self.y
        value2 = other.x + other.y
        return value1 > value2
    


if __name__ == '__main__':
    p1 = Ponto(15, 2)
    p2 = Ponto(1, 4)
    p3 = p1 + p2
    print(p3)
    print(f'P1 e maior do que p2?', p1 > p2)
    print(f'P2 e maior do que p1?', p2 > p1)