"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, n ame, price, category, stock]
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from os import system
from time import sleep
import datetime

'''-----LISTA DE 5 PRODUCTOS CON MAYORES VENTAS-----'''
def top_sales_product():
    #Diccionario con los id por producto
    product_id = {}
    for product in lifestore_products:
        id_product = product[0]
        name = product[1]
        if name not in product_id.keys():
            product_id[name] = []
        product_id[name].append(id_product)

    #Diccionario con las ventas(unidades) por id
    product_sales = {}
    for sales in lifestore_sales:
        id_product_sales = sales[1]
        refund = sales[4]
        if id_product_sales not in product_sales.keys():
            product_sales[id_product_sales] = []
        product_sales[id_product_sales].append(refund)
        #Si la venta tuvo devolución, entonces no se toma en cuenta
        if refund != 0:
            product_sales[id_product_sales].remove(1)

    #Diccionario con el total de ventas(unidades) por cada producto
    #Asignación de ventas y ganancias a cada producto por medio del ID. 
    product_results = {}
    for name, list_id in product_id.items():
        total_sales = 0
        total_profit = 0
        for id_product_sales in list_id:
            if id_product_sales not in product_sales.keys():
                continue
            no_refund_sales = product_sales[id_product_sales]
            price = lifestore_products[id_product_sales-1][2]
            sales_amount = len(no_refund_sales)

            profit_amount = price*sales_amount

            total_sales += sales_amount
            total_profit += profit_amount

            #Si se imprime aquí dentro solo serían los vendidos
        
        #Si se imprime afuera serían todos los productos
        product_results[name] = {
        'ID': id_product_sales,  
        'Total Sales': total_sales,
        'Total Profit': total_profit }

    #Ordenando el diccionario resultante
    product_results_ord = sorted(product_results.items(), key = lambda x: x[1]['Total Sales'], reverse= True)
    print(f'\n\t\tLISTA DE LOS 5 PRODUCTOS CON MAYORES VENTAS')
    print(f'|ID| \t\t Nombre del Producto \t Unidades Vendidas (u) \t Ganancia Total ($)')

    #Imprimiendo solo 5 productos
    for product, attributes in product_results_ord[0:5]: #Lista
        print(f'{attributes["ID"]} \t {product[0:30]} \t {attributes["Total Sales"]} \t\t\t {attributes["Total Profit"]} ')


'''-----LISTA DE 10 PRODUCTOS CON MAYORES BÚSQUEDAS-----'''
def top_searches_product():
    #Diccionario con el id por producto
    product_id = {}
    for product in lifestore_products:
        id_product = product[0]
        name = product[1]
        if name not in product_id.keys():
            product_id[name] = []
        product_id[name].append(id_product)

    #Diccionario con las busquedas(cantidad) por id
    product_searches = {}
    for searches in lifestore_searches:
        id_product_searches = searches[1]
        search = searches[0]
        if id_product_searches not in product_searches.keys():
            product_searches[id_product_searches] = []
        product_searches[id_product_searches].append(search)

    #Diccionario con el total de busquedas por cada producto 
    #Asignación de busquedas a cada producto por medio del ID
    searches_results = {}
    for name, list_id in product_id.items():
        total_searches = 0
        for id_product_searches in list_id:
            if id_product_searches not in product_searches.keys():
                continue
            search_list_lifestore = product_searches[id_product_searches]
            search_amount = len(search_list_lifestore)
            total_searches += search_amount
        
        searches_results[name] = {
        'ID': id_product_searches,  
        'Total Searches': total_searches,
        }

    #Ordenando el diccionario de búsquedas resultante
    searched_results_ord = sorted(searches_results.items(), key = lambda x: x[1]['Total Searches'], reverse= True)
    print(f'\n\tLISTA DE LOS 10 PRODUCTOS CON MAYORES BUSQUEDAS')
    print(f'|ID| \t\t Nombre del Producto \t\t Busquedas Totales ')

    #Imprimiendo solo 10 productos
    for product, attributes in searched_results_ord[0:10]: #Lista
        print(f'{attributes["ID"]} \t {product[0:30]} \t\t {attributes["Total Searches"]}')


