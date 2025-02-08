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



# INTERFACE
raiz = ctk.CTk()
raiz.title("SISTEMA DE AGENDAMENTO MÉDICO")
raiz.geometry("1000x500")

consultas = []

titulo_label = ctk.CTkLabel(raiz, text="SISTEMA DE AGENDAMENTO DE CONSULTAS", font=("Arial", 24, "bold"))
titulo_label.pack(pady=(20, 10))


quadro_entradas = ctk.CTkFrame(raiz)
quadro_entradas.pack(pady=10, padx=40, fill="x")
ctk.CTkLabel(quadro_entradas, text="👤 Paciente:", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_nome = ctk.CTkEntry(quadro_entradas, width=200)
entrada_nome.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(quadro_entradas, text="🩺 Médico:", anchor="w").grid(row=0, column=2, padx=10, pady=5, sticky="w")
entrada_medico = ctk.CTkEntry(quadro_entradas, width=200)
entrada_medico.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(quadro_entradas, text="🕑 Início (HH:MM):", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entrada_inicio = ctk.CTkEntry(quadro_entradas, width=100)
entrada_inicio.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(quadro_entradas, text="🕑 Término (HH:MM):", anchor="w").grid(row=1, column=2, padx=10, pady=5, sticky="w")
entrada_fim = ctk.CTkEntry(quadro_entradas, width=100)
entrada_fim.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(quadro_entradas, text="Prioridade:", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entrada_prioridade = ctk.CTkComboBox(quadro_entradas, values=["Baixa", "Média", "Alta"], width=150)
entrada_prioridade.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
entrada_prioridade.set("Baixa")


tabela_frame = ctk.CTkFrame(raiz)
tabela_frame.pack(pady=10, padx=10, fill="both", expand=False)

tabela = ttk.Treeview(tabela_frame, columns=("Paciente", "Médico", "Prioridade", "Início", "Término"), show="headings", height=8)
tabela.pack(fill="both", expand=False)

tabela.heading("Paciente", text="Paciente")
tabela.heading("Médico", text="Médico")
tabela.heading("Prioridade", text="Prioridade")
tabela.heading("Início", text="Início")
tabela.heading("Término", text="Término")

raiz.mainloop()