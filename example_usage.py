import ASTM_Precision

data = {
    "method": "D4739",
    "analyte": "Base Number Fresh Oil",
    "data": [6.5, 6.4, 6.6]
}

analysis = ASTM_Precision.analyze(data)
print(analysis)
