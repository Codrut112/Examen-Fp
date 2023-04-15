class ValidError(Exception):
    pass


class Validator():
    def valideaza(self,spectacol):
        '''
        functie de validare
        :param spectacol: spectacol
        :return: raise ValidError pt id negativ sau nul,titlu vid,artist vid ,durata necorespunzzatoare, si gen care nu e 'Comedie','Concert','Balet','Altele'
        '''
        erori=''
        if spectacol.get_id()<0:
            erori+='id invalid\n'
        if spectacol.get_titlu()=='':
            erori+='titlu invalid\n'
        if spectacol.get_artist()=='':
            erori+='artist invalid\n'
        if spectacol.get_gen() not in ['Comedie','Concert','Balet','Altele']:
            erori+='gen invalida\n'
        if spectacol.get_durata()<=0:
            erori+='durata invalida\n'
        if len(erori)>0:
            raise ValidError(erori)

