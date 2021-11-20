from openfoodfacts import products
import product

listaProds = []
query = ''

def search():

    return product.InvenProduct()

print('Introduce término de búsqueda: ')

query = input()

for product in products.search_all(query):
    print (product['product_name'])