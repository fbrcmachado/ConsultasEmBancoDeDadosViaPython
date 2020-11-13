import pyodbc as pdb
import pandas as pd
from credenciais_acesso import Credenciais as cr



class Repository(object):

    def base(self, QUERY, contexto):
         if contexto == "banco1":
            credenciaisContexo = cr.GetCredenciaisBanco1(self)
         else :
            credenciaisContexo = cr.GetCredenciaisBanco2(self)
            
         with pdb.connect(
                'DRIVER=' + credenciaisContexo.driver + 
                ';SERVER=' + credenciaisContexo.server + 
                ';PORT=1433;DATABASE=' + credenciaisContexo.database + 
                ';UID=' + credenciaisContexo.username + 
                ';PWD=' + credenciaisContexo.password) as conn:
            consulta = pd.read_sql(QUERY, conn)
         return consulta
    
   