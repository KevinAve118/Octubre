CREATE TABLE IF NOT EXISTS products(
    id integer PRIMARY KEY autoincrement,
    name TEXT NOT NULL,
    descripcion TEXT NOT NULL, 
    price REAL NOT NULL, 
    stock INTEGER NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)