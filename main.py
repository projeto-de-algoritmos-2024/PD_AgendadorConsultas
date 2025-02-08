import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

PESOS = {"Baixa": 1, "Média": 2, "Alta": 3}

def converter_para_minutos(horario_str):
    try:
        horario_obj = datetime.strptime(horario_str, "%H:%M")
        return horario_obj.hour * 60 + horario_obj.minute
    except ValueError:
        messagebox.showerror("Erro", f"Horário inválido: {horario_str}. Use o formato HH:MM.")
        return None
    
def weighted_interval_scheduling(consultas):
    consultas_ordenadas = sorted(consultas, key=lambda x: x[1])
    n = len(consultas_ordenadas)
    dp = [0] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if consultas_ordenadas[j][1] <= consultas_ordenadas[i][0]:
                prev[i] = j
                break

    for i in range(n):
        peso_atual = consultas_ordenadas[i][4]
        if prev[i] != -1:
            peso_atual += dp[prev[i]]
        dp[i] = max(peso_atual, dp[i - 1] if i > 0 else 0)

    i = n - 1
    resultado = []
    while i >= 0:
        if prev[i] == -1 or (dp[i] > dp[i - 1] if i > 0 else True):
            resultado.append(consultas_ordenadas[i])
            i = prev[i]
        else:
            i -= 1

    return resultado[::-1] 