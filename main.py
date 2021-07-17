# -*- coding: UTF-8 -*-
import webbrowser
import keyboard
import pyautogui
import json
import colorama
import os.path
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

def abrirPagina(url):
    webbrowser.open(url)

def EnableMacro():
    print(
        Fore.GREEN + f'{msgEnabledMacro}'.format(macro_KeyToEnable, macro_KeyToDisable).upper())
    while True:
        if keyboard.is_pressed(f'{macro_KeyToEnable}'):
            pyautogui.click(button='right', interval=macro_msDelay)
        if keyboard.is_pressed(f'{macro_KeyToDisable}'):
            print(Fore.RED + f'{msgDisabledMacro}'.upper())
            langMenu()

def langMenu():
    arquivo_json = open('languages.json', 'r', encoding='utf-8')
    data = json.loads(arquivo_json.read())

    global Menu
    global MenuOption0
    global MenuOption1
    global MenuOption2
    global MenuOption3
    global msgAutoStartEnabled
    global msgEnabledMacro
    global msgDisabledMacro
    global msgSettings

    Menu = data[f"{macro_CurrentLanguage}"][0]["menu"]
    MenuOption0 = data[f"{macro_CurrentLanguage}"][0]["menuOption0"]
    MenuOption1 = data[f"{macro_CurrentLanguage}"][0]["menuOption1"]
    MenuOption2 = data[f"{macro_CurrentLanguage}"][0]["menuOption2"]
    MenuOption3 = data[f"{macro_CurrentLanguage}"][0]["menuOption3"]
    msgAutoStartEnabled = data[f"{macro_CurrentLanguage}"][0]["msgAutoStartEnabled"]
    msgEnabledMacro = data[f"{macro_CurrentLanguage}"][0]["msgEnabledMacro"]
    msgDisabledMacro = data[f"{macro_CurrentLanguage}"][0]["msgDisabledMacro"]
    msgSettings = data[f"{macro_CurrentLanguage}"][0]["msgCurrentSettings"]
    msgTutorial = data[f"{macro_CurrentLanguage}"][0]["msgTutorial"]

    funChangeLanguage = data[f"{macro_CurrentLanguage}"][0]["funChangeLanguage"]
    funChangeAutoStart = data[f"{macro_CurrentLanguage}"][0]["funChangeAutoStart"]
    funmsChange = data[f"{macro_CurrentLanguage}"][0]["funmsChange"]
    funKeyChange = data[f"{macro_CurrentLanguage}"][0]["funKeyChange"]
    funKeyToDisable = data[f"{macro_CurrentLanguage}"][0]["funKeyToDisable"]

    msgSuccess = data[f"{macro_CurrentLanguage}"][0]["msgSuccess"]

    option = input(f'{Menu}')

    if option in MenuOption0:
        EnableMacro()
    elif option in MenuOption1:
        print(Fore.BLUE +  f'{msgSettings}'.format(macro_CurrentLanguage, macro_AutoStart, macro_msDelay,
                                                        macro_KeyToEnable, macro_KeyToDisable))
        changeLanguage = input(f'{funChangeLanguage}')
        changeAutoStart = input(f'{funChangeAutoStart}')
        msChange = input(f'{funmsChange}')
        keyChange = input(f'{funKeyChange}')
        KeyToDisable = input(f'{funKeyToDisable}')
        data = {}
        data['Settings'] = []
        data['Settings'].append({
            'CurrentLanguage': f'{changeLanguage}',
            'AutoStartMacro': f'{changeAutoStart}',
            'msDelay': f'{msChange}',
            'KeyToEnable': f'{keyChange}',
            'KeyToDisable': f'{KeyToDisable}'
        })
        with open('settings.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)
        print(f'{msgSuccess}')
        LoadSettings()
        langMenu()
    elif option in MenuOption2:
        print(Fore.YELLOW + f'{msgTutorial}'.format(macro_KeyToEnable, macro_KeyToDisable))
        input('Press Enter to continue...')
        langMenu()
    elif option in MenuOption3:
        abrirPagina('http://steamcommunity.com/profiles/76561198405044969')
        langMenu()

def LoadSettings():
    if os.path.isfile('settings.json'):
        arquivo_json = open('settings.json', 'r', encoding='utf-8')
        data = json.loads(arquivo_json.read())
    else:
        arquivo_json = f = open('settings.json', 'a', encoding='utf-8')
        data = {}
        data['Settings'] = []
        data['Settings'].append({
            'CurrentLanguage': 'ptbr',
            'AutoStartMacro': 'no',
            'msDelay': f'0.25',
            'KeyToEnable': f'Q',
            'KeyToDisable': f'E'
        })
        with open('settings.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)

    if os.path.isfile('languages.json'):
        arquivo_json = open('settings.json', 'r', encoding='utf-8')
        data = json.loads(arquivo_json.read())
    else:
        arquivo_json = f = open('languages.json', 'a', encoding='utf-8')
        data = {}
        data['ptbr'] = []
        data['ptbr'].append({
            'menu': 'Menu:\n0 - Ativar\n1 - Alterar Configurações\n2 - Tutorial\n3 - Criador do Programa\nDigite: ',
            'menuOption0': ['0', 'ativar', 'Ativar', 'ATIVAR'],
            'menuOption1': ['1', 'alterar configurações', 'Alterar Configurações', 'ALTERAR CONFIGURAÇÕES',
                            'alterar configuracoes', 'alterar configurações'],
            'menuOption2': ['2', 'tutorial', 'Tutorial', 'TUTORIAL'],
            'menuOption3': ['3', 'criador do programa', 'Criador do Programa', 'CRIADOR DO PROGRAMA'],
            'msgAutoStartEnabled': 'Macro foi iniciado automaticamente por causa da função AutoStartMacro está configurada como: {}',
            'msgEnabledMacro': 'Macro ativado com sucesso, para utilizar pressione: {}. OU, Desativar pressione: {}',
            'msgDisabledMacro': 'Macro desativado com sucesso!',
            'msgCurrentSettings': 'Atual Configurações:\nIdioma: {}\nAutomaticamente iniciar Macro: {}\nDelay do Macro: {}\nTecla para Utilizar: {}\nTecla para Desabilitar: {}',
            'msgTutorial': 'Ativar o Macro: {}, Desativar: {}',
            'funChangeLanguage': 'Escolha seu idioma: ',
            'funChangeAutoStart': 'Auto iniciar Macro: ',
            'funmsChange': 'Quanto de MS (exemplo - 0.25): ',
            'funKeyChange': 'Tecla para utilizar o macro: ',
            'funKeyToDisable': 'Tecla para desativar o macro: ',
            'msgSuccess': 'As configurações foram alteradas com sucesso! Voltaremos ao menu principal.'
        })
        data['en'] = []
        data['en'].append({
            'menu': 'Menu:\n0 - Enable\n1 - Change Settings\n2 - Tutorial\n3 - Program developer\nYour choice: ',
            'menuOption0': ['0', 'enable', 'Enable', 'ENABLE'],
            'menuOption1': ['1', 'change settings', 'Change Settings', 'CHANGE SETTINGS'],
            'menuOption2': ['2', 'tutorial', 'Tutorial', 'TUTORIAL'],
            'menuOption3': ['3', 'program developer', 'Programa Developer', 'PROGRAMA DEVELOPER', 'dev'],
            'msgAutoStartEnabled': 'The macro was started automatically because the AutoStartMacro function is configured as: {}',
            'msgEnabledMacro': 'Macro successfully activated, to use press: {}. OR, Disable press: {}',
            'msgDisabledMacro': 'Macro deactivated successfully!',
            'msgCurrentSettings': 'Current Settings:\nLanguage: {}\nAutomatically start Macro: {}\nMacro Delay: {}\nKey to Use: {}\nDisable key: {}',
            'msgTutorial': '\nEnable Macro: {}, Disable Macro:{}',
            'funChangeLanguage': 'Choose your language: ',
            'funChangeAutoStart': 'Auto start Macro: ',
            'funmsChange': 'How much MS (example - 0.25): ',
            'funKeyChange': 'Key to use the macro: ',
            'funKeyToDisable': 'Key to disable macro: ',
            'msgSuccess': 'The settings have been successfully changed! We will return to the main menu.'
        })
        data['custom'] = []
        data['custom'].append({
            'menu': 'Menu:\n0 - Enable\n1 - Change Settings\n2 - Tutorial\n3 - Program developer\nYour choice: ',
            'menuOption0': ['0', 'enable', 'Enable', 'ENABLE'],
            'menuOption1': ['1', 'change settings', 'Change Settings', 'CHANGE SETTINGS'],
            'menuOption2': ['2', 'tutorial', 'Tutorial', 'TUTORIAL'],
            'menuOption3': ['3', 'program developer', 'Programa Developer', 'PROGRAMA DEVELOPER', 'dev'],
            'msgAutoStartEnabled': 'The macro was started automatically because the AutoStartMacro function is configured as: {}',
            'msgEnabledMacro': 'Macro successfully activated, to use press: {}. OR, Disable press: {}',
            'msgDisabledMacro': 'Macro deactivated successfully!',
            'msgCurrentSettings': 'Current Settings:\nLanguage: {}\nAutomatically start Macro: {}\nMacro Delay: {}\nKey to Use: {}\nDisable key: {}',
            'msgTutorial': '\nEnable Macro: {}, Disable Macro:{}',
            'funChangeLanguage': 'Choose your language: ',
            'funChangeAutoStart': 'Auto start Macro: ',
            'funmsChange': 'How much MS (example - 0.25): ',
            'funKeyChange': 'Key to use the macro: ',
            'funKeyToDisable': 'Key to disable macro: ',
            'msgSuccess': 'The settings have been successfully changed! We will return to the main menu.'
        })
        with open('languages.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)

    global macro_CurrentLanguage
    global macro_AutoStart
    global macro_msDelay
    global macro_KeyToEnable
    global macro_KeyToDisable

    macro_CurrentLanguage = data['Settings'][0]['CurrentLanguage']
    macro_AutoStart = data['Settings'][0]['AutoStartMacro']
    msDelay = data['Settings'][0]['msDelay']
    macro_msDelay = float(msDelay)
    macro_KeyToEnable = data['Settings'][0]['KeyToEnable']
    macro_KeyToDisable = data['Settings'][0]['KeyToDisable']

LoadSettings()
if macro_AutoStart in ['1', 'yes', 'YES', 'Yes', 'sim', 'Sim', 'SIM', "true"]:
    EnableMacro()
else:
    langMenu()