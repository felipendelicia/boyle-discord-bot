#importing modules
import chempy
from chempy import chemistry
import pint

def molecularmass(formule):
    return str(chempy.Substance.from_formula(formule).unicode_name) + " = "+str(chemistry.Substance.from_formula(formule).molar_mass())

def balancereactions(reactives, products):
    a,b = chempy.chemistry.balance_stoichiometry(set(reactives),set(products))
    return str(chempy.chemistry.Reaction(a,b))

def concentration(dictionary):
    result = []

    #N
    if "substance" in dictionary and "mst" in dictionary and "vsc" in dictionary and "eqsubstance" in dictionary or "eqst" in dictionary and "vsc" in dictionary:
        if "mst" in dictionary:
            equivalents = (pint.Quantity(float(dictionary["mst"][0]),str(dictionary["mst"][1])).to("g").magnitude)*(float(dictionary["eqsubstance"][0])/chemistry.Substance.from_formula(dictionary["substance"]).molar_mass().magnitude)
            solution_volume = pint.Quantity(float(dictionary["vsc"][0]),str(dictionary["vsc"][1])).to("L").magnitude
            Normality = str(str(equivalents/solution_volume) + " equivalents/liter N")
            result.append(Normality)
        else:
            equivalents = float(dictionary["eqst"][0])
            solution_volume = pint.Quantity(float(dictionary["vsc"][0]),str(dictionary["vsc"][1])).to("L").magnitude
            Normality = str(str(equivalents/solution_volume) + " equivalents/liter N")
            result.append(Normality)

    #M
    if "substance" in dictionary and "mst" in dictionary and "vsc" in dictionary or "molst" in dictionary and "vsc" in dictionary:
        if "mst" in dictionary:
            moles = pint.Quantity((pint.Quantity(float(dictionary["mst"][0]),str(dictionary["mst"][1])).to("g").magnitude)/(chemistry.Substance.from_formula(dictionary["substance"]).molar_mass().magnitude),"mol")
            solution_volume = pint.Quantity(float(dictionary["vsc"][0]),str(dictionary["vsc"][1])).to("L")
            Molarity = str(moles/solution_volume) + " M" 
            result.append(Molarity)
        else:
            moles = pint.Quantity(float(dictionary["molst"][0]),str(dictionary["molst"][1])).to("mole")
            solution_volume = pint.Quantity(float(dictionary["vsc"][0]),str(dictionary["vsc"][1])).to("L")
            Molarity = str(moles/solution_volume) + " M"
            result.append(Molarity)

    #%m/m
    if "mst" in dictionary and "msc" in dictionary:
        solute_mass = pint.Quantity(float(dictionary["mst"][0]),str(dictionary["mst"][1])).to("g")
        solution_mass = pint.Quantity(float(dictionary["msc"][0]),str(dictionary["msc"][1])).to("g")
        
        #%m/m = st/sc .100
        percentaje_mm = str(((solute_mass/solution_mass)*100).magnitude) + " %(m/m)"

        result.append(percentaje_mm)

    #%m/v and ppm
    if "mst" in dictionary and "vsc" in dictionary:
        solute_mass = pint.Quantity(float(dictionary["mst"][0]),str(dictionary["mst"][1]))
        solution_volume = pint.Quantity(float(dictionary["vsc"][0]),str(dictionary["vsc"][1]))

        #%m/v:
        percentaje_mv = str(((solute_mass.to("g")/solution_volume.to("ml"))*100).magnitude) + " %(m/v)"
        result.append(percentaje_mv)
        #ppm
        ppm = str(solute_mass.to("mg")/solution_volume.to("L")) + " ppm"
        result.append(ppm)
    #%v/v
    if "vst" in dictionary and "vsc" in dictionary:
        solute_volume = pint.Quantity(float(dictionary["vst"][0]),str(dictionary["vst"][1])).to("ml")
        solution_volume = pint.Quantity(float(dictionary["vsc"][0]),str(dictionary["vsc"][1])).to("ml")
        percentaje_vv = str(((solute_volume/solution_volume)*100).magnitude) + " %(v/v)"
        result.append(percentaje_vv)
    
    return result

def trition(cpatron, vpatron, vmuestra, nOH, nH, AB): # {entry} ---> *trition <c. sc patron><v. patron><v. muestra><n° OH><n° H><B or A (patron)>
	#If patron solution is an acid
	if AB.lower() == "a":
		concentration = (float(nOH)*float(cpatron)*float(vpatron))/(float(nH)*float(vmuestra))
		return concentration

	#If the patron solution is a base
	elif AB.lower() == "b":
		concentration = (float(nH)*float(cpatron)*float(vpatron))/(float(nOH)*float(vmuestra))
		return concentration

	#If the user has a type error
	else:
		return "Especificá bien si el patron se trata de un acido o de una base!"