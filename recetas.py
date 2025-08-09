from doctores import Doctor
from pacientes import Paciente

class Receta:
    def __init__(self, receta_id, paciente, doctor, medicacion):
        self.receta_id = receta_id
        self.paciente = paciente
        self.doctor = doctor
        self.medicacion = medicacion

    def detalles(self):
        return(
            f"Receta {self.receta_id}: paciente {self.paciente.nombre},"
            f"Doctor {self.doctor.nombre}, medicacion: {','.join(self.medicacion)}"
        )
    
if __name__ =="__main__":
    doc = Doctor(101, "Garcia", "Cardiologia")
    p = Paciente(501, "Maria", 45)
    r = Receta(9001, p, doc, ["Aspirina", "Vitamina C"])
    print(r.detalle())