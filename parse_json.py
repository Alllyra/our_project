import json

with open('vacancies.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

responsibilities = []

for vacancy in data:
    description = vacancy.get('description')
    if description:
        responsibilities_start = description.find('<strong>Обязанности:</strong>')
        if responsibilities_start != -1:
            ul_start = description.find('<ul>', responsibilities_start)
            ul_end = description.find('</ul>', responsibilities_start)
            if ul_start != -1 and ul_end != -1:
                ul = description[ul_start + 4:ul_end]
                li_start = 0
                while True:
                    li_start = ul.find('<li>', li_start)
                    if li_start == -1:
                        break
                    li_end = ul.find('</li>', li_start)
                    responsibility = ul[li_start + 4:li_end]
                    responsibilities.append({
                        'name': responsibility.strip(),
                        'vacancy_id': vacancy.get('id')
                    })
                    li_start = li_end + 1

with open('responsibilities.json', 'w', encoding='utf-8') as f:
    json.dump(responsibilities, f, ensure_ascii=False, indent=4)