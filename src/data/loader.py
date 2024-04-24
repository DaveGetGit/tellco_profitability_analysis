from connection import database_connection_pool


def fetch_top_ten_handsets():
    """
        This function will select the top handsets used by users
    """
    connection = database_connection_pool.get_connection()
    try:
        with connection.cursor() as cursor:
            sql_query = """
            SELECT "Handset Type", COUNT("Handset Type") AS handset_count 
            FROM public.xdr_data
            GROUP BY "Handset Type"
            ORDER BY handset_count DESC
            LIMIT 10
            """
            cursor.execute(sql_query)
            handset_data = cursor.fetchall()
    finally:
        database_connection_pool.release_connection()
    return handset_data
