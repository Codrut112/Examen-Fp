class Spectacol():
    def __init__(self,id,titlu,artist,gen,durata):
        self.__id=id
        self.__titlu=titlu
        self.__artist=artist
        self.__gen=gen
        self.__durata=durata
    def get_id(self):
        '''
        returneaza idul spectacolului
        :return: str
        '''
        return self.__id
    def get_artist(self):
        '''
        returneaza artistul spectacolului
        :return: str
        '''
        return self.__artist
    def get_titlu(self):
        '''
        returneaza titlu spectacolului
        :return: str
        '''
        return self.__titlu
    def get_durata(self):
        '''
        returneaza durata spectacolului
        :return: int
        '''
        return self.__durata
    def set_gen(self,gen):
        '''
        seteaza genul unui spectacol
        :return: -
        '''
        self.__gen=gen
    def set_durata(self,durata):
        '''
        seteaza durata unui spectacol
        :return: int
        '''
        self.__durata=durata
    def get_gen(self):
        '''
        returneaza genul unui spectacol
        :return: string
        '''
        return self.__gen
    def __str__(self):
        '''
        functie de afisare
        :return: str
        '''
        return f'{self.__id},{self.__titlu},{self.__artist},{self.__gen},{self.__durata}'
    def __eq__(self, other):
        '''
        verifica daca doua spectacole au acelasi id
        :param other: spectacol
        :return:
        '''
        return self.__id==other.get_id()
    def str2(self):
        '''
                functie de afisare
                :return: str
                '''
        return f'{self.__titlu},{self.__artist},{self.__gen},{self.__durata}'
