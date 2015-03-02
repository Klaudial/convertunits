
class length(object)
    def __init__(self, *args):
        Number = int(filter(str.isdigit, args))
        unit = int(filter(str.isalpha, args))
        
        if type(lead)==type(self):
...             # Copy constructor
...             self.data=dict(lead.data)
...             self.coefficient=lead.coefficient




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
...             for unit, number in another.data.iteritems():
...                 if unit in result_data:
...                     result_data[number]+=another.data[number]
...                 elif unit == "km":
...                     result_data[number]+= 1000*another.data[number]
...                 elif unit == "cm":
                        result_data[number]+=another.data[number]/100
                    else:
                        raise error "Please use a metric length with units m, cm or km!"
...         return units(result_data,result_unit)

        def __add__(self, other):
...         return self.addunits(other)