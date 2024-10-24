my_dict = {'Anton': 2000, 'Sergey': 2002}
print(my_dict)
print(my_dict['Anton'])
my_dict['Max'] = 1999
print(my_dict)
print(my_dict['Max'])
my_dict.update({'Roma': 2006,
                'Grisha': 1998})
print(my_dict)
del my_dict['Max']
print(my_dict)
print(my_dict.get('Max'))
my_set = {1,2,3,4,1,4,2,'Katya',2.6, 'Katya'}
print(my_set )
my_set.update({5,
               'cow'})
print(my_set )
print(my_set.discard(5))
print(my_set)
