#Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
# Написать две функции, одна переводит слово с английского на русский, где слово - это входной параметр,
# вторая функция - с русского на английский.
dictionary_eng_ru = {"apple": "яблоко", "lesson" : "урок", "you": "ты", "we": "мы"}
def translate_ru_eng(word):
    dictionary_reversed = {value:key for key, value  in dictionary_eng_ru.items()}
    translated_word = dictionary_reversed.get(word, "translation not found")
    print(translated_word)
translate_ru_eng("он")

def translate_eng_ru(word):
    translated_word = dictionary_eng_ru.get(word, "translation not found")
    print(translated_word)
translate_eng_ru("lol")