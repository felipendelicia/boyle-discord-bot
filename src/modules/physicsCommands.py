import pint
def ideal_gases(parameters_dic, output_unit): #*ideal_gases parameters{[temperature][mol][pressure][volume]} [output unit]
    r = 0.08205746
    parameters_units = list(parameters_dic.keys())

    print(parameters_units)

    if "t" in parameters_units:
        tem = pint.Quantity(float(parameters_dic["t"][0]),parameters_dic["t"][1]).to("K").magnitude
        print(tem)

    if "n" in parameters_units:
        mol = pint.Quantity(float(parameters_dic["n"][0]),parameters_dic["n"][1]).to("mol").magnitude
        print(mol)

    if "v" in parameters_units:
        vol = pint.Quantity(float(parameters_dic["v"][0]),parameters_dic["v"][1]).to("L").magnitude
        print(vol)

    if "p" in parameters_units:
        pre = pint.Quantity(float(parameters_dic["p"][0]),parameters_dic["p"][1]).to("atmosphere").magnitude
        print(pre)

    if "p" in parameters_units and "t" in parameters_units and "v" in parameters_units: #pv/rt = n
        return str(pint.Quantity(float((pre*vol)/(r*tem)),"mole").to(output_unit))

    if "n" in parameters_units and "v" in parameters_units and "p" in parameters_units: #t = pv/rn
        return str(pint.Quantity(float((pre*vol)/(r*mol)),"K").to(output_unit))

    if "t" in parameters_units and "n" in parameters_units and "v" in parameters_units: #nrt/v = p
        return str(pint.Quantity(float((mol*tem*r)/(vol)),"atm").to(output_unit))

    if "p" in parameters_units and "t" in parameters_units and "n" in parameters_units: #nrt/p = v
        return pint.Quantity(float((mol*tem*r)/(pre)),"L").to(output_unit)
