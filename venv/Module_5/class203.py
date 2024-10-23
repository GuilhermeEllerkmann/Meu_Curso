#mantendo estados dentro da classe

class Camera:
    def __init__(self, nome_camera, filmando=False):
        self.nome_camera = nome_camera
        self.filmando = filmando

    def fotografar(self):

        if self.filmando:
            print('A camera nao pode fotografar, pois esta filmando')
            return
            
        print(f'Foto capturada')

    def filmar(self):

        if self.filmando == True:
            print('A camera ja esta filmando')
            return
        
        self.filmando = True
        print('Comecando gravacao')

    def parar_de_filmar(self):
        self.filmando = False
        print('Parando gravacao')


camera_sony = Camera('Sony')

camera_sony.fotografar()
camera_sony.filmar()
camera_sony.fotografar()
camera_sony.parar_de_filmar()
camera_sony.fotografar()

        