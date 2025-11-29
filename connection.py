import network
import time

def connect_wifi():
    ssid = "CasaMax"
    password = "A6R9N2J4Y9K2"
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        print("Ya estabas conectado.")
        print("IP:", wlan.ifconfig())
        return wlan

    print("Conectando a WiFi...")
    wlan.connect(ssid, password)

    timeout = 30  # segundos
    start = time.time()

    while not wlan.isconnected():
        if time.time() - start > timeout:
            print("No se pudo conectar (timeout).")
            return None
        time.sleep(0.5)

    print("Conectado exitosamente.")
    print("IP:", wlan.ifconfig())
    return wlan