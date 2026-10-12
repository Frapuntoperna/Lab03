from operator import attrgetter
class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno = int(anno)
        self.valore = float(valore)

    def __str__(self):
        return f"[{self.id_strumento}] {self.tipo} {self.marca} ({self.anno}) - €{self.valore:.2f}"



class Prestito:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"[{self.id_prestito}] Strumento {self.id_strumento} in prestito a {self.cognome_allievo} dal {self.data}"



class DepositoStrumenti:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}



    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        with open (file_path, 'r', encoding= 'utf-8') as file:
            for riga in file:
                lista = riga.strip().split(',')
                id_strumento = lista[0]
                tipo = lista[1]
                marca = lista[2]
                anno_acquisto = lista[3]
                valore = lista [4]

                strumento=Strumento(id_strumento,tipo, marca, anno_acquisto, valore)
                self.strumenti [id_strumento]=strumento

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        i=1
        for chiave in self.strumenti:
            i+=1

        contatore_codice=str(f'S{i}')
        nuovo_strumento = Strumento(contatore_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti[contatore_codice]=nuovo_strumento
        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        lista_strumenti=list(self.strumenti.values())
        lista_strumenti.sort(key=attrgetter('marca'))
        return lista_strumenti


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        self.data=data
        self.id_strumento=id_strumento
        self.cognome_allievo=cognome_allievo
        lista_prestito=[data, id_strumento, cognome_allievo]
        i=0
        for i in self.prestiti:
            i+=1
        id_prestito=str(f'P{i}')
        self.strumenti[id_prestito]=lista_prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        self.prestiti[id_prestito]=None