import os
import socket
from playsound import playsound
from plyer import notification
import time

def check_connection():
    estado_anterior = None
    while True:
        estado_actual = False
        try:
            for i in range(3):
                ping_result = os.system("ping -c 1 8.8.8.8")
                if ping_result == 0:
                    estado_actual = True
                    break
                time.sleep(2.5)
            if estado_actual != estado_anterior:
                estado_anterior = estado_actual
                if estado_actual:
                    playsound("alerta.wav", block=False)
                    notification.notify(title="Check Connection",
                                        message="Conectado a Internet",
                                        app_name="Check Connection",
                                        timeout=10)
                else:
                    playsound("alerta.wav", block=False)
                    notification.notify(title="Check Connection",
                                        message="Se ha perdido la conexión a Internet",
                                        app_name="Check Connection",
                                        timeout=10)
        except socket.gaierror:
            if estado_anterior != False:
                playsound("alerta.wav", block=False)
                notification.notify(title="Check Connection",
                                    message="Se ha perdido la conexión a Internet",
                                    app_name="Check Connection",
                                    timeout=10)
            estado_anterior = False
        time.sleep(10)
check_connection()