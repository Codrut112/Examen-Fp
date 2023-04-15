import random

from domeniu.spectacol import Spectacol


class Service():
    def __init__(self,repo,validator):
        self.__repo=repo
        self.__validator=validator
    def adauga_spectacol(self,id,titlu,artist,gen,durata):

        '''
        adauga un spectacol in aplicatie
        :param id: int
        :param titlu: string
        :param artist: string
        :param gen: string
        :param durata:int
        :return: -
        raise valid error daca spectacolul nnu este valid
        repo error daca deja exista in aplicatie
        '''
        spectacol=Spectacol(id,titlu,artist,gen,durata)
        self.__validator.valideaza(spectacol)
        self.__repo.adauga_spectacol(spectacol)

    def modifica_spectacol(self, id, titlu, artist, gen, durata):
        '''
                modifica un spectacol din aplicatie
                :param id: int
                :param titlu: string
                :param artist: string
                :param gen: string
                :param durata:int
                :return: -
                raise valid error daca spectacolul nu este valid
                repo error daca nu exista in aplicatie
                '''

        spectacol = Spectacol(id, titlu, artist, gen, durata)
        self.__validator.valideaza(spectacol)

        self.__repo.modifica_spectacol(spectacol)

    def get_all(self):
        '''
        returneaza o lista cu toate spectacolele
        :return: list
        '''

        return self.__repo.get_all()
    def __len__(self):
        '''
        returneaza numarul de spectacole
        :return: int
        '''
        return self.__repo.__len__()
    def export(self,nume_fisier):
        '''
        scrie in fisierul nume_fisier toate spectacolele ordonate dupa titlu si artist
        :param nume_fisier: string
        :return: -
        '''
        with open(nume_fisier,'w') as f:
            spectacole=self.__repo.get_all()


            spectacole.sort(key=lambda x :(x.get_titlu(),x.get_artist())   )
            for spectacol in spectacole:

                f.write(spectacol.str2()+"\n")
    def adauga_random(self):
        '''
        adauga un spectacol generat random
        :return: spectacol
        '''
        x=random.randint(9,12)
        voc='aeiouAEIOUYy'
        cons='zxcvbnmsdfghjklqwrtpZXCVBNMSDFGHJLQWRTP'
        titlu=''
        artist=''
        for i in range(x):
            if i==4:
                titlu=titlu+' '
                artist=artist+' '

            if i%2==0:
                i = random.randint(0, 4)
                titlu=titlu+voc[i]
                i = random.randint(0, 4)
                artist=artist+voc[i]
            else:
                i = random.randint(0, 15)
                titlu = titlu + cons[i]
                i = random.randint(0, 15)
                artist = artist + cons[i]
        id=random.randint(9000,120000000)
        i = random.randint (0,3)
        genuri=['Comedie','Concert','Balet','Altele']
        gen=genuri[i]
        durata = random.randint(1, 5)
        spectacol = Spectacol(id, titlu, artist, gen, durata)
        self.__validator.valideaza(spectacol)
        self.__repo.adauga_spectacol(spectacol)
        return spectacol







