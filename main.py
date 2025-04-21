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
    head_or_tailwind_kts = cells[17].text.strip()
    ident_freq_dist_bearing = cells[18].text.strip()
    fpln.append({"ident": ident, "name": name, "procedure": procedure, "hdg": hdg, "distance_nm": distance_nm, "wind_degree_m_kts": wind_degree_m_kts, "head_or_tailwind_kts": head_or_tailwind_kts, "ident_freq_dist_bearing": ident_freq_dist_bearing})
    print(f"[cyan]Ident: {ident}[/cyan], Distance: {distance_nm}, Heading: {hdg}, Wind: {wind_degree_m_kts}, Head/Tailwind: {head_or_tailwind_kts}, Ident/Freq/Dist/Bearing: {ident_freq_dist_bearing}")
departure = fpln[0]['ident']
arrival = fpln[-1]['ident']
import os
os.path.isfile('.\Штурманский_журнал.xlsx')
if not os.path.isfile('.\Штурманский_журнал.xlsx'):
    print("[red]❌  Шаблон Штурманоского журнала не найден. 'Штурманский_журнал.xlsx' not found  ❌[/red]")
    os.system('pause')
    sys.exit(1)
# Print the extracted values
new_fn = excel.fill_excel('.\Штурманский_журнал.xlsx', fpln, departure, arrival)
print(f"[green]✈️Штурманский журнал экспортирован: {new_fn}✈️[/green]")
os.system('pause')
sys.exit(1)