from trafilatura import extract

downloaded_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Example Page</title>
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is some text in a paragraph.</p>
    <aside>This is some text in a sidebar.</aside>
    <p>This is more text in another paragraph.</p>
    <footer>This is a footer.</footer>
</body>
</html>
"""

extracted_text = extract(downloaded_html)

print(extracted_text)

# Вывод:
# This is a heading
# This is some text in a paragraph.
# This is more text in another paragraph.

from trafilatura import fetch_url

url = "https://www.example.com" #  Замените на реальный URL

try:
    extracted_text = fetch_url(url)
    if extracted_text:
        print(extracted_text)
    else:
        print("Не удалось извлечь текст с URL")
except Exception as e:
    print(f"Произошла ошибка: {e}")


from trafilatura import bare_extraction

extracted_text_with_metadata = bare_extraction(downloaded_html, include_comments=False, include_tables=True, deduplicate=True)
print(extracted_text_with_metadata)

# Пример вывода (может варьироваться в зависимости от контента страницы):
# {'title': 'Example Page', 'text': 'This is a heading\nThis is some text in a paragraph.\nThis is more text in another paragraph.', 'author': None, 'url': None, 'hostname': None, 'description': None, 'date': None}