from bs4 import BeautifulSoup
import sys
import excel
from rich import *
try:
    with open(sys.argv[1], 'r', encoding="utf8") as file:
        html = file.read()
except IndexError:
    print("[red]❌  Please provide the HTML file path as an argument. || Пожалуста, укажите путь к HTML-файлу в качестве аргумента.  ❌[/red]")
    os.system('pause')
    sys.exit(1)
import os
import urllib.request
TEMPLATE_PATH = "template.xlsx"

if not os.path.exists(TEMPLATE_PATH):
        print( f"❌ Не найден шаблон {TEMPLATE_PATH} в директории программы. Скачиваю...")
        urllib.request.urlretrieve("https://github.com/AlexNetYT/------------------/raw/refs/heads/main/template.xlsx", "template.xlsx")
    
soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('tr')

fpln = []

for row in rows[1:]:
    cells = row.find_all('td')
    
    ident = cells[1].text.strip()
    name = cells[2].text.strip()
    if name != '': ident = ident +" - " + name
    procedure = cells[3].text.strip()
    hdg = int(cells[9].text.strip()) if cells[9].text.strip() != '' else ''
    distance_nm =  '' if cells[10].text.strip() == '' else float(cells[10].text.strip().replace(',', '.'))
    wind_degree_m_kts = cells[16].text.strip()
    wind_lst = cells[17].text.strip().split(' ') if cells[17].text.strip() != "" else ["","0"]
    head_or_tailwind_kts = int("-"+wind_lst[1]) if wind_lst[0] == "⮟" else int(wind_lst[1])
    ident_freq_dist_bearing = cells[18].text.strip()
    fpln.append({"ident": ident, "name": name, "procedure": procedure, "hdg": hdg, "distance_nm": distance_nm, "wind_degree_m_kts": wind_degree_m_kts, "head_or_tailwind_kts": head_or_tailwind_kts, "ident_freq_dist_bearing": ident_freq_dist_bearing})
    print(f"[cyan]Ident: {ident}[/cyan], Distance: {distance_nm}, Heading: {hdg}, Wind: {wind_degree_m_kts}, Head/Tailwind: {head_or_tailwind_kts}, Ident/Freq/Dist/Bearing: {ident_freq_dist_bearing}")
departure = fpln[0]['ident']
arrival = fpln[-1]['ident']

# Print the extracted values
new_fn = excel.fill_excel('template.xlsx', fpln, departure, arrival)
print(f"[green]✈️Штурманский журнал экспортирован: {new_fn}✈️[/green]")
os.system('pause')
sys.exit(1)