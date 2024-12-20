from flask import Flask, request, jsonify

app = Flask(__name__)

# Limites críticos
LIMITE_CO2 = 1000
LIMITE_PM25 = 35

@app.route('/enviar_dados', methods=['POST'])
def enviar_dados():
    dados = request.json
    alertas = []
    if dados["CO2"] > LIMITE_CO2:
        alertas.append("⚠️ CO2 acima do limite crítico!")
    if dados["PM2.5"] > LIMITE_PM25:
        alertas.append("⚠️ PM2.5 acima do limite crítico!")
    
    return jsonify({
        "mensagem": "Dados recebidos com sucesso.",
        "alertas": alertas
    })

if __name__ == '__main__':
    app.run(debug=True)
