import sqlite3

database = sqlite3.connect("my_database.db")
cursor = database.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        first_name varchar(255),
        last_name varchar(255),
        phone_number INTEGER
    );
""")

# cursor.execute("""
# insert into Users (first_name, last_name, phone_number)
#  values ('name2', 'name3', 89001003030)
#
#  """)

# database.commit()

# print(cursor.execute("""
# select * from Users where id > 5
# """).fetchall())



cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        product_name varchar(255),
        creator_id INTEGER 
    );
""")


# cursor.execute("""
# insert into Products (product_name, creator_id) values ("milk", 3)
# """)
#
# database.commit()


print(cursor.execute("""
select * from Products where creator_id = 1
""").fetchall())

database.commit()