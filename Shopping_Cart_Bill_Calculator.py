# Shopping Cart & Bill Calculator

customer_name = input("Enter customer name: ")

products = ("Laptop", "Mouse", "Keyboard", "Monitor", "Headphones")

prices = [50000, 800, 1500, 12000, 2000]

total = prices[0] + prices[1] + prices[2] + prices[3] + prices[4]

average = total / len(prices)

product_details = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000
}

unique_products = set(products)

laptop_present = "Laptop" in products
mouse_present = "Mouse" in products

price_comparison = prices[0] > prices[1]

logical_result = prices[0] > 10000 and prices[1] < 1000

print("Customer Name:", customer_name)
print("Products:", products)
print("Prices:", prices)
print("Total:", total)
print("Average:", average)
print("Product Details:", product_details)
print("Unique Products:", unique_products)
print("Laptop Present:", laptop_present)
print("Mouse Present:", mouse_present)
print("Laptop price greater than Mouse price:", price_comparison)
print("Logical Result:", logical_result)