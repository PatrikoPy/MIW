def celsius_to(temp_C, temperature_type='kelvin'):
    if temp_C < -273.15:
        raise Exception("Wrong temp input")
    if temperature_type.lower() == "kelvin":
        return temp_C + 273.15
    elif temperature_type.lower() == "rankine":
        return temp_C * 1.8 + 491.67
    elif temperature_type.lower() == "fahrenheit":
        return temp_C * 9.0 / 5.0 + 32
    else:
        raise Exception("Wrong output temp type")

print(celsius_to(3))
print(celsius_to(3, temperature_type="rankine"))
print(celsius_to(3,temperature_type="Kelvin"))
print(celsius_to(3, temperature_type="fahrenheit"))

