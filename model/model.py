from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO
        self.G.clear() #pulisco il grafico da quello che è apparso in una richiesta precedente
        id_map_filiali={}
        self._nodes=DAO.get_filiali() #salvo in questa variabile la lista di oggetti della classe Filiale
        for filiale in self._nodes: #per ogni filiale in quella lista...
            self.G.add_node(filiale) #...ci creo un nodo nel grafo
            id_map_filiali[filiale.id]=filiale #chiave=id, valore=oggetto filiale intero

            #aggiungo un nodo per ogni filiale, anche se successivamente
            #alcune possono non avere collegamenti, ma esistono comunque

        bonifici=DAO.get_bonifici() #salvo in sta variabile la lista di oggetti bonifici
        collegamenti={}
        for b in bonifici: #itero per ogni bonifico nella lista
            # Ordino i due ID in modo che (A, B) e (B, A) producano la stessa identica chiave
            # Se capita la stessa coppia ma invertita questo if else mette sempre quello
            # piu piccolo a sx e verrano due coppie di id uguali
            id1 = b.id_filiale_origine #estraggo ogni origine e ogni destinazione di ogni bonifico nella lista
            id2 = b.id_filiale_destinazione
            if id1 < id2:
                coppia = (id1, id2)
            else:
                coppia = (id2, id1) #se c'è (3,8) o (8,3), con questo if else la coppia viene uguale-->(3,8)

            if coppia not in collegamenti:
                collegamenti[coppia] = [0.0, 0] #chiave è la tupla con la coppia di id
        #il valore è la somma degli importi e il conteggio dei collegamenti, al di là della direzione, tre 2 stesse filiali
            collegamenti[coppia][0] += b.importo #somma degli importi per coppie uguali
            collegamenti[coppia][1] += 1

            #Calcolo l'importo medio per ogni coppia e aggiungo l'arco se >= threshold
        for coppia, dati in collegamenti.items():
            somma_importi = dati[0]
            conteggio = dati[1]
            importo_medio = somma_importi / conteggio

            if importo_medio >= threshold:
                filiale_1 = id_map_filiali[coppia[0]] #presso l'oggetto filiale identificato in map dall'id
                filiale_2 = id_map_filiali[coppia[1]]
                self.G.add_edge(filiale_1, filiale_2, weight=importo_medio)
                #metto nel grafo solo quelli che superano la soglia!

                #per gli edge si deve mettere come parametro i nodi di inizio e di fine e il valore del colleg.(peso)





    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges() #numero di collegamenti nel grafo, ovvero dei bonifici tra filiali sopra la soglia!

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return self.G.edges(data=True) #senza data=True otterrei solo i due id...invece voglio pure il valore
