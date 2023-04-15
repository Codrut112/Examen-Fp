from business.service import Service
from domeniu.spectacol import Spectacol
from infrastrucura.file_repo import File_Repo
from infrastrucura.repo import RepoError
from validator.validator import Validator, ValidError


class Teste():
    def testare(self):
        self.teste_domeniu()
        self.teste_repo()
        self.teste_validator()
        self.teste_service()

    def teste_domeniu(self):
        spectacol=Spectacol(1,"da",'nu',"comedie",2)
        assert spectacol.get_id()==1
        assert spectacol.get_durata()==2
        assert spectacol.get_titlu()=='da'
        assert spectacol.get_artist()=='nu'
        spectacol.set_gen('gen')

        assert spectacol.get_gen()=='gen'




    def teste_repo(self):
        spectacol = Spectacol(1,"da", 'nu', "comedie", 2)
        repo=File_Repo("teste/spectacol.test")
        repo.clear()
        assert repo.__len__()==0
        repo.adauga_spectacol(spectacol)
        repo.adauga_spectacol(Spectacol(2,"da", 'nu', "comedie", 2))
        repo.adauga_spectacol(Spectacol(3, "da", 'nu', "comedie", 2))
        try:
            repo.adauga_spectacol(spectacol)
            assert False
        except RepoError:
            assert True

        assert repo.__len__()==3
        repo.modifica_spectacol(Spectacol(1,"da", 'nu', "comedie", 3))
        spectacole=repo.get_all()
        assert spectacole[0].get_durata()==3

        repo.clear()

    def teste_validator(self):
        validator=Validator()
        validator.valideaza(Spectacol(1,"da", 'nu', "Comedie", 2))
        try:
            validator.valideaza(Spectacol(1,"da", 'nu', "comedie", 2))
            assert False
        except ValidError:
            assert True

    def teste_service(self):
        service=Service(File_Repo("teste/spectacol.test"),Validator())

        assert service.__len__()==0
        service.adauga_spectacol(1,"da", 'nu', "Comedie", 5)
        assert service.__len__() == 1
        service.modifica_spectacol(1,"da", 'nu', "Comedie", 5)
        spectacole=service.get_all()
        assert spectacole[0].get_durata()==5
        service.adauga_spectacol(2, "da", 'nu', "Comedie", 5)
        service.adauga_spectacol(3, "da", 'nu', "Comedie", 5)
        spectacole=[Spectacol(1,"da", 'nu', "comedie", 2),Spectacol(2,"da", 'nu', "comedie", 2),Spectacol(3,"da", 'nu', "comedie", 2)]
        assert spectacole==service.get_all()
        assert service.__len__()==3
        service.adauga_random()
        assert service.__len__()==4
        service.export('fisier_test')




