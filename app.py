from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {'id':1, 'charada': 'O que é um pontinho amarelo num iate?', 'resposta': 'Um milhonário'},
    {'id':2, 'charada': 'Qual é o filme que te ameaça de morte?', 'resposta': 'Vingadores eu-te-mato'},
    {'id':3, 'charada': 'Onde comprar comida para um super-herói?', 'resposta': 'No super-mercado'},
    {'id':4, 'charada': 'Por que o filho e a mulher do Hulk se separam dele?', 'resposta': 'Porque o Hulk estava verde e precisava ser mais maduro.'},
    {'id':5, 'charada': 'Qual a cidade Sul-americana que pende nos galhos da árvore?', 'resposta': 'Lima'},
    {'id':6, 'charada': 'O que é, o que é? Essa aqui não é bolinho. Adivinhe se puder: quanto mais quente ele está, mais fresco o danado é.', 'resposta': 'Pão.'},
    {'id':7, 'charada': 'Como um matemático come um X-Burger?', 'resposta': 'Ele começa pelo pão e pelo hambúrguer, só pra poder isolar o X'},
    {'id':8, 'charada': 'O que é um pontinho vermelho no meio da parede?', 'resposta': 'Uma acerola alpinista.'},
    {'id':9, 'charada': 'Qual é a fruta que nunca reprova?', 'resposta': 'Uva passa.'},
    {'id':10, 'charada': 'Por que a terra é virgem?', 'resposta': 'Porque a minhoca é mole e o vento é fresco.'}
]

@app.route('/')
def index():
    return 'API TÁ ON'

@app.route('/charada', methods=['GET'])
def charada():
    numero_aleatorio = random.randint(0, 9)
    charada_aleatoria = charadas[numero_aleatorio]

    return jsonify(charada_aleatoria), 200

@app.route('/charada/<int:id>', methods=['GET'])
def busca(id):
    for charada in charadas:
        if charada["id"] == id:
            return jsonify(charada), 200
    else:
        return jsonify({'mensagem': 'Erro! Charada não encontrada!'}), 404
if __name__ == '__main__':
    app.run()