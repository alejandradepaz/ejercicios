from machine import Pin, Timer
import time
import connection

# Conectar WiFi (solo una vez)
connection.connect_wifi()

# Pines
led_auto = Pin(2, Pin.OUT)     # LED que parpadea automáticamente
led_boton = Pin(5, Pin.OUT)    # LED controlado por el botón
boton = Pin(4, Pin.IN, Pin.PULL_UP)  # Botón con resistencia pull-up

# --- PARPADEO AUTOMÁTICO USANDO TIMER ---
def parpadear(timer):
    led_auto.value(not led_auto.value())  # Cambia de encendido a apagado cada vez

# Timer para el LED automático
timer = Timer(0)
timer.init(period=500, mode=Timer.PERIODIC, callback=parpadear)

# --- BUCLE PRINCIPAL ---
while True:
    if boton.value() == 0:  # LOW significa que el botón está presionado
        led_boton.value(1)
        print("Botón presionado")
    else:
        led_boton.value(0)
    time.sleep(0.05)  # pequeño retardo para evitar lecturas muy rápidas
