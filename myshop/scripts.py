import requests

url = 'http://localhost:18800/api/products/'  # Полный адрес эндпоинта
response = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_on_python = response.json()
# Запишем полученные данные в файл product.txt
with open('products.txt', 'w') as file:
    for product in response_on_python:
        file.write(
            f"id - {product['id']}, name - {product['name']}, price - {product['price']}, category - {product['category']}.\n"
        )