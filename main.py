from machine import Pin
import time
import _thread
import connection

connection.connect_wifi()

# --- LED automático (parpadea solo) ---
led_auto = Pin(2, Pin.OUT)

# --- LED que depende del botón ---
led_boton = Pin(5, Pin.OUT)

# --- Botón con pull-up interno ---
boton = Pin(4, Pin.IN, Pin.PULL_UP)

boton2 = Pin(18, Pin.IN, Pin.PULL_UP)
prev_boton2 = 1  

# --- HILO PARA EL PARPADEO AUTOMÁTICO ---
def parpadeo():
    while True:
        led_auto.value(1)
        time.sleep(0.5)
        led_auto.value(0)
        time.sleep(0.5)

_thread.start_new_thread(parpadeo, ())

# --- BUCLE PRINCIPAL (BOTÓN) ---
while True:
    if boton.value() == 1:
        #print("Boton encendido")# Botón presionado (va a GND)
        led_boton.value(1)       # Enciende LED
    else:
        #print("Boton apagado")
        led_boton.value(0)       # Apaga LED

    time.sleep(0.01)
    
    valor_b2 = boton2.value()
    
    if prev_boton2 == 1 and valor_b2 == 0:
        print("Botón 2 PRESIONADO")  
    prev_boton2 = valor_b2
