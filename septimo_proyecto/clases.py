class CD:

    def __init__(self,autor,titulo,cant_canciones):
        self.autor = autor
        self.titutlo = titulo
        self.cant_canciones = cant_canciones

    def __str__(self):
        return f"Album:{self.titutlo} de {self.cant_canciones}"

    def __len__(self):
        return self.cant_canciones

    def __del__(self):
        print('emilinado')

mi_cd =  CD('GHTG','hgvdbfh',2)


del mi_cd

