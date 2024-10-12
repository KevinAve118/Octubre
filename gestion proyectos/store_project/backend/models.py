import sqlite3
#definimos la conexion de sqllite3
def get_db_connection():
    conn = sqlite3.connect('store.db')
    con.row_factory = sqlite3.Row
    return conn
#definimos la conexion de ña db tabla de productos
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products') 

    conn.close()
    return products
def add_product(name,descripcion, price, stock):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO products (name, descripcion, price, stock)'VALUES (?,?;?;?)",( name, descripcion, price,stock)) 
    
    conn.commit()
    conn.close()