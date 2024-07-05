import json

def func(values_file, tests_file, report_file):
    valuess = dict()
    with open(tests_file, "r+") as file, open(report_file, 'w+') as report:
        report.write(file.read())
        report.seek(0)  # rewind
        file.seek(0)  # rewind
        #print('report.read()', report.read())
        report_dict = eval(file.read())
        with open(values_file) as file_v:
            values = eval(file_v.read())
        for dict_ in values["values"]:
            valuess[dict_['id']] = dict_['value']
        print(valuess)
        for dict_ in report_dict["tests"]:  
            dict_['value'] = valuess[dict_['id']]
            if 'values' in dict_:
                print(dict_['id'], dict_['id'])
                for j in dict_['values']:
                    j['value'] = valuess[j['id']]
                    if 'values' in j: 
                        print(j['id'], j['id'])
                        for k in j['values']:
                            if k['id'] in valuess.values():
                                print('122 - ',  valuess[k['id']])
                                k['value'] = valuess[k['id']]
                            if 'values' in k: 
                                for r in k['values']:
                                    r['value'] = valuess[r['id']]
            else:
                dict_['value'] = valuess[dict_['id']]
        print(report)
        print(valuess)
        report.seek(0)  # rewind
        json.dump(report_dict, report)
        report.truncate()


if __name__ == '__main__': 
    values_file = input('Введите фаил значений (values): ')
    tests_file = input('Введите фаил формы (tests): ')
    report_file = input('Введите фаил заполнения (report): ')
    func(values_file, tests_file, report_file)