'''-----LISTA DE PRODUCTOS CON MENORES VENTAS POR CATEGORÍA-----'''
def category_bottom_sales():
    #Diccionario con los nombres por categoría
    category_product = {}
    for product in lifestore_products:
        name = product[1]
        category = product[3]
        if category not in category_product.keys():
            category_product[category] = []
        category_product[category].append(name)

    #Diccionario con los id por producto
    product_id = {}
    for product in lifestore_products:
        id_product = product[0]
        name = product[1]
        if name not in product_id.keys():
            product_id[name] = []
        product_id[name].append(id_product)

    #Diccionario con las ventas(unidades) por id
    #En este diccionario se eliminan las ventas con devolución
    product_sales = {}
    for sales in lifestore_sales:
        id_product_sales = sales[1]
        refund = sales[4]
        if id_product_sales not in product_sales.keys():
            product_sales[id_product_sales] = []
        product_sales[id_product_sales].append(refund)
        if refund != 0:
            product_sales[id_product_sales].remove(1)

    #Diccionario con el total de ventas(unidades) por cada producto
    #Asignación de ventas y ganancias a cada producto por medio del ID.
    #Name: Id ----> Id : Sales 
    product_results = {}
    for name, list_id in product_id.items():
        total_sales = 0
        total_profit = 0
        for id_product_sales in list_id:
            if id_product_sales not in product_sales.keys():
                continue
            no_refund_sales = product_sales[id_product_sales]
            price = lifestore_products[id_product_sales-1][2]
            sales_amount = len(no_refund_sales)

            profit_amount = price*sales_amount

            total_sales += sales_amount
            total_profit += profit_amount
        
        product_results[name] = {
        'ID': id_product_sales,  
        'Total Sales': total_sales,
        'Total Profit': total_profit }

    #Diccionario con el total de productos por cada categoría
    #División de productos por categpría por medio del nombre,
    # Category:Name ----> Name:Id
    category_results = {}
    for cat, list_name in category_product.items():
        names_product = []
        for name in list_name:
            if name not in product_results.keys():
                continue
            names_product.append([name[0:30],product_results[name]])

        category_results[cat] = {
        'Name' : names_product }

    #Indagando en el diccionario para imprimir la categoría y
    #los atributos de cada producto (ID, Ventas y Ganancias)
    print(f'\n\t\t\tLISTA DE 5 PRODUCTOS CON MENORES VENTAS POR CATEGORÍA')
    print(f'|ID| \t\t Nombre del Producto \t\t Unidades Vendidas (u) \t\t Ganancia Total ($)')
    for categories, attributes in category_results.items():
        print(f'\nCategoría: {categories.upper()}')
        for key, list_product in attributes.items():
            #Imprimiendo solo 5 productos
            list_product = sorted(list_product, key = lambda x: x[1]['Total Sales'], reverse= False)
            for product_name, attr in list_product[0:5]:
                #if attr["Total Sales"] != 0:
                        print(f'{attr["ID"]} \t {product_name} \t\t {attr["Total Sales"]} \t\t\t\t {attr["Total Profit"]} ')


