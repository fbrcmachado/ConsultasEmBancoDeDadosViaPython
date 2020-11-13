from conexao import Repository as rp
from consultas import Consultas as cn
from databases import Contextos as ctx

## Esse arquivo possui as chamadas da consulta. Ele poderia ser dividido em dois, inclusive; um com a classe Consulta e um com as chamadas dessa classe, a qual funcionaria como 
## uma controller do MVC (apenas com as chamadas).Na classe Consultas temos um construtor das credenciais da consulta e um método chamado RetornaDados. Ele faz a chamada na repository
## do metodo base, que serve para executar as consultas, passando como  parametro o construtor self, o texto da consulta (resultado da chamada do método GetAll) e o contexto (retronado
## pelo método Banco1() - que retornará no caso o banco 1)
## Fora da classe, temos apenas a chamada do método RetornaDados(), armazenado na variável x. 
class Consulta(object):
     def __init__(self):
         self.password = ""
         self.server = ""
         self.database = ""
         self.username = ""
         self.driver = ""
    
     def RetornaDados(self):
         x = rp.base(self, cn.GetAll(), ctx.Banco1())
         return x
 

x = Consulta().RetornaDados()
