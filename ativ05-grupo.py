import random
import time
import pandas as pd
import streamlit as st

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================
st.set_page_config(
    page_title="Algoritmos de Ordenação",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Comparação de Algoritmos de Ordenação")

st.write("Este projeto compara o tempo de execução dos algoritmos:")

# =====================================================
# RANDOM FIXO
# =====================================================
random.seed(10)

# =====================================================
# GERANDO VETORES
# =====================================================
vetor_20 = [random.randint(1, 1000) for _ in range(20)]
vetor_100 = [random.randint(1, 1000) for _ in range(100)]
vetor_200 = [random.randint(1, 1000) for _ in range(200)]
vetor_1000 = [random.randint(1, 1000) for _ in range(1000)]
vetor_5000 = [random.randint(1, 1000) for _ in range(5000)]

# =====================================================
# ALGORITMOS DE ORDENAÇÃO
# =====================================================
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# =====================================================
# FUNÇÃO PARA MEDIR TEMPO
# =====================================================
def medir_tempo(funcao, vetor, inplace=True):
    copia = vetor.copy()
    inicio = time.perf_counter()
    if inplace:
        funcao(copia)
    else:
        copia = funcao(copia)
    fim = time.perf_counter()
    return fim - inicio

# =====================================================
# MEDIÇÕES
# =====================================================
dados = {
    "Algoritmo": ["Bubble", "Selection", "Insertion", "Merge", "Quick", "Python sorted"],

    "20 números": [
        medir_tempo(bubble_sort, vetor_20),
        medir_tempo(selection_sort, vetor_20),
        medir_tempo(insertion_sort, vetor_20),
        medir_tempo(merge_sort, vetor_20),
        medir_tempo(quick_sort, vetor_20, inplace=False),
        medir_tempo(sorted, vetor_20, inplace=False)
    ],

    "100 números": [
        medir_tempo(bubble_sort, vetor_100),
        medir_tempo(selection_sort, vetor_100),
        medir_tempo(insertion_sort, vetor_100),
        medir_tempo(merge_sort, vetor_100),
        medir_tempo(quick_sort, vetor_100, inplace=False),
        medir_tempo(sorted, vetor_100, inplace=False)
    ],

    "200 números": [
        medir_tempo(bubble_sort, vetor_200),
        medir_tempo(selection_sort, vetor_200),
        medir_tempo(insertion_sort, vetor_200),
        medir_tempo(merge_sort, vetor_200),
        medir_tempo(quick_sort, vetor_200, inplace=False),
        medir_tempo(sorted, vetor_200, inplace=False)
    ],

    "1000 números": [
        medir_tempo(bubble_sort, vetor_1000),
        medir_tempo(selection_sort, vetor_1000),
        medir_tempo(insertion_sort, vetor_1000),
        medir_tempo(merge_sort, vetor_1000),
        medir_tempo(quick_sort, vetor_1000, inplace=False),
        medir_tempo(sorted, vetor_1000, inplace=False)
    ],

    "5000 números": [
        medir_tempo(bubble_sort, vetor_5000),
        medir_tempo(selection_sort, vetor_5000),
        medir_tempo(insertion_sort, vetor_5000),
        medir_tempo(merge_sort, vetor_5000),
        medir_tempo(quick_sort, vetor_5000, inplace=False),
        medir_tempo(sorted, vetor_5000, inplace=False)
    ]
}

# =====================================================
# DATAFRAME
# =====================================================
df = pd.DataFrame(dados)

# =====================================================
# TABELA
# =====================================================
st.subheader("📋 Tabela de Tempos")

st.dataframe(df.style.format({
    "20 números": "{:.6f}",
    "100 números": "{:.6f}",
    "200 números": "{:.6f}",
    "1000 números": "{:.6f}",
    "5000 números": "{:.6f}"
}), use_container_width=True)

# =====================================================
# GRÁFICO
# =====================================================
st.subheader("📈 Comparação dos Algoritmos")

grafico_df = df.set_index("Algoritmo").T
st.line_chart(grafico_df)

# =====================================================
# EXEMPLO DE ORDENAÇÃO
# =====================================================
st.subheader("🔎 Exemplo de Ordenação")

st.write("Vetor original:")
st.write(vetor_20)

for alg, func in [("Bubble Sort", bubble_sort),
                  ("Selection Sort", selection_sort),
                  ("Insertion Sort", insertion_sort),
                  ("Merge Sort", merge_sort),
                  ("Quick Sort", quick_sort),
                  ("Python sorted", sorted)]:
    st.write(alg + ":")
    st.write(func(vetor_20.copy()))

# =====================================================
# RODAPÉ
# =====================================================
st.success("Análise concluída com sucesso ✅")
