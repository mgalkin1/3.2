
def print_params(a=1, b='строка', c=True):
    print("Параметры функции:")
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print()

# Вызов функции с разным количеством аргументов
print_params()
print_params(10, 'новая строка', False)
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [42, 'hello', False]
values_dict = {'a': 10, 'b': 'world', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [3.14, 'pi']
print_params(*values_list_2, 42)

