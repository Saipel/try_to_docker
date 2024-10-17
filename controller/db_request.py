
def insert_some_data(text_for_insert : chr, conn):
    cur = conn.cursor()
    sql_command = """INSERT INTO test_bd(some_text) VALUES(%s)"""
    cur.execute(sql_command, (text_for_insert, ))
    conn.commit()
    cur.close()  
    conn.close()

def select_data(conn):
    cur = conn.cursor()
    sql_command = """SELECT * FROM test_bd"""
    cur.execute(sql_command)
    some_text = cur.fetchall()
    cur.close()
    conn.close()
    return form_json(some_text)

def form_json(db_request_rezult):
   return dict(db_request_rezult)
        