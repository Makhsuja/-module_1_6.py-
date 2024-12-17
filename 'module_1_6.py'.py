my_dict = {'Anton': 2000, 'Sergey': 2002}
print(my_dict)
print(my_dict.get('Anton'), my_dict.get("Polina"))
my_dict.update({'Roma': 2006,
                'Grisha': 1998})
a = my_dict.pop('Anton')
print(my_dict)
print(a)


#Работа с множествами
my_set = {1,2,3,4,1,4,2,'Katya',2.6, 'Katya'}
print(my_set)
my_set.update({False,
               'cow'})
print(my_set.remove(2.6))
print(my_set )
