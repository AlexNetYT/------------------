import eel
import os
import urllib.request

from convert import convert
eel.init('web')

TEMPLATE_NAME = "template.xlsx"
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), TEMPLATE_NAME)
if not os.path.exists(TEMPLATE_PATH):
        print( f"❌ Не найден шаблон {TEMPLATE_NAME} в директории программы. Скачиваю...")
        urllib.request.urlretrieve("https://github.com/AlexNetYT/------------------/raw/refs/heads/main/template.xlsx", "template.xlsx")
    
@eel.expose
def start_conversion(plan_path):
    print("AAA")
    print(plan_path)
    # try:
    fp = convert(plan_path)
    
    return f"✅ Конвертация завершена! Файл сохранён: {fp}"
    # except Exception as e:
    #     return f"❌ Ошибка: {str(e)}"

eel.start('index.html', size=(600, 400))