'''-----LISTA DE PRODUCTOS CON MENORES BÚSQUEDAS POR CATEGORÍA-----'''
def category_bottom_searches():
    #Diccionario con los nombres por categoría
    category_product = {}
    for product in lifestore_products:
        name = product[1]
        category = product[3]
        if category not in category_product.keys():
            category_product[category] = []
        category_product[category].append(name)

    #Diccionario con los id por producto
    product_id = {}
    for product in lifestore_products:
        id_product = product[0]
        name = product[1]
        if name not in product_id.keys():
            product_id[name] = []
        product_id[name].append(id_product)

    #Diccionario con las ventas(unidades) por id
    #En este diccionario se eliminan las ventas con devolución
    product_searches = {}
    for searches in lifestore_searches:
        id_product_searches = searches[1]
        search = searches[0]
        if id_product_searches not in product_searches.keys():
            product_searches[id_product_searches] = []
        product_searches[id_product_searches].append(search)

    #Diccionario con el total de ventas(unidades) por cada producto
    #Asignación de ventas y ganancias a cada producto por medio del ID
    #Name: Id ----> Id : Sales 
    searches_results = {}
    for name, list_id in product_id.items():
        total_searches = 0
        for id_product_searches in list_id:
            if id_product_searches not in product_searches.keys():
                continue
            search_list_lifestore = product_searches[id_product_searches]
            search_amount = len(search_list_lifestore)
            total_searches += search_amount
        
        searches_results[name] = {
        'ID': id_product_searches,  
        'Total Searches': total_searches,
        }

    #Diccionario con el total de productos por cada categoría
    #División de productos por categpría por medio del nombre,
    # Category:Name ----> Name:Id
    category_results = {}
    for cat, list_name in category_product.items():
        names_product = []
        for name in list_name:
            if name not in searches_results.keys():
                continue
            names_product.append([name[0:30],searches_results[name]])

        category_results[cat] = {
        'Name' : names_product }

    #Indagando en el diccionario para imprimir la categoría y
    #los atributos de cada producto (ID y Búsquedas)
    print(f'\n\tLISTA DE 10 PRODUCTOS CON MENORES BÚSQUEDAS POR CATEGORÍA')
    print(f'|ID| \t\t Nombre del Producto \t\t Busquedas Totales ')
    for categories, attributes in category_results.items():
            print(f'\nCategoría: {categories.upper()}')
            for key, list_product in attributes.items():
            #Imprimiendo solo 10 productos
                list_product = sorted(list_product, key = lambda x: x[1]['Total Searches'], reverse= False)
                for product_name, attr in list_product[0:10]:
                    print(f'{attr["ID"]} \t {product_name} \t\t {attr["Total Searches"]}')


'''------- LISTAS DE LAS MEJORES Y PEORES RESEÑAS --------'''
def product_review():
    #Diccionario con los id por producto
    product_id = {}
    for product in lifestore_products:
        id_product = product[0]
        name = product[1]
        if name not in product_id.keys():
            product_id[name] = []
        product_id[name].append(id_product)

    #Diccionario con las reseñas por id
    product_review = {}
    for reviews in lifestore_sales:
        id_product_review = reviews[1]
        review = reviews[2]
        if id_product_review not in product_review.keys():
            product_review[id_product_review] = []
        product_review[id_product_review].append(review)

    #Diccionario con el total de reviews por cada producto
    #Asignación de ventas, ganancias y review promedio a cada producto por medio del ID
    review_results = {}
    for name, list_id in product_id.items():
        total_review = []
        total_sales = 0
        total_profit = 0
        for id_product_review in list_id:
            if id_product_review not in product_review.keys():
                continue
            no_refund_sales = product_review[id_product_review]
            price = lifestore_products[id_product_review-1][2]
            sales_amount = len(no_refund_sales)

            profit_amount = price*sales_amount

            total_sales += sales_amount
            total_profit += profit_amount

            no_review_sales = product_review[id_product_review]
            total_review += no_review_sales
            #Si se imprime aquí dentro solo serían los vendidos
            
            #Calculando la review promedio por producto
            prom = sum(total_review)/len(total_review)
            prom_round = round(prom,2)

        #Si se imprime afuera serían todos los productos
        review_results[name] = {
        'ID': id_product_review,
        'Total Sales': total_sales,
        'Total Profit': total_profit,  
        'Total Review': prom_round }

    ##LISTAS MEJORES Y PEORES REVIEWS 
    '''----------------------------------------------------------------------------------------------'''

    #Ordenando el diccionario de MEJOR REVIEW a PEOR REVIEW, sin tomar en cuenta la cantidad de ventas
    product_results_ord = sorted(review_results.items(), key = lambda x: x[1]['Total Review'], reverse= True)
    print(f'\n\t\t\t\tLISTA DE LOS 5 PRODUCTOS CON MEJORES RESEÑAS ')
    print(f'|ID| \t\t Nombre del Producto \t Reseña Promedio \t Unidades Vendidas (u) \t Ganancia Total ($)')

    #Imprimiendo solo 5 productos
    #Se propone que el producto tenga mas de dos ventas para que se considere su reseña promedio
    for product, attributes in product_results_ord[0:20]: #Lista
        if attributes['Total Sales'] != 0 and attributes['Total Sales'] > 2 :
            print(f'{attributes["ID"]} \t {product[0:30]} \t {attributes["Total Review"]} \t\t\t {attributes["Total Sales"]} \t\t\t {attributes["Total Profit"]} ')

    #Ordenando el diccionario de PEOR REVIEW a MEJOR REVIEW, sin tomar en cuenta la cantidad de ventas
    product_results_ord = sorted(review_results.items(), key = lambda x: x[1]['Total Review'], reverse= False)
    print(f'\n\t\t\t\tLISTA DE LOS 5 PRODUCTOS CON PEORES RESEÑAS ')
    print(f'|ID| \t\t Nombre del Producto \t Reseña Promedio \t Unidades Vendidas (u) \t Ganancia Total ($)')

    #Imprimiendo solo 5 productos
    for product, attributes in product_results_ord[0:6]: #Lista
        if attributes['Total Sales'] != 0:
            print(f'{attributes["ID"]} \t {product[0:30]} \t {attributes["Total Review"]} \t\t\t {attributes["Total Sales"]} \t\t\t {attributes["Total Profit"]} ')


