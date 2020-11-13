from conexao import Repository as rp
from consultas import Consultas as cn
from databases import Contextos as ctx

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