first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
second_list = list()
result = list()

# def get_uniq_numbers(nums: list):
#     second_list = list(set(nums))  # с помощью конвертирования в множество, внесли элементы только в 1 кол-ве, потом в список, чтобы удобнее было работать далее
#     for i in range(len(second_list)):
#         count = 0
#         for j in range(len(first_list)):
#             if second_list[i] == first_list[j]:
#                 count = count + 1
#         if count == 1:
#             result.append(second_list[i])
#
#     yield result
#
#
# print(*get_uniq_numbers(first_list))
# К всеобщему сожалению, множество рушит порядок следования элементов, поэтому способ с конвертированием в set не подходит

def get_uniq_numbers(nums: list):
    for item in first_list:
        itemExist = False
        for i in second_list:
            if i == item:
                itemExist = True
                break
        if not itemExist:  # тоже самое, что и  if itemExist == False, но выглядит аккуратнее
            second_list.append(item)  # с помощью itemExist'a формируем список в нужном порядке и без повторений

    for i in range(len(second_list)):  # и теперь начинаем сравнивать и формировать результат
        count = 0
        for j in range(len(first_list)):
            if second_list[i] == first_list[j]:
                count = count + 1
        if count == 1:  # count - кол-во повторений
            result.append(second_list[i])
    yield result


print(*get_uniq_numbers(first_list))
