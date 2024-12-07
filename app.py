from flask import Flask, render_template, request

app = Flask(__name__)

# Словарь для замены символов
replace_dict = {
    'й': '£', 'ц': '™', 'у': '%', 'к': '€', 'е': '∏', 'н': '^',
    'г': '●', 'ш': '[', 'щ': ']', 'з': '§', 'х': '®', 'ъ': '<',
    'ф': '©', 'ы': '>', 'в': 'I', 'а': '~', 'п': '=', 'р': '{',
    'о': '○', 'л': '$', 'д': '√', 'ж': '✕', 'э': '@', 'я': '&',
    'ч': '∨', 'с': '}', 'м': '¢', 'и': '▽', 'т': ':', 'ь': '#',
    'б': '/', 'ю': '₽'
}

# Обратный словарь для повторной замены
replace_back_dict = {value: key for key, value in replace_dict.items()}


def replace_text(text: str, replacements: dict) -> str:
    """Функция для замены символов согласно указанному словарю."""
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['text']
        # Проверяем, является ли введенное сообщение закодированным
        decoded = replace_text(user_input, replace_back_dict)
        if user_input == decoded:  # Если это не было декодировано, значит это исходный текст
            result = replace_text(user_input, replace_dict)
            return render_template('index.html', result=f'Закодированное сообщение: {result}', input=user_input)
        else:  # Иначе это закодированное сообщение
            result = decoded
            return render_template('index.html', result=f'Декодированное сообщение: {result}', input=user_input)
    return render_template('index.html', result='', input='')


if __name__ == '__main__':
    app.run(debug=True)