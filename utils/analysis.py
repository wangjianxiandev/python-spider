# -*- coding: utf-8 -*-
import csv
import json
import pygal


class Analysis():
    """对租房数据进行分析"""

    def jsonfenxi(self, city_name):

        file_name = "D:\\JetBrains\\Projects\\kaiyuan\\Spider\\csvfile\\" + city_name + ".csv"
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
            # print(rows)

        file_path = "D:\\JetBrains\\Projects\\kaiyuan\\Spider\\jsonfile\\" + city_name + ".json"
        with open(file_path, 'w') as w_obj:
            json.dump(rows, w_obj)
        address = []
        price = []
        for data in rows:
            address.append(data['address'])
            price.append(data['price'])

        line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
        line_chart.title = city_name + "租房价"
        line_chart.x_labels = address
        # line_chart.x_labels_major = address[:20]
        line_chart.add(city_name + '租房价', price)
        line_chart.render_to_file("D:\\JetBrains\\Projects\\kaiyuan\\Spider\\analysisfile\\"+ city_name + '租房价格分析.svg')