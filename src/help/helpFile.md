# HELP FILE

## Chemistry commands:

### -calculation of molar masses from the formula-
    *molecular_mass [formula]
    *molecular_mass NaOH

## -balancing chemical equations-
    *balance_equations [reactivos]=[productos]
    *balance_equations Al + HCl = AlCl3 + H2

## -calculating the concentration of a solution-
    *concentration parameters{[mst,vst,msc,vsc,eqsubstance,eqst,substance,molst]}
    *concentration mst=10g, vst=20ml, msc=30g, vsc=40ml, eqsubstance=2, substance=H2SO4

## -acid-base titration solver-
    *trition [c.pattern] [v.pattern] [v.sample] [n°OH(base)] [n°H(acid)] [A or B (the pattern is a base or an acid?)]
    *trition 0.1 10 10 1 1 a

## Math commands:

### -roots of a quadratic function-
    *quadratic_function [a][b][c]
    *quadratic_function 1 2 3

## Physics commands:

### -using the ideal gas equation of state-
    *ideal_gases parameters{[temperature][mol][pressure][volume]} [output unit]
    *ideal_gases v=22.4L, t=273.15K, n=1mol, to torr

## Other commands:

### -unit conversion-
    *convert_units [magnitud][unidad inicial]to[unidad final]
    *convert_units 30 kilojoule to joule

[Units system](https://github.com/hgrecco/pint/blob/master/pint/default_en.txt)