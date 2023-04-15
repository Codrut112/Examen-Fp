from domeniu.spectacol import Spectacol
from infrastrucura.repo import Repo


class File_Repo(Repo):
    def __init__(self,calea_catre_fisier):
        self.__calea_catre_fisier=calea_catre_fisier
        Repo.__init__(self)
    def read_all_from_file(self):
        '''
        adaauga in aplicatie toate spectacolele din fisier
        :return:-
        '''
        with open(self.__calea_catre_fisier,'r') as f:
            lines=f.readlines()
            self._repo.clear()
            for line in lines:
                if line!='':
                    line=line.strip()
                    parti=line.split(',')
                    spectacol=Spectacol(int(parti[0]),parti[1],parti[2],parti[3],int(parti[4]))
                    self._repo[int(parti[0])]=spectacol
    def write_all_to_file(self):
        '''
        scrie in fisier taote spectacolele din aplicatie
        :return:-
        '''
        with open(self.__calea_catre_fisier,'w') as f:
            for spectacol in self._repo.values():
                f.write(str(spectacol)+"\n")
    def adauga_spectacol(self,spectacol):
        '''
        adauga in aplicatie si scrie in fisier un spectacol
        :param spectacol: spectacol
        :return: -
        '''

        self.read_all_from_file()
        Repo.adauga_spectacol(self,spectacol)
        self.write_all_to_file()
    def modifica_spectacol(self,spectacol):
        '''
        modifica un spectacol
        :param spectacol: spetacol
        :return: -
        '''
        self.read_all_from_file()
        Repo.modifica_spectacol(self,spectacol)
        self.write_all_to_file()
    def __len__(self):
        '''
        returneaza numarul
        :return:int
        '''
        self.read_all_from_file()
        return Repo.__len__(self)
    def get_all(self):
        '''
        returneaza o slista cu toate spectacolele din fiser
        :return: list
        '''
        self.read_all_from_file()
        return Repo.get_all(self)
    def clear(self):
        '''
        sterge toate spectacolele din fisiere
        :return: -
        '''
        with open(self.__calea_catre_fisier, 'w') as f:
            pass