def inf_sales_LifeStore():
    #Creación de diccionario donde se guarda la cantidad 
    #de ventas por cada mes.
    month_sales = {}
    mon_calendar = [datetime.date(2000, m, 1).strftime('%m') for m in range(1, 13)]
    for product in lifestore_sales:
            id_sales = product[0]
            refund = product[4]
            _, mon, year = product[3].split('/')
            if mon not in month_sales.keys():
                month_sales[mon] = []
            month_sales[mon].append(id_sales)

            for mons in mon_calendar:
                if mons not in month_sales.keys():
                    month_sales[mons] = []
            
            #Si hay una devolución, la venta no se concreta
            #por lo que no se contaría dentro del total
            if refund != 0:
                month_sales[mon].remove(id_sales)
            
    #Diccionario con información de cada uno de los meses
    #Cálculo del total de ventas y el total de ganancia por cada MES
    info_month = {}
    for mon in month_sales.keys():
        month_list = month_sales[mon]
        total_profit = 0
        total_sales = 0
        for id_sales in month_list:
            id_product = lifestore_sales[id_sales-1][1]
            price = lifestore_products[id_product-1][2]

            total_profit += price
            total_sales = len(month_list)
        
        #Se sustituye el número del mes por
        #su respectivo nombre, para mejor presentación
        if mon == '01':
            mons = '- January -'
        elif mon == '02':
            mons ='- February -'
        elif mon == '03':
            mons = '- March -'
        elif mon == '04':
            mons ='- April -'
        elif mon == '05':
            mons = '- May -'
        elif mon == '06':
            mons ='- June -'
        elif mon == '07':
            mons = '- July -'
        elif mon == '08':
            mons = '- August -'
        elif mon == '09':
            mons = '- September -'
        elif mon == '10':
            mons ='- October -'
        elif mon == '11':
            mons = '- November -'
        else:
            mons = '- December -'

        info_month[mons] = {
        'No': mon,
        'TSales': total_sales,
        'TProfit': total_profit}


    #Ordenando el diccionario de información por cada mes
    info_month_new = sorted(info_month.items(), key = lambda x: x[1]['No'], reverse= False)
    print(f'\nTOTAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES')
    print(f'\nNo.Mes \t Mes \t\t Ventas(u) \t Ingresos($)')

    #Imprimiendo la información del ingreso y ventas por cada mes
    total_anual_profit = 0
    for mons, attributes in info_month_new: #Lista
        print(f'{attributes["No"]} \t {mons} \t {attributes["TSales"]} \t\t {attributes["TProfit"]}')
        total_anual_profit += attributes["TProfit"]

    #Ordenando el diccionario de información por mes acorde a la cantidad de ventas
    info_month_new = sorted(info_month.items(), key = lambda x: x[1]['TSales'], reverse= True)
    print(f'\n\t5 MESES CON MÁS VENTAS AL AÑO')
    print(f'No.Mes \t Mes \t\t Ventas(u) \t Ingresos($)')

    #Imprimiendo la información de los meses con más ventas en LifeStore
    for mons, attributes in info_month_new[0:5]: #Lista
        print(f'{attributes["No"]} \t {mons} \t {attributes["TSales"]} \t\t {attributes["TProfit"]}')

    print(f'\nEl Total Anual de LifeStore es: $', total_anual_profit)


