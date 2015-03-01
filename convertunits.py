
class length(object)
    def __init__(self, *args):
        number = int(filter(str.isdigit, args))

#class units(length)



# at first, let's just do m and km
@extend(units)
... class units(Length):
... 
...     def addunits(self, *others):
...         result_data=dict(self.data)
...         result_unit=self.unit
...         # Convert non metres to metres
...         others=map(units,others)
...         for another in others:
...             for unit, symbol, exponent in another.data.iteritems():
...                 if unit in result_data:
...                     result_data[number]+=another.data[number]
...                 elif unit == "km":
...                     result_data[number]+= 1000*another.data[number]
...                 elif unit == "cm":
                        result_data[number]+=another.data[number]/100
...         return units(result_data,result_unit)