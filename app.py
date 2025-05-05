
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from pycaret.regression import load_model, predict_model

app = Flask(__name__)
CORS(app)
model = load_model('modelo_fluxo_passageiros')


@app.route('/prever', methods=['POST'])
def prever():
    dados = request.json

    try:
        linha = int(dados['linha'])
        mes = int(dados['mes'])
        ano = int(dados['ano'])

        entrada = pd.DataFrame({
            'Linhas': [linha],
            'Mês': [mes],
            'Ano': [ano]
        })
        entrada['ano_mes'] = entrada['Ano'] * 12 + entrada['Mês']
        entrada['mes_sin'] = np.sin(2 * np.pi * entrada['Mês'] / 12)
        entrada['mes_cos'] = np.cos(2 * np.pi * entrada['Mês'] / 12)

        previsao = predict_model(model, data=entrada)
        fluxo = float(previsao['prediction_label'].iloc[0])

        return jsonify({
            'linha': linha,
            'mes': mes,
            'ano': ano,
            'previsao_passageiros': round(fluxo)
        })

    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)