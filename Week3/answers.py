# Question 1
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:

        discount = (price * discount_percent)/100

        return price - discount
    
    else:
        return price 

finalPrice = calculate_discount(5500, 26)
print(finalPrice)


# Question 2
price = float(input("What if the price of the item?"))

discount_percent = float(input("What is the discount?" ))

finalPrice = price - (price * discount_percent)/100

print(finalPrice)