import json

valuess = dict()
with open('tests.json', "r+") as file:
    tests = eval(file.read())
    with open('values.json') as file_v:
        values = eval(file_v.read())
    for dict_ in values["values"]:
        valuess[dict_['id']] = dict_['value']
    print(valuess)
    for dict_ in tests["tests"]:  
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
    print(tests)
    print(valuess)
    file.seek(0)  # rewind
    json.dump(tests, file)
    file.truncate()

