from app.lib_set import *

if __name__ == '__main__':
    with open('Chernoble_beneficiaries.txt', 'r', encoding='utf-8') as f,\
            open('Seniors_beneficiaries.txt', 'r', encoding='utf-8') as g:
        data1 = set([i.strip() for i in f.readlines()])
        data2 = set([i.strip() for i in g.readlines()])
    print(inter_set(data1, data2))
    print(diff_set(data1, data2))
