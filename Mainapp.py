from flask import Flask, render_template
from flask import request
from datetime import date, timedelta 
#from flask_bootstrap import Bootstrap
from DbPoweri import DbPoweri
from StampaPeso import StampaPeso
 

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('/artebianca.html')

 
@app.route('/peso', methods=('GET', 'POST'))
def peso():
    #print (request.method)
    if request.method == 'POST':
        datain=request.form.getlist('datein')
        datafi=request.form.getlist('datefi')
        #print (datain, datafi)
        datai=request.form.getlist('datein')  
        dataf=request.form.getlist('datefi')
        datain='20'+datain[0][-2:]+datain[0][2:-2]+datain[0][:2]
        datafi='20'+datafi[0][-2:]+datafi[0][2:-2]+datafi[0][:2]
        #print (datain) 
        #print (datafi) 
        c=DbPoweri()
        c.connection()
        rows, col_names=c.peso(c.c1, datain ,datafi)
        rows1, col_namest=c.totpeso(c.c1, datain ,datafi)
        st=StampaPeso()
        st.testata(datai[0], dataf[0], datain, datafi)
         
    if request.method != 'POST'  : 
        #print ("get")
        dataric = date.today()
        datain = dataric.strftime('%Y%m%d')
        datafi = dataric.strftime('%Y%m%d')
        #print (datain)
        #print (datafi)
        c=DbPoweri()
        c.connection()
        rows, col_names=c.peso(c.c1, datain, datafi)
        rows1, col_namest=c.totpeso(c.c1, datain ,datafi)
        #print (rows1)
        
     
    if len(rows)>0    :     
        return render_template('/peso.html', len = len(rows), 
                               lenr = len(rows[0]), rows=rows, 
                               lent = len(col_names), lenrt = len(col_names[0]), rowst=col_names,
                               rows1=rows1)
        
     
    
                                