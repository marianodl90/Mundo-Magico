from datetime import datetime



class Persona:
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        

class Reserva:
    def __init__(self, fecha, plaza:str, direccion:str, seña:int):
        self.fecha = datetime(*fecha)
        self.plaza = plaza
        self.direccion = direccion
        self.seña = seña
        
    def __str__(self):
        fecha_formateada = self.fecha.strftime('%d/%m/%Y %H:%M')
        return f"Se reservo {self.plaza} el dia {fecha_formateada} en la dirección {self.direccion}, y se pago de seña {self.seña} pesos"
    

class Cliente (Persona):
    def __init__(self, nombre:str, apellido:str, telefono:int):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.reservas = []
  
    def __str__(self):
         print(f"Reserva realizada \nEl nombre del cliente es {self.nombre} {self.apellido}, y su telefono es {self.telefono}") 

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
        
    def mostrar_reserva(self):
      
       
    
    def eliminar_reserva(self):
       pass


