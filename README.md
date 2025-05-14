
# 🚇 Previsão de Passageiros no Metrô com IA

Este projeto aplica **Aprendizado de Máquina** para prever o número de passageiros transportados por linha, mês e ano, com base em dados históricos. A solução foi desenvolvida com **PyCaret**, **Flask** e uma interface web simples em **HTML + CSS**.

---

## 🔍 Objetivo

Permitir que o usuário informe uma **linha**, **mês** e **ano** e receba uma **previsão estimada de passageiros** para o período informado.

---

## 🧠 Tecnologias Utilizadas

- Python 3.x  
- PyCaret  
- Pandas  
- Flask  
- HTML5 + CSS3  
- JavaScript (Fetch API)  

---

## 📊 Treinamento do Modelo

- **Dataset**: `fluxo_linhas_2023-2024.csv`  
- **Colunas utilizadas**: `Linhas`, `Mês`, `Ano`, `Fluxo de Passageiros`  
- **Validação**: `TimeSeriesSplit`, 5 folds  
- **Seleção de modelo**: `compare_models()`  
- **Salvamento do modelo**:
  
```python
save_model(best_model, 'modelo_previsao_passageiros')
```

---

## 🌐 Interface Web

A interface permite ao usuário inserir:

- **Linha**: 1, 2, 3 ou 15  
- **Mês**: 1 a 12  
- **Ano**: Exemplo: 2025  

A previsão de passageiros será exibida diretamente na tela.

---

## ▶️ Como Executar

1. **Clone o repositório**:

```bash
git clone https://github.com/csclementino/metroflux-predictor.git
```

2. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

3. **Execute o script de treinamento do modelo (apenas na primeira vez ou quando atualizar os dados)**:

```bash
python treinar_modelo.py
```

4. **Execute o servidor Flask**:

```bash
python app.py
```

5. **Acesse no navegador**:

[http://localhost:5000](http://localhost:5000)

---

## 📁 Estrutura do Projeto

```
projeto/
├── app.py
├── fluxo_linhas_2023-2024.csv
├── style.css
├── index.html
├── requirements.txt
└── README.md
```

---

## 📬 Contato

Desenvolvido por **Carlos Clementino**  
🔗 [LinkedIn](https://www.linkedin.com/in/carlosclementino/)

---

⭐ Se curtir o projeto, deixe uma estrela no repositório!
