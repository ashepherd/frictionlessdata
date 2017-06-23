import datapackage

dp = datapackage.DataPackage('datapackage.json')
try:
    dp.validate()
except datapackage.exceptions.ValidationError as e:
    # Handle the ValidationError
    pass
