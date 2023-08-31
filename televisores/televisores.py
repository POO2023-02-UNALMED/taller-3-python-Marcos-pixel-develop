

class Marca:
    def __init__(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def setCanal(self, canal):
        if self._tv:
            self._tv.setCanal(canal)

    def setVolumen(self, volumen):
        if self._tv:
            self._tv.setVolumen(volumen)

    def turnOn(self):
        if self._tv:
            self._tv.turnOn()

    def turnOff(self):
        if self._tv:
            self._tv.turnOff()

    def canalUp(self):
        if self._tv:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv:
            self._tv.canalDown()

    def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()

    def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()

    def getTV(self):
        return self._tv

class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.numTV += 1

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca

    def setCanal(self, canal):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    def getCanal(self):
        return self._canal

    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio

    def setVolumen(self, volumen):
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    def getVolumen(self):
        return self._volumen

    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._estado and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self._estado and self._canal > 1:
            self._canal -= 1

    def volumenUp(self):
        if self._estado and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self):
        if self._estado and self._volumen > 0:
            self._volumen -= 1

