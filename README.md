# Nginx Configuration Curl Generator ⚙️

Этот скрипт на Python позволяет извлекать параметры из конфигурационного файла Nginx и генерировать команды `curl` для тестирования API. Скрипт автоматически заменяет переменные на их значения и сохраняет сгенерированные команды в текстовый файл.

## Установка

Для запуска скрипта вам потребуется Python 3.6 или выше. Убедитесь, что у вас установлен Python, затем выполните следующие команды:

```bash
git clone https://github.com/yourusername/nginx-curl-generator.git
cd nginx-curl-generator
```
## Использование

Запустите скрипт:
```bash
python nginx_curl_generator.py
```
Введите путь к файлу конфигурации: Укажите полный путь к файлу конфигурации Nginx в формате:
```bash
server_name:example.com
---
vars:
{variableName}=value
...
---
METHOD endpoint
```
Укажите путь для сохранения выходного файла: Укажите полный путь, где хотите сохранить сгенерированные команды curl, например, output.txt.
Пример формата конфигурационного файла

## Пример содержимого файла конфигурации Nginx:
```bash
server_name: test-server.com
---
vars:
{env1}=5902b97c-e5cc-4ca5-a051-1666e9dc560a
{env2}=5902b97c-e5cc-4ca5-a051-1666e9dc560a
---
POST api/account/signinstage
GET api/account/current
GET api/clients/positions/{env1}
```
## Пример выходных данных

После выполнения скрипта в указанный файл будут сохранены команды curl:

```bash
curl -X POST https://test-server.com/api/account/signinstage
curl -X GET https://test-server.com/api/account/current
curl -X GET https://test-server.com/api/clients/positions/5902b97c-e5cc-4ca5-a051-1666e9dc560a
```
## Обработка пропущенных переменных

Если в конфигурации отсутствуют значения для некоторых переменных, скрипт выведет сообщение об этом:
```bash
Пропущенные переменные:
- {id}
```
## Зависимости

На данный момент скрипт не требует дополнительных библиотек, но убедитесь, что у вас установлен Python.