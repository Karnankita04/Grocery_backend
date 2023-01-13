# dao stands for data access object 
from sql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor = connection.cursor()
    query = ("SELECT products.Product_id,products.Name,products.Uom_id,products.Price_per_Unit,"
    "uom.uom_name FROM gs.products inner join uom on uom.uom_id = products.Uom_id ;")
    cursor.execute(query)
    response = []
    for (P_id,Name,Uom_id,PPU,uom_name) in cursor:
        response.append({
            'Product_id':P_id,
            'Name':Name,
            'Uom_id': Uom_id,
            'Price_per_Unit':PPU,
            'uom_name':uom_name
        }) 
    # connection.close()
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (Name,Uom_id,Price_per_Unit) VALUES (%s, %s, %s)")
    data = (product['Product_name'],product['UOM_ID'],product['Price_per_unit'])
    cursor.execute(query,data)
    connection.commit() #commit will help to save to record permanently 
    return cursor.lastrowid
    
def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where Product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit() #commit will help to save to record permanently 
    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # for deleting the product using product id from database
    print(delete_product(connection,8))


    # for inserting new product into table
    # print(insert_new_product(connection,{
    #     'Product_name':'Banana',
    #     'UOM_ID':2,
    #     'Price_per_unit':30
    # }))

    # for print all the product 
    # print(get_all_products(connection))
