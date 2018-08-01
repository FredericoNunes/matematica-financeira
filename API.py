from Financeira import Financeira as fn

from flask import Flask , jsonify, request

app = Flask(__name__)

@app.route('/Matematica/Financeira/ValorPresente',methods=['POST'])
def valorpresente():
    valores = request.get_json()
    teste_requisitos = ['valorFuturo','taxa','tempo','base']

    resposta = []
    for itens in valores:
        if not all(k in itens for k in teste_requisitos):
            resposta.append({"ValorPresente":
                                 'Erro: Valores Faltando ou Incorreto'
                             })
        else:
            resposta.append({"ValorPresente":
                                 fn().ValorPresente(itens['valorFuturo'],
                                               itens['taxa'],
                                               itens['tempo']/itens['base'])
                             })

    return jsonify(resposta), 200

@app.route('/Matematica/Financeira/ValorFuturo',methods=['POST'])
def valorfuturo():
    valores = request.get_json()
    teste_requisitos = ['valorPresente','taxa','tempo','base']

    resposta = []
    for itens in valores:
        if not all(k in itens for k in teste_requisitos):
            resposta.append({"ValorFuturo":
                                 'Erro: Valores Faltando ou Incorreto'
                             })
        else:
            resposta.append({"ValorFuturo":fn().ValorFuturo(itens['valorPresente'],itens['taxa'],itens['tempo']/itens['base'])})

    return jsonify(resposta), 200

@app.route('/Matematica/Financeira/Desconto',methods=['POST'])
def desconto():
    valores = request.get_json()
    teste_requisitos = ['valorNominal',
                        'taxa',
                        'tempo',
                        'base'
                        ]

    resposta = []
    for itens in valores:
        if not all(k in itens for k in teste_requisitos):
            resposta.append({"Desconto":
                                 'Erro: Valores Faltando ou Incorreto'})
        else:
            resposta.append({"Desconto":
                                 fn().Desconto(itens['valorNominal'],itens['taxa'],itens['tempo']/itens['base'])
                             })

    return jsonify(resposta), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


