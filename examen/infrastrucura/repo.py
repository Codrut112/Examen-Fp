class RepoError(Exception):
    pass


class Repo():
    def __init__(self):
        self._repo={}
    def get_all(self):
        '''
        returneeaza o lista cu toate spectacolele
        :return: list
        '''
        emisiuni=[]
        for emisiune in self._repo.values():
            emisiuni.append(emisiune)
        return emisiuni
    def adauga_spectacol(self,spectacol):
        '''
        adauga un spectacol in aplicatie
        :param spectacol: spectacol
        :return: -
        '''

        if spectacol.get_id() in self._repo:
            raise RepoError("spectacol existent!")
        self._repo[spectacol.get_id]=spectacol
    def modifica_spectacol(self,spectacol):
        '''
        modifica un spectacol
        :param spectacol: spectacol
        :return: -
        '''
        if spectacol.get_id() not in self._repo:
            raise RepoError("spectacol inexistent!")
        self._repo[spectacol.get_id()]=spectacol
    def __len__(self):
        '''
        returneaza numarul de spectacole din fisier
        :return:
        '''
        return len(self._repo)
