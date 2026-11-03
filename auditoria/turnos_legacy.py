import requests
import yaml

turnos = []
config = yaml.load(open("config.yml"))


def procesar_turno(nombre, edad, obra_social, urgente, especialidad):
    if nombre != None and nombre != "":
        if edad > 0:
            if obra_social == "OSDE":
                print("Paciente premium")
                if urgente == True:
                    prioridad = 1
                else:
                    prioridad = 2
            elif obra_social == "SWISS":
                print("Paciente premium")
                if urgente == True:
                    prioridad = 1
                else:
                    prioridad = 2
            elif obra_social == "PUBLICA":
                print("Paciente publico")
                if urgente == True:
                    prioridad = 2
                else:
                    prioridad = 3
            else:
                prioridad = 3
            if especialidad == "cardiologia" or especialidad == "neurologia":
                if edad > 65:
                    prioridad = prioridad - 1
            turno = nombre + "-" + str(edad) + "-" + obra_social + "-" + str(prioridad)
            if urgente == True:
                turno = turno + "-URGENTE"
            turnos.append(turno)
            requests.post(config["url_notificaciones"], data={"turno": turno})
            return turno
    return None


def reprogramar_turno(nombre, edad, obra_social, urgente, especialidad, fecha):
    if nombre != None and nombre != "":
        if edad > 0:
            if obra_social == "OSDE":
                print("Paciente premium")
                if urgente == True:
                    prioridad = 1
                else:
                    prioridad = 2
            elif obra_social == "SWISS":
                print("Paciente premium")
                if urgente == True:
                    prioridad = 1
                else:
                    prioridad = 2
            elif obra_social == "PUBLICA":
                print("Paciente publico")
                if urgente == True:
                    prioridad = 2
                else:
                    prioridad = 3
            else:
                prioridad = 3
            if especialidad == "cardiologia" or especialidad == "neurologia":
                if edad > 65:
                    prioridad = prioridad - 1
            turno = nombre + "-" + str(edad) + "-" + obra_social + "-" + str(prioridad)
            turno = turno + "-" + fecha
            if urgente == True:
                turno = turno + "-URGENTE"
            turnos.append(turno)
            requests.post(config["url_notificaciones"], data={"turno": turno})
            return turno
    return None
