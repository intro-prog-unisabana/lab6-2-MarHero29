datos = {"temp": 22.5, "color": "blue", "status": "ok"}
def temp_and_color(datos):
    temp=datos.get("temp")
    color=datos.get("color")
    return (temp,color)
print(temp_and_color(datos))
datos = {"status": "ok"}
print(temp_and_color(datos))