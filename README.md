# Agendador de Consultas

**Número da Lista**: 06<br>
**Conteúdo da Disciplina**: Programação Dinâmica<br>

## [Para assistir a apresentação desta entrega, clique aqui!](https://www.youtube.com/watch?v=eo5aZXzX5LM&ab_channel=GabrielZaranza)

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0107243  |  Gabriel Pessoa Zaranza |
| 21/1063149  |  Izabella Alves Pereira |

## Sobre 

Este é um sistema de agendamento médico desenvolvido com Python. O sistema permite adicionar consultas, informando o paciente, médico, horário de início e término, e prioridade (baixa, média ou alta). A partir dessas informações, ele otimiza o agendamento das consultas, evitando sobreposição de horários e priorizando as de maior importância.

A otimização é feita por meio de programação dinâmica, utilizando a técnica de interval scheduling com pesos. A função weighted_interval_scheduling ordena as consultas pelo horário de término e calcula o melhor conjunto de consultas a serem agendadas, levando em conta as prioridades e os horários. 

## Screenshots
![a](https://github.com/projeto-de-algoritmos-2024/PD_AgendadorConsultas/blob/master/images/tela_vazia.png)
![a](https://github.com/projeto-de-algoritmos-2024/PD_AgendadorConsultas/blob/master/images/tela_preenchida.png)

## Instalação 
**Linguagem**: Python<br>
**Framework**: Nenhum (utiliza apenas a biblioteca CustomTkinter embutida no Python)<br>

1. Para rodar este projeto, é necessário ter o Python instalado. Além disso, você precisará instalar as bibliotecas customtkinter e tkinter:

```
pip install customtkinter
```

2. Clone ou baixe este repositório para o seu computador:

```
git clone https://github.com/projeto-de-algoritmos-2024/PD_AgendadorConsultas
cd PD_AgendadorConsultas
```

3. Execute o programa:
```
python main.py
```

## Uso 

1. Após executar o programa, a interface será exibida.

2. Preencha os campos obrigatórios:

    - Nome do paciente.
    - Nome do médico.
    - Horário de início e término da consulta.
    - Prioridade

3. Clique em "ADICIONAR CONSULTA" para salvar os dados.

4. Todas as consultas serão exibidas na tabela abaixo.

5. Para visualizar as consultas, considerando a sobreposição de horários e priorizando as de maior importância, clique no botão "EXIBIR AGENDA".
