def calculate_cart_total(cart, flowers_in_cart):
    total = 0
    for flower in flowers_in_cart:
        quantity = cart[str(flower.id)]
        total += flower.price * int(quantity)
    return total