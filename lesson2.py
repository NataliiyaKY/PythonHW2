from typing import Callable


# # # 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# # # - перший записує в список нову справу
# # # - другий повертає всі записи
# # # 2) протипізувати перше завдання


def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        return todo_list

    return add_todo, get_all


a, b = notebook()

print(a('один'), b())
print(a('два'), b())
print(a('три'), b())


# # # 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
# # # Приклад:
# # # expanded_form(12) # return '10 + 2'
# # # expanded_form(42) # return '40 + 2'
# # # expanded_form(70304) # return '70000 + 300 + 4'


def main():
    li = []

    def calculation(some):
        nonlocal li
        for i in range(len(some)):
            if some[i] != '0':
                m = str(some)[i] + '0' * (len(some) - i - 1)
                li.append(m)

    def returnlist():
        return li

    return calculation, returnlist


c, d = main()

print(c('70302'), d())


# # # 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# # # та буде виводити це значення після виконання функцій


def decor(func):
    count = 0

    def some():
        nonlocal count
        count += 1
        print(f'count: {count}')
        func()

    return some


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
