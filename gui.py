import eel
import os
import urllib


eel.init('web')

TEMPLATE_NAME = "template.xlsx"
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), TEMPLATE_NAME)

@eel.expose
def start_conversion(plan_path, save_dir):
    if not os.path.exists(TEMPLATE_PATH):
        print( f"❌ Не найден шаблон {TEMPLATE_NAME} в директории программы. Скачиваю...")
        template_file = urllib.URLopener()
        template_file.retrieve("http://randomsite.com/file.gz", "file.gz")
        


    try:
        
        return "✅ Конвертация завершена!"
    except Exception as e:
        return f"❌ Ошибка: {str(e)}"

eel.start('index.html', size=(600, 400))
