# BotonAnimado
> Boton animado que aumenta levemente su tamaño durante unos instantes para luego volver a su tamaño original

## 1. ¿Donde puedo implemenarlo?
Es un boton genérico que puede ser implementado en casi cualquier app y ser ajustado facilmente

## 2. Metodos que incorpora
Metodo que cambia a un color aleatorio y activa la animacion cuando el boton es pulsado
~~~python
def pulsado(self):
        self.color=random.choice(self.colors)
        while(self.oldcolor==self.color):
            self.color=random.choice(self.colors)
        if self.anim_group.state() != QPropertyAnimation.Running:
            self.setStyleSheet(self.color)
        self.anim_group.start()
        self.oldcolor=self.color
        self.setText("pressed")
~~~ 
Metodo para ajustar el tamaño del boton de forma absoluta y otro de forma relativa
~~~python   
    def sizeHint(self):
        return QSize(60, 60)

    def AddsizeHint(self,a,b):
        return QSize(60+a, 60+b)
~~~
Propiedades que ajustan la duracion de la animación

~~~python
    
    @Property(int)
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion
~~~