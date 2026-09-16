def calculate_picnic_cost(sandwich_price, drink_price, dessert_price, flower_price):
    total_cost = sandwich_price + drink_price + dessert_price + flower_price
    return f"Our romantic picnic basket contains sandwiches, drinks, desserts, and flowers for ${total_cost:.2f} total"