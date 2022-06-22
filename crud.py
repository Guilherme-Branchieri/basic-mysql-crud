import mysql.connector

class DataBase():
    def __init__(self):
        pass

    def connect_db(self, host='localhost', user='root', password='Aa1@sessenta', database='clients'):
        global data_base
        global cursor
        try:
            data_base = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database = database

                
            )
            cursor = data_base.cursor()
            
        except mysql.connector.Error as error:
            print(f"Error found: {error}")

        finally:
            if data_base.is_connected():
                print('Connection went successful')
            else:
                print("Verify inserted data or try again later")
                
    def disconnect_db(self):
        if data_base.is_connected():
            data_base.close()
            print('Disconnected from MySQL')
                
    def create_db(self, name):
        cursor.execute(f"CREATE DATABASE {name}")
        print('Successfully created database')
    
    
    def create_table(self, name):
        global table_name


        table_name = name
        cursor.execute(f"CREATE TABLE {name} (id INT(5), client VARCHAR(255), email VARCHAR(255), phone int(30), cpf VARCHAR(14))")
        print(f'Successfully created table {name}')

    def drop_table(self, name):
        cursor.execute(f"DROP TABLE {name}")
        print(f'Deleting table {name}')
        
    def insert_data(self, id, client, email, phone, cpf,table_name='client_info'):
        
        try:

            cursor.execute(f"SELECT * FROM {table_name}")
            search_client = []
            client_data = dict()        
            for column in cursor.fetchall():
                client_data['id'] = column[0]
                search_client.append(client_data['id'])
                client_data['client'] = column[1]
                client_data['email'] = column[2]
                client_data['phone'] = column[3]
            if id in client_data.values():    
                print('Client already in database')
                return
            else:
                insert = f"INSERT INTO {table_name} (id, client, email, phone, cpf) VALUES (%s, %s, %s, %s, %s)"
                data = (id, client, email, phone, cpf)
                cursor.execute(insert, data)
                data_base.commit()                            
                print(f'Client added successfully')
        except mysql.connector.Error as erro:
                print(f'An error ocurred: {erro}')

        finally:
            print('Done')

    def ver_cliente(self):
        cursor.execute(f"SELECT * FROM {table_name}")
        cursor.execute(f"SELECT * FROM {table_name}")
        cursor.fetchmany()
        return data

    def delete_client(self, id):
        cursor.execute(f"DELETE FROM {table_name} WHERE id = {id}")
        data_base.commit()
        print(f'Produto excluido com sucesso')



    
db = DataBase()
db.connect_db(
    host='localhost',
    user='root',
    password='Aa1@sessenta',
    database = 'clients'
)
db.ver_cliente()




