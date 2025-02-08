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