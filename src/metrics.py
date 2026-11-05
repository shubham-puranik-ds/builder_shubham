def calculate_sales_metrics(sales):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)

    return total_sales, average_sales

def calculate_max_sales(sales):
    return max(sales)