import pandas as pd
import numpy as np
from pycaret.regression import *

df = pd.read_csv("fluxo_linhas_2023-2024.csv", sep=';')
df['ano_mes'] = df['Ano'] * 12 + df['Mês']
df['mes_sin'] = np.sin(2 * np.pi * df['Mês'] / 12)
df['mes_cos'] = np.cos(2 * np.pi * df['Mês'] / 12)
reg_setup = setup(
    data=df,
    target='Fluxo de Passageiros',
    session_id=42,
    numeric_features=['Linhas', 'Mês', 'Ano', 'ano_mes', 'mes_sin', 'mes_cos'],
    ignore_features=['MDU', 'MDO', 'MAX'],
    fold_strategy='timeseries',
    fold=5,
    fold_shuffle=False,
    data_split_shuffle=False,
    verbose=False
)
best_model = compare_models()
tuned_model = tune_model(best_model)
save_model(best_model, 'modelo_fluxo_passageiros')
print(f"\n✅ Melhor modelo ajustado:\n{tuned_model}")