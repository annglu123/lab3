# TODO Напишите функцию для поиска индекса товара
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def find(name,list):
    for ind, pos in enumerate(list):
        if name in pos:
            return ind
for find_item in ['банан', 'груша', 'персик']:
    index_item = find(find_item,items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
