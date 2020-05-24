from app.lib_dict import *

if __name__ == '__main__':
    # Получаем доступ к списку работников
    with open('Company_workers.txt', 'r', encoding='utf-8') as f:
        data = [(i.strip()).split(' # ') for i in f.readlines()]

    # Создаем словарь работников и их характеристик
    company_workers = dict()
    for i in range(len(data)):
        key_arr = ['age', 'rate']  # Ключи характеристик
        name = data[i].pop(0)
        company_workers[name] = dict(zip(key_arr, data[i]))

    # Список ключей для сортировки
    names = []
    for key in company_workers:
        names.append(key)

    # Производим сортировку по выбору
    print('Выберите вариант сортировки (цифру):\n'
          '1. По алфавиту.\n'
          '2. По возрасту.\n'
          '3. По зарплате.')
    choice = 0
    try:
        choice = int(input())
    except ValueError:
        print('Неверное значение.')

    if choice > 3 or choice < 1:
        print('Вариант не выбран. Программа завершена.')
    else:
        if choice == 1:
            names.sort()
        elif choice == 2:
            keys = arr_key(company_workers, 'age')
            names = sort_by_keys(names, keys)
        elif choice == 3:
            keys = arr_key(company_workers, 'rate')
            names = sort_by_keys(names, keys)

        # Выводим отсортированные значения
        for i in range(len(names)):
            print(f'{names[i]}')
            for key, item in company_workers[names[i]].items():
                print(f'{key}: {item}')
