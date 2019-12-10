'''
Created on 3 dic 2019

@author: g.fontana
'''
from fpdf import FPDF
 
import webbrowser
 
import os.path
from DbPoweri import DbPoweri
from time import gmtime, strftime 
 
class StampaPeso():
    
    def __init__(self):
        pass
            
    def testata(self, datai, dataf, datain , datafi):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=20)
        
        self.page=1
        pdf.cell(200, 10, txt="Riepilogo produzione:" +datai+"-"+dataf , ln=1, align="C")
         
        pdf.set_font("Arial", size=12)
        
        
        self.dettaglio(pdf, datain , datafi)   
        
        a=strftime("%Y-%m-%d %H-%M-%S", gmtime())
         
              
        if os.path.exists("C:\\temp\\StampaProduzionePeso"+a+".pdf")  is False:
            pdf.output( "C:\\temp\\StampaProduzionePeso"+a+".pdf","F").encode('latin-1')
            webbrowser.open_new_tab(r''  'C://temp//StampaProduzionePeso'+a+'.pdf')
        else:
            print ("error") 
            
            return
        
         
        
        #pdf.open()
        
        
    def dettaglio(self,pdf,datain, datafi):
        
        pdf.set_font('Arial', '', 10)
         
        
        c=DbPoweri()
        c.connection()
        rows, col_names=c.peso(c.c1, datain, datafi)
        rows1, col_namest=c.totpeso(c.c1, datain ,datafi)
         
        cod =""
        des=""
        gramm=""
        peso=""
        
        pdf.set_fill_color(192,192,192)
        pdf.cell(10, 10, 'Cod', 1, 0, 'C',fill = True)
        
        pdf.cell(40, 10, 'Qta_Grammatura', 1, 0, 'C',fill = True)
        pdf.cell(40, 10, 'Qta_KG', 1, 1, 'C',fill = True) 
         
         
        
        pdf.ln(0)
        
        nr=0
        posizione=0
        for riga in rows:
            posizione=posizione+1
           
            w_x=0
            for col in riga:
                w_x=w_x+1
                #print (col)
                #print (riga)
                
                if w_x==1:
                    cod=col
                
                if w_x==2:
                    gramm=col
                if w_x==3:
                    peso=col
            pdf.set_fill_color(192,192,192) 
            pdf.cell(10, 8, str(cod), 1, 0, 'L')
           
            pdf.cell(40, 8, str(gramm), 1, 0, 'R')
            pdf.cell(40, 8, str(peso), 1, 1, 'R')   
            
        for riga in rows1:
            posizione=posizione+1
           
            w_x=0
            for col in riga:
                w_x=w_x+1
                #print (col)
                #print (riga)
                
                if w_x==1:
                    gramm=col
                if w_x==2:
                    peso=col
                 
            pdf.cell(10, 8, "", 1, 0, 'L')  
            
            pdf.cell(40, 8, str(gramm), 1, 0, 'R')
            pdf.cell(40, 8, str(peso), 1, 1, 'R')     
  
