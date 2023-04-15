from infrastrucura.repo import RepoError
from validator.validator import ValidError


class UI():
    def __init__(self,service):
        self.__service=service
        self.__comenzi={
            'adauga_spectacol':self.adauga_spectacol,
            'modifica_spectacol':self.modifica_spectacol,
            'export':self.export,
            'random':self.randoma
        }
    def run(self):
        while True:
            comanda=input('>>>')
            if comanda=='gata':
                break
            parti=comanda.split()
            comanda=parti[0]
            self.__params=parti[1:]

            if comanda in self.__comenzi:
                try:
                    self.__comenzi[comanda]()
                except ValueError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
                except ValidError as ve:
                    print(ve)
            else: print("comanda invalida")
    def adauga_spectacol(self):
        '''
        adauga un spectacol in fisier

        :return:-
        '''
        id = int(input('id='))
        titlu = input('titlu=')
        artist = input("artist=")
        gen = input("gen=")
        durata = int(input('durata='))
        self.__service.adauga_spectacol(id, titlu, artist, gen, durata)
        print("spectacol adaugat cu succes")
    def modifica_spectacol(self):
        '''
        modifica un spectacol din fisier
        :return:-
        '''

        id=int(input('id='))
        titlu=input('titlu=')
        artist=input("artist=")
        gen=input("gen=")
        durata=int(input('durata='))
        self.__service.modifica_spectacol(id,titlu,artist,gen,durata)
        print("spectacol modificat cu succes")
    def export(self):
        '''
        afiseaza spectacole intr-un fisier dat de utulizator
        :return:-
        '''
        if (len(self.__params) != 1):
            print('numar parametri invalid')
            return
        self.__service.export(self.__params[0])
    def randoma(self):
        if (len(self.__params) != 1):
            print('numar parametri invalid')
            return
        spectacole=[]
        x=int(self.__params[0])
        for i in range(x):
            spectacole.append(self.__service.adauga_random())
        for spectacol in spectacole:
            print(spectacol.str2())


