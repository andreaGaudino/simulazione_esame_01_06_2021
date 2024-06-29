from database.DB_connect import DBConnect
from model.geni import Gene


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.GeneID as id, Chromosome as cromosoma
                    from genes_small.genes g 
                    where g.Essential = 'Essential' """

        cursor.execute(query, ())

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinctrow g.GeneID as g1, g2.GeneID as g2, i.Expression_Corr as corr, g.Chromosome as c1, g2.Chromosome as c2
                    from genes_small.genes g, genes_small.genes g2 , genes_small.interactions i 
                    where ( (g.GeneID = i.GeneID1 and g2.GeneID = i.GeneID2 ) or (g2.GeneID = i.GeneID1 and g.GeneID = i.GeneID2 ) )
                    and g.Essential = 'Essential' 
                    and g2.Essential = 'Essential'
                    and g.GeneID < g2.GeneID  """

        cursor.execute(query, ())

        for row in cursor:
            result.append([row["g1"],row["g2"],row["corr"],row["c1"],row["c2"]])

        cursor.close()
        conn.close()
        return result
