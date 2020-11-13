class Consultas():
    
    ## Essa classe serve para retornar o texto de uma consulta específica. Futuramente esse arquivo pode ser separado em vários, por contexto. 
    ## exemplo: todas as consultas de uma determinada tabela, todas as consultas de um determinado banco... com isso, caso o sistema cresça, as 
    ## consultas estarão centralizadas em um único ponto, facilitando a manutenção. 
    
    def GetAll():
        return "SELECT * FROM TABELA"
    
    
