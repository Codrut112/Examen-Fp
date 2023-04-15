from business.service import Service
from infrastrucura.file_repo import File_Repo
from prezentare.consola import UI
from teste.teste import Teste
from validator.validator import Validator

teste=Teste()
teste.testare()
file_repo=File_Repo('spectacole')
validator=Validator()
service=Service(file_repo,validator)
ui=UI(service)
ui.run()