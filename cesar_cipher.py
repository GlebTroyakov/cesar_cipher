def open_file(filename):
    """Прочитать тестовый файл с именем 'filename' и вернуть
    содержимое как строку."""
    with open(filename, 'r', encoding='utf-8') as fh:
        return fh.read()


def save_file(filename, text):
    """Сохранить строку 'text' в текстовый файл с именем 'filename'."""
    with open(filename, 'w', encoding='utf-8') as fh:
        fh.write(text)


def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): свдиг.

    Результат:
        str: измененная строка."""
    # alfa = [chr(i) for i in range(ord('А'), ord('я') + 1)]  # Способ из примера - создает аллфавит сам
    alfa = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # Мой способ с Ёё
    new_text = ''
    # Создать 2 списка заглавнных и прописнных букв, проверять символ текста на up/low, сравнивать shift + index с 32
    if int(shift) > 33 or shift < 33:  # 32 if not Ёё
        shift = shift % 33  # 32 if not Ёё

    if int(shift) % 33 == 0:  # 32 if not Ёё
        print('Кодировка не возможна, смещение равно длине алфавита')

    for letter in text:
        if not letter.isalpha():
            new_text += letter
        else:
            if shift > 0:
                if letter.isupper() and (alfa.index(letter) + shift + 1) > 33:  # 32 if not Ёё
                    new_text += alfa[shift + alfa.index(letter) - 33]  # 32 if not Ёё
                elif letter.islower() and (alfa.index(letter) + shift + 1) > 66:  # 64 if not Ёё
                    new_text += alfa[shift + alfa.index(letter) - 33]  # 32 if not Ёё
                else:
                    new_text += alfa[alfa.index(letter) + shift]

            else:
                if alfa[alfa.index(letter) + shift].isupper() and letter.islower():
                    new_text += alfa[alfa.index(letter) + shift + 33]  # 32 if not Ёё
                elif alfa[alfa.index(letter) + shift].islower() and letter.isupper():
                    new_text += alfa[alfa.index(letter) + shift + 33]  # 32 if not Ёё
                else:
                    new_text += alfa[alfa.index(letter) + shift]

    return new_text


if __name__ == '__main__':
    # text = input('Text: ')
    # shift = int(input('Shift: '))
    text = 'Я иду домой. Эх как хорошо!'
    shift = 67
    encoded = ceasar(text, shift)
    print('text: ', text)
    print('Зашифрованая строка: ', encoded)
    decoded = ceasar(encoded, -shift)
    print('Расшифрованная строка: ', decoded)