# DICCIONARIOS-Y-LISTAS-PYTHON
natalia={'Nombre':'Natalia','EDAD':'19'}
print(natalia['Nombre'])
for key, nombre in natalia.items():
    print(key+" -" +nombre)

responses={}
while True:
    name = input("whats your name ")
    response=input("wich ountain would you like to climb someday")
    responses[name]= response
    repeat=input ("would you like to let another person respond(yes/no)")
    if repeat=='no':
        False
    for name ,response  in responses.items():
        print(name+response)