'''----------------------------------LOGIN----------------------------------------'''
users = {'Daniel Morán' : 'danielmoraan' , 'Jaime Alonso' : 'jimmyalonso'}
passwords = {'Daniel Morán' : 'Pyth0n3mTech' , 'Jaime Alonso' : '3mTechD4t4'}

intentos = 4
while intentos > 0:
    print("\t\tLIFESTORE - LOGIN")
    user = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')

    #Al ingresar con el usuario, borrará el contenido de la terminal
    #y mostrará el menú principal
    if  user == users['Daniel Morán'] and password == passwords['Daniel Morán']:
        sleep(2)
        system("cls")
        print('\tBIENVENIDE A LIFESTORE ' + str.upper(users['Daniel Morán']))

        print('\n1. Lista de los productos con mayores ventas')
        print('2. Lista de los productos con mayores búsquedas')
        print('3. Lista (por categoría) de los productos con menores ventas')
        print('4. Lista (por categoría) de los productos con menores búsquedas')
        print('5. Lista de los productos por reseña')
        print('6. Información financiera mensual y anual de LifeStore')
        print('7. Salir')

        ans = int(input('\nSelecciona una opción: '))
        
        #Al ingresar a cualquier opción, borrará el contenido de la terminal
        #y mostrará lo solicitado
        if ans == 1: 
            sleep(2)
            system("cls")
            top_sales_product()

        elif ans == 2:
            sleep(2)
            system("cls")
            top_searches_product()

        elif ans == 3:
            sleep(2)
            system("cls")
            category_bottom_sales()

        elif ans == 4:
            sleep(2)
            system("cls")
            category_bottom_searches()

        elif ans == 5:
            sleep(2)
            system("cls")
            product_review()

        elif ans == 6:
            sleep(2)
            system("cls")
            inf_sales_LifeStore()

        else:
            sleep(2)
            system("cls")
            print('REGRESA PRONTO...')
            exit()

        break

    elif user == users['Jaime Alonso'] and password == passwords['Jaime Alonso']:
        sleep(2)
        system("cls")
        print('\tBIENVENIDE A LIFESTORE ' + str.upper(users['Jaime Alonso']))

        print('\n1. Lista de los productos con mayores ventas')
        print('2. Lista de los productos con mayores búsquedas')
        print('3. Lista (por categoría) de los productos con menores ventas')
        print('4. Lista (por categoría) de los productos con menores búsquedas')
        print('5. Lista de los productos por reseña')
        print('6. Información financiera mensual y anual de LifeStore')
        print('7. Salir')

        ans = int(input('\nSelecciona una opción: '))
        
        #Al ingresar a cualquier opción, borrará el contenido de la terminal
        #y mostrará lo solicitado
        if ans == 1: 
            sleep(2)
            system("cls")
            top_sales_product()

        elif ans == 2:
            sleep(2)
            system("cls")
            top_searches_product()

        elif ans == 3:
            sleep(2)
            system("cls")
            category_bottom_sales()

        elif ans == 4:
            sleep(2)
            system("cls")
            category_bottom_searches()

        elif ans == 5:
            sleep(2)
            system("cls")
            product_review()

        elif ans == 6:
            sleep(2)
            system("cls")
            inf_sales_LifeStore()

        else:
            sleep(2)
            system("cls")
            print('REGRESA PRONTO...')
            exit()

        break
    else:
        print('El usuario y/o contraseña son incorrectos')
        intentos -= 1
        print('Tienes ' + str(intentos) + ' intentos más\n')
        if intentos == 0:
            print("¡Acceso bloqueado! Intentalo más tarde")
            exit()
    sleep(2)
    system("cls")






