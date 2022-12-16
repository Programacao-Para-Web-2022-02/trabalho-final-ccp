import bd
from flask import Flask, render_template, request,redirect, session
import random

app = Flask(__name__)


@app.route('/index', methods=['GET','POST'])
def index():
   
    comando = "SELECT * FROM Usuario;"


    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
     banco = bd.SQL( ) 
     msg= ''
     comando = "select cod_usur from Usuario where usur_email = %s and senha = %s"
     result = banco.consultar(comando, [request.form['email'], request.form['senha']]).fetchone()
    
     if result == None:
        msg = ''' <div class="msg-e">
                           <p>Usuario não cadastrado<p>
                        </div>
        '''
        return render_template('index.html', msg = msg)
     else:
         session['email'] = request.form['email']
         session['senha'] = request.form['senha']
         session['cod_usur'] = result[0]
         return redirect (f"/profile/{result[0]}")
     

        
    

@app.route('/profile/<cod_usur>',methods=['GET', 'POST'] )
def profile(cod_usur):
    banco = bd.SQL( ) 
    if request.method == 'POST':
     comnt = "insert into comentario (autor_cod_usur,Usuario_cod_usur,comenta) values ( %s ,%s,%s)"
     banco.executar(comnt,[session['cod_usur'],cod_usur,request.form['comenta']])
   

    query = 'select c.comenta, u.nme_usur, c.autor_cod_usur  from comentario c inner join  Usuario u on  autor_cod_usur  = cod_usur where c.Usuario_cod_usur = %s ; '
    cs = banco.consultar(query,[cod_usur]) 
    cm= " "
    form =f'<form action="/profile/{cod_usur}" method="post" >'
    
   
    
    for (comenta,nme_usur,autor_cod_usur ) in cs:
        cm += f'<div><div class="nome"><i class="fa-solid fa-user orkut-font-color"></i>{nme_usur}</div> <div>{comenta}<i class="fa-solid fa-pen orkut-font-color"></i></div> </div>'

    


    return render_template('profile.html', cm = cm, form = form )

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.run(debug=1)





