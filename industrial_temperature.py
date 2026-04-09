def trigger_alarm(temperatures, threshold=80):
    alarmas = []
    for sensores, temp in temperatures.items():
        if temp>threshold:
            alarmas.append(sensores)
            
    return alarmas