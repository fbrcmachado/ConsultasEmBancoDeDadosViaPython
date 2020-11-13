class Credenciais():
    
    ##  Desta forma temos tudo centralizado em um local, a classe Repository irá chamar as credenciais corretas
    
    def GetCredenciaisBanco1(self):
        self.username = "LOGIN"
        self.password = "SENHA"
        self.driver="DRIVE DE BANCO DE DADOS"
        self.server="SERVER"
        self.database="NOME DO BANCO"
        return self
    
      def GetCredenciaisBanco2(self):
        self.username = "LOGIN"
        self.password = "SENHA"
        self.driver="DRIVE DE BANCO DE DADOS"
        self.server="SERVER"
        self.database="NOME DO BANCO"
        return self
    
 
    
