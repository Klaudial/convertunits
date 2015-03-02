
class length(object)
    def __init__(self, *args):
        Number = int(filter(str.isdigit, args))
        unit = int(filter(str.isalpha, args))
        
        if type(lead)==type(self):
...             # Copy constructor
...             self.Number=dict(int(filter(str.isdigit, args)).data)
...             self.unit=int(filter(str.isalpha, args)).coefficient





# at first, let's just do m and km
@extend(length)
... class length(object):
... 
...     def addunits(self, *others):
...         result_data=dict(self.data)
...         result_unit=self.unit
...         # Convert non metres to metres - except it doesn't, 'cos if you start in not metres, it doesn't work
...         others=map(units,others)
...         for another in others:
...             for unit, numbers in another.data.iteritems():
...                 if unit in result_data:
...                     result_data[numbers]+=another.data[numbers]
...                 elif unit == "km":
...                     result_data[numbers]+= 1000*another.data[numbers]
...                 elif unit == "cm":
                        result_data[numbers]+=another.data[numbers]/100
                    else:
                        raise TypeError("Please use a metric length with units m, cm or km!")
...         return units(result_data,result_unit)

        def __add__(self, other):
...         return self.addunits(other)