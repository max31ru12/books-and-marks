# Декораторы функции

# Это имя функции-декоратора, в качестве аргумента передается имя функции
# которую мы оборачиваем в декоратор
def decorator_function(func):
    # Это функция-обертка, здесь происходят какие-то вещи, а затем вызывается оборачиваемая функция
    def wrapper():
        print('Функция-обёртка!') # Какое-то действие
        print('Оборачиваемая функция: {}'.format(func)) # Какое-то действие
        print('Выполняем обёрнутую функцию...') # Какое-то действие
        func() # Здесь происходит вызов оборачиваемой функции
        print('Выходим из обёртки') # Какое-то действие
    return wrapper


# Оборачиваем функцию в декоратор (следующаяя строчка - имя декоратора)
@decorator_function
# дальше идет функция, которая оборачивается
def some_func():
    pass


some_func()


