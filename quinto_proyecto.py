
def suma(num1, *args, **kwargs):
   print(num1)
   print(args)
   total = 0
   for clave, value in kwargs.items():
       print(f"{clave} = {value}")
       total += value
   return total

print(suma(5, "cele",1,2,3, x=3,y=2,z=4))