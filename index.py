
from flask import Flask, jsonify, request, json

app= Flask(__name__)

desenvolvedores=[
    {   
        'id': 0,
        'nome': 'Rosa',
        'habilidades':['javascript', 'python']
    },
     {  
        'id': 1,
        'nome': 'Cristina',
        'habilidades':['java', 'PHP']
    }
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem= 'Desenvolvedor de ID {} não existe'.format(id)
            response ={'status':'erro', 'mensagem':mensagem} 
        return jsonify(response)
    elif request.method == 'PUT':
        dados= json.loads(request.data)
        desenvolvedores[id]=dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'menssagem': 'registro excluido'})

@app.route('/devs', methods=['GET', 'POST'])
def desenvolvedorAll():
    if request.method == 'GET':
        return jsonify(desenvolvedores)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao= len(desenvolvedores)
        dados['id']= posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

if __name__ == '__main__':
    app.run(debug=True)    