from openfoodfacts.products import get_product
from openfoodfacts import utils


print('Enter a barcode: ')
query = input()
product = get_product(str(query))


print('Name: ' + product['product']['product_name'])
print('Quantity: ' + str(product['product']['product_quantity']))
print('Cals: ' + str(product['product']['nutriments']['energy-kcal_100g']))
print('Carbs: ' + str(product['product']['nutriments']['carbohydrates_100g']))
print('Proteins: ' + str(product['product']['nutriments']['proteins_100g']))
print('Fat: ' + str(product['product']['nutriments']['fat_100g']))