import copy
import random

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def buildGraph(self):
        self.graph.clear()
        nodi = DAO.getNodi()
        for n in nodi:
            self.graph.add_node(n)
            self.idMap[n.id] = n
        archi = DAO.getArchi()
        for riga in archi:
            if riga[3] == riga[4]:
                self.graph.add_edge(self.idMap[riga[0]], self.idMap[riga[1]],weight = float(2 * abs(riga[2])))
            else:
                self.graph.add_edge(self.idMap[riga[0]], self.idMap[riga[1]], weight=float(abs(riga[2])))

    def getAdiacenti(self, gene):
        vicini = list(self.graph.neighbors(gene))
        res = {}
        for v in vicini:
            res[v] = self.graph[gene][v]["weight"]
        ordinati = sorted(res, key=lambda x: res[x], reverse=True)
        final = {}
        for o in ordinati:
            final[o] = res[o]
        return final


    def simulazione(self, gene, nIng):
        dizio = {gene:nIng}
        for i in range(36):
            nuovoDizio = {}
            for g in dizio:
                vicini = list(self.graph.neighbors(g))
                denominatore = 0
                for v in vicini:
                    denominatore += float(self.graph[g][v]["weight"])
                nuoviIng = round(0.7 * dizio[g])
                nuovoDizio[g] = dizio[g] - round(0.7 * dizio[g])
                for v in vicini:
                    if denominatore==0:
                        prob = 1
                    else:
                        prob = (float(self.graph[g][v]["weight"]))/denominatore
                    if v not in dizio:
                        nuovoDizio[v] = round(prob*nuoviIng)
                    else:
                        nuovoDizio[v] = dizio[v] + round(prob * nuoviIng)

            dizio = copy.deepcopy(nuovoDizio)
        print(dizio)
        return dizio



    def graphDetails(self):
        for a in list(self.graph.edges(data=True)):
            if a[2]["weight"] == 0 :
                print(a)
        return len(self.graph.nodes),  len(self.graph.edges)