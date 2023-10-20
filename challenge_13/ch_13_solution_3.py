"""
Find Product with Highest Sales
=================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=================================

This script defines a function, find_product_with_highest_sales, 
which identifies the product with the highest sales
based on the input sales transaction data.
"""


def find_product_with_highest_sales(data: list):
    """
    Find the product with the highest sales based on the input data.

    Args:
        data (list): A list of tuples or lists containing sales transaction data.
        Each data item should have three elements, i.e., transaction ID, 
        product ID and sales price

    Returns:
        tuple: A tuple containing the product ID and the total sales amount 
        of the product with the highest sales.

    Raises:
        ValueError: If the data format is not a tuple or a list with three elements,
                    or if the sales price is not a numerical value.
    """
    product_sales = {}

    for sales_record in data:
        if isinstance(sales_record, (tuple, list)) and len(sales_record) == 3:
            _, product_id, sales_price = sales_record

            if isinstance(sales_price, (int, float)):
                if product_id in product_sales:
                    product_sales[product_id] += sales_price
                else:
                    product_sales[product_id] = sales_price
            else:
                raise ValueError(
                    f"Product sales price must be a numerical value: {sales_record}")
        else:
            raise ValueError(
                f"The data format must be a tuple or a list with three elements: {sales_record}")

    # Find the product with the highest sales
    top_product_id = max(product_sales, key=lambda k: product_sales[k])
    top_product_sales = product_sales[top_product_id]

    return top_product_id, top_product_sales


if __name__ == '__main__':
    transactions = [
        (1, 101, 15.0),
        (2, 102, 20.0),
        (3, 101, 15.0),
        (4, 103, 10.0),
        (5, 102, 20.0),
        (6, 101, 15.0),
        (7, 103, 10.0),
        (8, 102, 20.0),
        (9, 103, 10.0)
    ]

    result = find_product_with_highest_sales(data=transactions)
    print(
        f"The product ID {result[0]} has the highest sales. The sales amount is ${result[1]:,.1f}")
