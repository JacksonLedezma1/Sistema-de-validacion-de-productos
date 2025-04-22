#Sistema de validación de productos
NombreP=[]
PrecioU=[]
CantidadP=[]
DescuentoP=[]
Precio_con_descuento=[]
Precio_sin_descuento=[]
total=0

#Funcion para calcular precios
def Calcular_Total(Npro, PrecioU, CantidadP, DescuentoP):
    for i in range(Npro):
        #precio sin descuento
        Precios=PrecioU[i]*CantidadP[i]
        Precio_sin_descuento.append(Precios)

        #precio con descuento
        precioD=Precios*(DescuentoP[i]/100)
        Preciof=Precios-precioD
        Precio_con_descuento.append(Preciof)

    return Precio_sin_descuento, Precio_con_descuento

#Introducir cuantos productos va a agregar
Npro=int(input("\nIngrese el numero de productos a agregar: "))
#Prevenir ingresar numeros incorrectos
while Npro < 0:
    print("\nCantidad invalida, por favor ingrese un numero valido.")
    Npro=int(input("Ingrese el numero de productos a agregar: "))

for i in range(Npro):
    print(f"\nProducto #{i+1}")
    #pedir nombre del producto
    nombre=str(input(f"\nIngrese el nombre del producto: "))
    NombreP.append(nombre)
    #pedir valor del producto
    precio=float(input(f"\nIngrese el precio unitario del producto: "))
    PrecioU.append(precio)
    #validacion de entrada
    while precio < 0:
        print("\nNo existen precios negativos")
        precio=float(input(f"Ingrese el precio unitario del producto: "))
        PrecioU.append(precio) 
    #pedir cantidad del producto
    cantidad=int(input(f"\nIngrese la cantidad de producto: "))
    CantidadP.append(cantidad)
    #validacion de entrada
    while cantidad < 1:
        print("\nNo puedes agregar menos de 1 producto")
        cantidad=float(input(f"Ingrese la cantidad de producto: "))
        CantidadP.append(cantidad) 
    #pedir el descuento
    Descuento=float(input(f"\nIngrese el % de descuento del producto: "))
    DescuentoP.append(Descuento)
    #validacion de entrada
    while Descuento < 0 and Descuento > 100:
        print("\nError, los descuentos son entre 0% y 100%")
        Descuento=float(input(f"Ingrese el % de descuento del producto: "))
        DescuentoP.append(Descuento)

Precio_sin_descuento, Precio_con_descuento = Calcular_Total(Npro, PrecioU, CantidadP, DescuentoP)

print("\nLista de productos:")
for i in range(Npro):
    print(f"\nProducto #{i+1}")
    print(f"Nombre: {NombreP[i]}")
    print(f"Precio sin descuento: ${Precio_sin_descuento[i]}")
    if DescuentoP[i]>0:
        print(f"Precio Con descuento: ${Precio_con_descuento[i]}")
        total=Precio_con_descuento[i]+total
    else:
        print("No aplica descuento")
        total=Precio_sin_descuento[i]+total


print(f"\nEl precio total es: ${total}")
