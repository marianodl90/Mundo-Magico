from datetime import datetime



class Persona:
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        

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
       pass
       
    
    def eliminar_reserva(self):
       pass


