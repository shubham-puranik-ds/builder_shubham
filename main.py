from src.metrics import *
sales = [100, 200, 300, 400, 500]

total_sales, average_sales = calculate_sales_metrics(sales)
max_sales=calculate_max_sales(sales)

print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"max Sales: {max_sales}")

print("Learning Git!")