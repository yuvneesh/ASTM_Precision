# ASTM Precision

Published ASTM Standards for laboratory testing generally contain the precision information about the test method. Repeatability and Reproducibility are the common parameters. These provide the maximum difference among multiple test results for the sample for 95% of the samples.


# Scope

The purpose of this project is to compile the repeatability and reproducibility data for common tests associated with Oil Analysis and provide a precision statement for a given dataset.

# Example Usage
```
>>> import ASTM_Precision
>>> data = {"method": "D4739", "analyte": "Base Number Fresh Oil", "data": [6.1, 6, 6.3]}
>>> report = ASTM_Precision.analyze(data)
>>> print(report)
All datapoints are valid
```
