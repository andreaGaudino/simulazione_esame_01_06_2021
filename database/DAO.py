from database.DB_connect import DBConnect


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Product_color as c
                    from go_sales.go_products gp 
                    order by Product_color """

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["c"])

        cursor.close()
        conn.close()
        return result

