#convert_units 30 cm to m
def convert_units(arguments):
    import pint

    x = pint.Quantity(float(arguments[0]),str(arguments[1]))

    try:
        z = x.to(arguments[3])
        return z
    except pint.errors.DimensionalityError:
        return f"No puede pasar de {arguments[1]} a {arguments[3]}"