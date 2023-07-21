#necessarios para criar a senha
import secrets
from random import randint
#necessaria para transformar em api
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/senha/<int:tamanho>',methods=['GET'])
def gerador_senha(tamanho):
    senha = []
    especiais = ["!","@",".","$","&","^",",", "*","/","_","¨","-","[","]","%","#"]
    senhaFinal = ''
    
    
    if tamanho < 6:
        tamanho = 6
    else:
        tamanho = tamanho

    secret = secrets.token_urlsafe(tamanho)
    esp1 = randint(0,len(especiais)-1)
    esp2 = randint(0,len(especiais)-1)
    esp3 = randint(0,len(especiais)-1)
    pos1 = randint(0,tamanho)
    pos2 = randint(0,tamanho)
    pos3 = randint(0,tamanho)

    for carac in secret:
        senha.append(carac)

    senha.insert(pos1,especiais[esp1])
    senha.insert(pos2,especiais[esp2])
    senha.insert(pos3,especiais[esp3])

    while(len(senha) != tamanho):
        senha.pop()
    senha.pop()
    senha.insert(len(senha)-1,especiais[esp3])
    for carac in senha:
        senhaFinal += carac
    
    senhaFinal = {"senha": senhaFinal,"tamanho":len(senhaFinal)}

    return senhaFinal

app.run(port=5000,host='localhost',debug=True)


