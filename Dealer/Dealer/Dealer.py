

from enum import Enum

class VirtualDealerState(Enum):
    Select = 0
    Quantity = 1
    Customize = 2
    Calculate = 3
    Update = 4
    Receipt = 5

class Brand(Enum):
    CAMRY = 0
    COROLLA = 1
    CROWN = 2
    GR86 = 3
    CHR = 4
    Mirai = 5
    Tacoma = 6
    Tundra = 7

class Cliente:
    def __init__(self, nombre, dolares):
        self.nombre = nombre
        self.dolares = dolares

class Carro:
    def __init__(self, modelo, year, inventario, precio, plate, transmission, color, asientos, aros):
        self.modelo = modelo
        self.year = year
        self.inventario = inventario
        self.precio = precio
        self.plate = plate
        self.transmission = transmission
        self.color = color
        self.asientos = asientos
        self.aros = aros

currentState = VirtualDealerState.Select

vendingmachine = [
    Carro(Brand.CAMRY, 0, 20, 26300, "", "", "", "", ""),
    Carro(Brand.COROLLA, 0, 20, 21700, "", "", "", "", ""),
    Carro(Brand.CROWN, 0, 20, 39950, "", "", "", "", ""),
    Carro(Brand.GR86, 0, 20, 27700, "", "", "", "", ""),
    Carro(Brand.CHR, 0, 20, 23150, "", "", "", "", ""),
    Carro(Brand.Mirai, 0, 20, 49500, "", "", "", "", ""),
    Carro(Brand.Tacoma, 0, 20, 28600, "", "", "", "", ""),
    Carro(Brand.Tundra, 0, 20, 57625, "", "", "", "", "")
]

autoSeleccionado = Carro(None, 0, 0, 0, "", "", "", "", "")
Jaychael = Cliente("Jaychael Colon", 900000)

