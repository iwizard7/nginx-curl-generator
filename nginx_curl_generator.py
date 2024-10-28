import re

# Запросить путь к файлу
file_path = input("Введите путь к файлу конфигурации: ")

# Запросить путь для сохранения выходного файла
output_file_path = input("Введите путь для сохранения запросов (например, output.txt): ")

# Инициализация переменных
server_name = ""
variables = {}
endpoints = []
missing_vars = set()

# Открытие и чтение файла
with open(file_path, 'r') as file:
    lines = file.readlines()

    parsing_vars = False
    parsing_endpoints = False

    # Обработка строк файла
    for line in lines:
        line = line.strip()

        # Определение server_name
        if line.startswith("server_name:"):
            server_name = line.split("server_name:")[1].strip()

        # Начало раздела с переменными
        elif line == "---" and not parsing_vars:
            parsing_vars = True
        elif line == "---" and parsing_vars:
            parsing_vars = False
            parsing_endpoints = True

        # Извлечение переменных
        elif parsing_vars and "=" in line:
            var_name, var_value = line.split("=")
            variables[var_name.strip()] = var_value.strip()

        # Извлечение методов и эндпоинтов
        elif parsing_endpoints and line.startswith(("GET", "POST")):
            method, endpoint = line.split(" ", 1)
            endpoints.append((method, endpoint.strip()))

# Генерация команд curl
curl_commands = []
for method, endpoint in endpoints:
    # Ищем все переменные в формате {var}
    endpoint_vars = re.findall(r"\{([a-zA-Z0-9_]+)(?::[a-zA-Z]+)?\}", endpoint)

    # Проверка на существование всех необходимых переменных
    for var in endpoint_vars:
        var_placeholder = "{" + var + "}"
        if var_placeholder in variables:
            # Замена переменной в эндпоинте
            endpoint = endpoint.replace(var_placeholder, variables[var_placeholder])
        else:
            # Если переменной нет, добавить в список пропущенных переменных
            missing_vars.add(var)

    # Формирование команды curl
    curl_command = f"curl -X {method} https://{server_name}/{endpoint}"
    curl_commands.append(curl_command)

# Вывод команд curl
for command in curl_commands:
    print(command)

# Сохранение команд в файл
with open(output_file_path, 'w') as output_file:
    for command in curl_commands:
        output_file.write(command + '\n')

# Сообщение о пропущенных переменных
if missing_vars:
    print("\nПропущенные переменные:")
    for var in missing_vars:
        print(f"- {var}")

print(f"\nЗапросы сохранены в файл: {output_file_path}")
