'''
Created on 07 mag 2018

@author: GianpieroF
'''
import pypyodbc
 
class DbPoweri():
     
    def __init__(self):
        super(DbPoweri, self).__init__()
        
    def connection(self):
        connection = pypyodbc.connect(driver='{iSeries Access ODBC Driver}',
                        system='192.168.0.251',uid='QPGMR',pwd='SCP2011')
        self.c1 = connection.cursor()
        #print ("cursor")
           
      
    def peso(self,c1, datain, datafi):
        
        stringa=("select cla5ma cod,   decimal(sum(qtmomm),11,0) Qta_Grammatura , "
                " decimal(sum(qtmomm*peunma), 11, 0)  Peso_Kg from ANT60DAT.mgmov00f  " +
                    " inner join ANT60dat.mgart00f on cddtma=cddtmm and cdarmm=cdarma " +
                     
                            
                    " where camomm='30' and cddtmm='01'"
                    "  and dtmomm between " + datain + " and " +datafi+ "" + 
                     " group by cla5ma " )    
            
        #print (stringa)
        c1.execute(stringa) 
        col_names = [x[0] for x in c1.description]  
        row = c1.fetchall()
         
        return row, col_names  
    def totpeso(self,c1, datain, datafi):
        
        stringa=("select   decimal(sum(qtmomm),11,0) Qta_Grammatura , "
                " decimal(sum(qtmomm*peunma), 11, 0)  Peso_Kg from ANT60DAT.mgmov00f  " +
                    " inner join ANT60DAT.mgart00f on cddtma=cddtmm and cdarmm=cdarma " +
                    
                            
                    " where camomm='30' and cddtmm='01'"
                    "  and dtmomm between " + datain + " and " +datafi+ "" + "")
                      
            
        #print (stringa)
        c1.execute(stringa) 
        col_names = [x[0] for x in c1.description]  
        row = c1.fetchall()
         
        return row, col_names  
 