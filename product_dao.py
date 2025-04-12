import mysql.connector
from mysql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = """
    SELECT products.product_id, products.product_name, products.category, 
           products.brand, products.quantity, products.uom_id, 
           products.price, products.supplier, products.expiry_date, 
           products.date_added, uom.uom_name  
    FROM `grocery store`.products 
    INNER JOIN uom ON products.uom_id = uom.uom_id
    """
    cursor.execute(query)

    response = []
    for (product_id, product_name, category, brand, quantity, uom_id, price, supplier, expiry_date, date_added, uom_name) in cursor:
        row = {
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'brand': brand,
            'quantity': quantity,
            'uom_id': uom_id,
            'price': price,
            'supplier': supplier,
            'expiry_date': expiry_date,
            'date_added': date_added,
            'uom_name': uom_name
        }
        response.append(row)
        print(row) 
    return response

def insert_product(connection, product):
    cursor = connection.cursor()
    query = """
    INSERT INTO `grocery store`.products 
    (product_id, product_name, category, brand, quantity, uom_id, price, supplier, expiry_date) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    data = (
        product['product_id'],
        product['product_name'],
        product['category'],
        product['brand'],
        product['quantity'],
        product['uom_id'],
        product['price'],
        product['supplier'],
        product['expiry_date']
    )
    
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM `grocery store`.products WHERE product_id = %s")
    cursor.execute(query, (product_id,))
    connection.commit()
    return f"Product with ID {product_id} deleted sucessfully."
    
if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 457894))