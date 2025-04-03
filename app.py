import pandas as pd
import scipy.stats
import streamlit as st
import time

# Variables de estado
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])

st.header('Lanzar una moneda')
chart = st.line_chart([0.5])

def toss_coin(n):
    resultados = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    media = 0
    total = 0

    for i, r in enumerate(resultados, start=1):
        total += r
        media = total / i
        chart.add_rows([media])
        time.sleep(0.05)
    
    return media

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)

    nuevo_resultado = pd.DataFrame(
        [[st.session_state['experiment_no'], number_of_trials, mean]],
        columns=['no', 'iterations', 'mean']
    )

    st.session_state['df_experiment_results'] = pd.concat(
        [st.session_state['df_experiment_results'], nuevo_resultado],
        ignore_index=True
    )

st.write(st.session_state['df_experiment_results'])
