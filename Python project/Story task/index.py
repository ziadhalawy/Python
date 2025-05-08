

def run(distance, fuelRate):
    rate = fuelRate / 10

    for i in range(0,distance,10):
        fuelRate = fuelRate - rate
    return fuelRate
print(run(20, 100))