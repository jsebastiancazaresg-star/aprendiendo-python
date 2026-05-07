# Variable multiple
nombre_completo=("Sebastian","Cazares",13, "Houston", "Texas")
#print(type(nombre_completo))
# usuario=("Cazador123","12345678")\
#caja_1=usuario[0]
#caja_2=usuario[1]
#print(caja_1)
#print(caja_2)
#desempaquetado de tupla
#var_1,var_2=usuario[0],usuario[1]
#print(var_1)
#print(var_2)
#var_1,var_2=usuario
#print(var_1)
#print(var_2)
'''
variable1=nombre_completo[0]
variable2=nombre_completo[1]
variable3=nombre_completo[2]
print(variable1)
print(variable2)
print(variable3)
'''
#para desempaquetar una tupla debo de crear la misma candidad de variables que tiene la tupla, de lo contrario maracara error 
var1, var2, _, _, var5 =nombre_completo
print(var1)
print(var2)
print(var5)