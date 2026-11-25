import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
    # il controller dice alla view(che contiene i vari controlli e pulsanti) che cosa deve fare vedere 'al click' diciamo
    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO
        self._view.lista_visualizzazione.controls.clear() #pulisco la lista di visualizzazione dai collegamenti precedenti
        importo = self._view.importo_medio_minimo.value #importo soglia dato in input
        try:
            importo=float(importo)
            if importo < 0:
                self._view.show_alert("Inserire un importo minimo positivo")
                self._view.update()
                return
        except ValueError:
            self._view.show_alert("Inserire un valore numerico valido")
            self._view.update()
            return

        # metto l'importo in input come parametro e mi trova con quella
        # def del model i vari collegamenti costruiti
        self._model.costruisci_grafo(importo)
        num_nodes=self._model.get_num_nodes() #prendeva il numero di nodi in seguito al grafo filtrato dalla def preced.
        num_edges=self._model.get_num_edges() #prendeva il numero di colleg. in seguito al grafo filtrato dalla def preced.
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Filiali: {num_nodes}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Collegamenti: {num_edges} "))
        n=1
        for u, v, data in self._model.get_all_edges():
            peso = data['weight']
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"{n}) | {u} -> {v} | <-> Importo medio per bonifico: € {peso:.2f} ")
            )
            n+=1

            # 6. Aggiorno la pagina Flet per mostrare tutto a schermo
        self._view.update()


