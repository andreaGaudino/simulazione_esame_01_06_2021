import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.gene = None


    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        n, e = self._model.graphDetails()
        self._view.txtGrafo.clean()
        self._view.txtGrafo.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self.fillDD()
        self._view.update_page()


    def handleCercaAdiacenti(self, e):
        if self.gene is None:
            self._view.create_alert("Gene non selezionato")
            self._view.update_page()
            return
        dizio = self._model.getAdiacenti(self.gene)
        self._view.txtGeniAd.controls.append(ft.Text(f"Geni adiacenti a {self.gene}"))
        for i in dizio:
            self._view.txtGeniAd.controls.append(ft.Text(f"{i} - {dizio[i]}"))
        self._view.update_page()


    def handleSimulazione(self, e):
        ing = self._view.nIngegneri.value
        if ing == "":
            self._view.create_alert("Numero di ingegneri non inserito")
            self._view.update_page()
            return


        try :
            intIng = int(ing)
        except ValueError:
            self._view.create_alert("Numero di ingegneri inserito non numerico")
            self._view.update_page()
            return

        self._model.simulazione(self.gene, intIng)
    def fillDD(self):
        nodi = list(self._model.graph.nodes)
        nodiDD = list(map(lambda x: ft.dropdown.Option(text=x, key=x, on_click=self.getNodo), nodi))
        self._view.ddGene.options = nodiDD

    def getNodo(self, e):
        if e.control.key is None:
            pass
        else:
            self.gene = e.control.key