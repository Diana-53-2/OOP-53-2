
#Импорт colorama
from colorama import init, Fore, Back, Style

# Инициализация colorama
init()

print(Fore.RED + 'текст красного цвета')  #Fore для получения цветного шрифта
print(Fore.GREEN + 'А этот зелёного')
print(Back.YELLOW + Fore.BLACK + 'Чёрный текст на жёлтом фоне')  #Back для цветного фона
print(Style.BRIGHT + 'Яркий текст')       #Style для того чтоб сделать жирным текст
print(Style.RESET_ALL + 'Сброс стилей и краски') # Style.RESET_ALL для сброса
