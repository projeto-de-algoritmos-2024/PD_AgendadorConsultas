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
    dp = [0] * (n + 1)
    prev = [-1] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if consultas_ordenadas[j][1] <= consultas_ordenadas[i][0]:
                prev[i] = j
                break

    for i in range(1, n + 1):
        peso_atual = consultas_ordenadas[i - 1][4]
        if prev[i - 1] != -1:
            peso_atual += dp[prev[i - 1] + 1]
        dp[i] = max(peso_atual, dp[i - 1])

    i = n
    resultado = []
    while i > 0:
        if i == 1 or dp[i] > dp[i - 1]: 
            resultado.append(consultas_ordenadas[i - 1])
            if prev[i - 1] != -1:
                i = prev[i - 1] + 1 
            else:
                i = 0
        else:
            i -= 1

    return resultado[::-1]

def adicionar_consulta():
    try:
        nome_paciente = entrada_nome.get()
        nome_medico = entrada_medico.get()
        prioridade = entrada_prioridade.get()
        horario_inicio_str = entrada_inicio.get()
        horario_fim_str = entrada_fim.get()

        horario_inicio = converter_para_minutos(horario_inicio_str)
        horario_fim = converter_para_minutos(horario_fim_str)

        if horario_inicio is None or horario_fim is None:
            return
        if horario_inicio >= horario_fim:
            messagebox.showerror("Erro", "O horário de início deve ser menor que o de término!")
            return

        peso = PESOS.get(prioridade, 1)
        nova_consulta = (horario_inicio, horario_fim, nome_paciente, nome_medico, peso, prioridade)
        consultas.append(nova_consulta)
        
        tabela.insert("", "end", values=(nome_paciente, nome_medico, prioridade, horario_inicio_str, horario_fim_str))
        entrada_nome.delete(0, tk.END)
        entrada_medico.delete(0, tk.END)
        entrada_inicio.delete(0, tk.END)
        entrada_fim.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para os campos de horários!")
        
def calcular_agendamento_otimizado():
    if not consultas:
        messagebox.showerror("Erro", "Nenhuma consulta foi adicionada!")
        return

    melhor_agendamento = weighted_interval_scheduling(consultas)

    tabela.delete(*tabela.get_children())
    for i, (inicio, fim, paciente, medico, _, prioridade) in enumerate(melhor_agendamento, start=1):
        horario_inicio_str = f"{inicio // 60:02d}:{inicio % 60:02d}"
        horario_fim_str = f"{fim // 60:02d}:{fim % 60:02d}"
        tabela.insert("", "end", values=(paciente, medico, prioridade, horario_inicio_str, horario_fim_str))

def limpar_tabela():
    global consultas
    consultas.clear()
    tabela.delete(*tabela.get_children()) 
    
# INTERFACE
raiz = ctk.CTk()
raiz.title("SISTEMA DE AGENDAMENTO MÉDICO")
raiz.geometry("1000x530")

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

botao_adicionar = ctk.CTkButton(quadro_entradas, text="ADICIONAR CONSULTA", command=adicionar_consulta)
botao_adicionar.grid(row=2, column=2, columnspan=2, pady=15)

tabela_frame = ctk.CTkFrame(raiz)
tabela_frame.pack(pady=10, padx=10, fill="both", expand=False)

tabela = ttk.Treeview(tabela_frame, columns=("Paciente", "Médico", "Prioridade", "Início", "Término"), show="headings", height=8)
tabela.pack(fill="both", expand=False)

tabela.heading("Paciente", text="Paciente")
tabela.heading("Médico", text="Médico")
tabela.heading("Prioridade", text="Prioridade")
tabela.heading("Início", text="Início")
tabela.heading("Término", text="Término")

botao_calcular = ctk.CTkButton(raiz, text="EXIBIR AGENDA", command=calcular_agendamento_otimizado)
botao_calcular.pack(pady=10)

botao_limpar = ctk.CTkButton(raiz, text="LIMPAR TABELA", command=limpar_tabela)
botao_limpar.pack(pady=10)

raiz.mainloop()