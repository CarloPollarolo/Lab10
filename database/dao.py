from database.DB_connect import DBConnect
from model.filiale import Filiale
from model.bonifico import Bonifico
class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO

    @staticmethod
    def get_filiali():
        cnx = DBConnect.get_connection()
        filiali = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = " SELECT * FROM filiale "
        try:
            cursor.execute(query)
            for row in cursor:
                filiale = Filiale(
                    row['id'],
                    row['codice'],
                    row['nome'],
                    row['citta'],
                    row['provincia'],
                    row['latitudine'],
                    row['longitudine']
                )
                filiali.append(filiale) #creo una lista di oggetti filiali, e cosi anche avanti per bonifici
        except Exception as e:
            print(f"Errore durante la query get_filiali: {e}")
            filiali = None
        finally:
            cursor.close()
            cnx.close()

        return filiali
    @staticmethod
    def get_bonifici():
        cnx = DBConnect.get_connection()
        bonifici = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = " SELECT * FROM bonifico "
        try:
            cursor.execute(query)
            for row in cursor:
                bonifico = Bonifico(
                    row["id"],
                    row["id_banca"],
                    row['codice_operazione'],
                    row['id_filiale_origine'],
                    row['id_filiale_destinazione'],
                    row['data_disposizione'],
                    row['commissione'],
                    row['data_accredito'],
                    row['importo']

                )
                bonifici.append(bonifico)
        except Exception as e:
            print(f"Errore durante la query get_bonifici: {e}")
            bonifici = None
        finally:
            cursor.close()
            cnx.close()

        return bonifici

