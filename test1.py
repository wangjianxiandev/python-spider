# -*- coding: utf-8 -*-
"""对房价进行分析"""
import csv
import json
import pygal
file_name = "D:\\JetBrains\\Projects\\kaiyuan\\Spider\\csvfile\\北京.csv"
with open(file_name, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    row = next(reader)
    rows = []
    for row in reader:
        temp = {
            "address": row[1],
            "price": int(row[2].split(' ')[0]),
        }
        rows.append(temp)

# file_path = "D:\\JetBrains\\Projects\\kaiyuan\\Spider\\jsonfile\\"+ city_name + ".json"
    print(rows)

file_path = "D:\\JetBrains\\Projects\\kaiyuan\\Spider\\jsonfile\\test.json"
with open(file_path, 'w') as w_obj:
    json.dump(rows, w_obj)
address = []
price = []
for data in rows:
    address.append(data['address'])
    price.append(data['price'])

line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
line_chart.title = "租房价"
line_chart.x_labels= address
# line_chart.x_labels_major = address[:20]
line_chart.add('租房价', price)
line_chart.render_to_file('租房价格分析.svg')