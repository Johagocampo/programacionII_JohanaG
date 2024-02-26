
class estudiante:
    def _init_ (self, nombre, apellido, identificacion, correo, celular):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.correo = correo
        self.celular = celular
    def obtenernombre(self):
        return f'Mi nombre es {self.nombre}'
    def obtenerapellido(self):
        return f'{self.apellido},'
    def obteneridentificacion(self):
        return f'\nMi identificacion es {self.identificacion}'
    def obtenercorreo(self):
        return f'\nMi correo es {self.correo}'
    def obtenercelular(self):
        return f'\nMi numero de celular es {self.celular}'

    e = ("Johana", "Gonzalez","1048439162","johagocampo31@outlook.com","3022594936")