while True:
    if currentState == VirtualDealerState.Select:
        print("Bienvenido al")
        print("Dealer Virtual Toyota \n")
        for i in range(8):
            print(vendingmachine[i].modelo.name, "tiene", vendingmachine[i].inventario, "autos, y cada cual cuesta", vendingmachine[i].precio)
        print("\n El cliente:")
        print(Jaychael.nombre, "tiene", Jaychael.dolares, "dolares en total. \n")
        print("<< fin de actualizacion >>\n")
        print("Seleccione el tipo de modelo que desea comprar de las opciones disponibles: ")
        print("CAMRY(0) = $26,300\nCOROLLA(1) = $21,700\nCROWN(2) = $39,950\nGR86(3) = $28,400\nCHR(4) = $23,150\nMIRAI(5) = $49,500\nTACOMA (6) = $28,600\nTUNDRA (7) = $57,625")
        autoElegido = int(input())
        
        if autoElegido == Brand.CAMRY.value:
            print("Haz elegido el CAMRY.")
            autoSeleccionado.modelo = Brand.CAMRY
            currentState = VirtualDealerState.Customize
        elif autoElegido == Brand.COROLLA.value:
            print("Haz elegido el COROLLA.")
            autoSeleccionado.modelo = Brand.COROLLA
            currentState = VirtualDealerState.Customize
        elif autoElegido == Brand.CROWN.value:
            print("Haz elegido el CROWN.")
            autoSeleccionado.modelo = Brand.CROWN
            currentState = VirtualDealerState.Customize
        elif autoElegido == Brand.GR86.value:
            print("Haz elegido el GR86.")
            autoSeleccionado.modelo = Brand.GR86
            currentState = VirtualDealerState.Customize
        elif autoElegido == Brand.CHR.value:
            print("Haz elegido el CHR.")
            autoSeleccionado.modelo = Brand.CHR
            currentState = VirtualDealerState.Customize
        elif autoElegido == Brand.Mirai.value:
            print("Haz elegido el Mirai.")
            autoSeleccionado.modelo = Brand.Mirai
            currentState = VirtualDealerState.Customize
        elif autoElegido == Brand.Tacoma.value:
            print("Haz elegido la Tacoma.")
            autoSeleccionado.modelo = Brand.Tacoma
            currentState = VirtualDealerState.Customize
        elif autoElegido == Brand.Tundra.value:
            print("Haz elegido la Tundra.")
            autoSeleccionado.modelo = Brand.Tundra
            currentState = VirtualDealerState.Customize
        else:
            print("Error! Selecciono un modelo invalido.")
            currentState = VirtualDealerState.Select
    
    elif currentState == VirtualDealerState.Customize:
        print("De que color desearia su vehiculo(s)?")
        color = input()
        print("De acuerdo, el color escogido fue:", color)
        print("Cual seria el estilo de transmision de su auto? (Manual o automatico)")
        transmission = input()
        print("Ha seleccionado el tipo de transmission:", transmission)
        print("Prefiere que sus asientos sean en cuero o platico?")
        asientos = input()
        print("Entendido, sus asientos seran en:", asientos)
        print("Cual color le gustaria para los aros?")
        aros = input()
        print("Los aros de su vehiculo seran:", aros)
        currentState = VirtualDealerState.Quantity
    
    elif currentState == VirtualDealerState.Quantity:
        print("Cuantos autos desea agregar a su orden?")
        orderQuantity = int(input())
        print("Su orden fue recibida exitosamente! Usted ordeno", orderQuantity, "autos.")
        
        if autoSeleccionado.modelo == Brand.CAMRY:
            if orderQuantity < 0 or orderQuantity > vendingmachine[0].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        elif autoSeleccionado.modelo == Brand.COROLLA:
            if orderQuantity < 0 or orderQuantity > vendingmachine[1].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        elif autoSeleccionado.modelo == Brand.CROWN:
            if orderQuantity < 0 or orderQuantity > vendingmachine[2].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        elif autoSeleccionado.modelo == Brand.GR86:
            if orderQuantity < 0 or orderQuantity > vendingmachine[3].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        elif autoSeleccionado.modelo == Brand.CHR:
            if orderQuantity < 0 or orderQuantity > vendingmachine[4].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        elif autoSeleccionado.modelo == Brand.Mirai:
            if orderQuantity < 0 or orderQuantity > vendingmachine[5].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        elif autoSeleccionado.modelo == Brand.Tacoma:
            if orderQuantity < 0 or orderQuantity > vendingmachine[6].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        elif autoSeleccionado.modelo == Brand.Tundra:
            if orderQuantity < 0 or orderQuantity > vendingmachine[7].inventario:
                print("No hay suficientes en el inventario disponible, disculpa.")
                currentState = VirtualDealerState.Select
                print("\n")
            else:
                currentState = VirtualDealerState.Calculate
        else:
            print("Cantidad invalida entrada. Error!")
    
    elif currentState == VirtualDealerState.Calculate:
        print("El costo total de su orden es:", end=" ")
        cost = 0
        
        if autoSeleccionado.modelo == Brand.CAMRY:
            cost = vendingmachine[0].precio * orderQuantity
        elif autoSeleccionado.modelo == Brand.COROLLA:
            cost = vendingmachine[1].precio * orderQuantity
        elif autoSeleccionado.modelo == Brand.CROWN:
            cost = vendingmachine[2].precio * orderQuantity
        elif autoSeleccionado.modelo == Brand.GR86:
            cost = vendingmachine[3].precio * orderQuantity
        elif autoSeleccionado.modelo == Brand.CHR:
            cost = vendingmachine[4].precio * orderQuantity
        elif autoSeleccionado.modelo == Brand.Mirai:
            cost = vendingmachine[5].precio * orderQuantity
        elif autoSeleccionado.modelo == Brand.Tacoma:
            cost = vendingmachine[6].precio * orderQuantity
        elif autoSeleccionado.modelo == Brand.Tundra:
            cost = vendingmachine[7].precio * orderQuantity
        else:
            print("Ocurrio un error, disculpa.")
        
        print(cost)
        print("Ingrese la cantidad a pagar:")
        payment = int(input())
        
        if payment > Jaychael.dolares or payment < cost or payment <= 0:
            print("No cuenta con los fondos actualmente para su orden!")
            currentState = VirtualDealerState.Select
            print("\n")
        else:
            Jaychael.dolares = Jaychael.dolares - payment
            change = payment - cost
            print("Gracias, el cambio de su orden es:", change, "dolares.")
            Jaychael.dolares = Jaychael.dolares + change
            currentState = VirtualDealerState.Update
    
    elif currentState == VirtualDealerState.Update:
        if autoSeleccionado.modelo == Brand.CAMRY:
            vendingmachine[0].inventario = vendingmachine[0].inventario - orderQuantity
        elif autoSeleccionado.modelo == Brand.COROLLA:
            vendingmachine[1].inventario = vendingmachine[1].inventario - orderQuantity
        elif autoSeleccionado.modelo == Brand.CROWN:
            vendingmachine[2].inventario = vendingmachine[2].inventario - orderQuantity
        elif autoSeleccionado.modelo == Brand.GR86:
            vendingmachine[3].inventario = vendingmachine[3].inventario - orderQuantity
        elif autoSeleccionado.modelo == Brand.CHR:
            vendingmachine[4].inventario = vendingmachine[4].inventario - orderQuantity
        elif autoSeleccionado.modelo == Brand.Mirai:
            vendingmachine[5].inventario = vendingmachine[5].inventario - orderQuantity
        elif autoSeleccionado.modelo == Brand.Tacoma:
            vendingmachine[6].inventario = vendingmachine[6].inventario - orderQuantity
        elif autoSeleccionado.modelo == Brand.Tundra:
            vendingmachine[7].inventario = vendingmachine[7].inventario - orderQuantity
        else:
            print("Error")
        
        print("El inventario ha sido actualizado exitosamente.")
        currentState = VirtualDealerState.Select
        print("\n")
    
    else:
        print("error estado invalido")


