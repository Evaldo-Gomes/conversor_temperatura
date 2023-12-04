import PySimpleGUI as psg
from conversor import fah

layout = [
    [psg.Text('Temperatura em Celsius: '), psg.Input(key='Tc')],
    [psg.Text('', key='Valor')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
]

janela = psg.Window('Conversor de Temperaturas V1.0', layout)

while True:
    eventos, valores = janela.read()

    if eventos == psg.WIN_CLOSED:
        break
    elif eventos == 'Limpar':
        janela['Tc'].update('')
        janela['Valor'].update('')
        janela['Tc'].set_focus()
    else:
        n1 = int(valores['Tc'])
        total = fah(n1)
        janela['Valor'].update(total)
janela.close()
