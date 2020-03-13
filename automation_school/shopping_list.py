def cost(l):
    total_sum = 0
    for i in l:
        total_sum += i['quantity'] * i['price']
    return total_sum


a = {
  "product": "Milk",
  "quantity": 1,
  "price": 1.50
}

b = {
  "product": "Bread",
  "quantity": 3,
  "price": 1
}

c = {
  "product": "Eggs",
  "quantity": 10,
  "price": 0.25
}

shopping_list = [a, b, c]
print(cost(shopping_list))

