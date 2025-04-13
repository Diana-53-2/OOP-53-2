def check_type(func):
    def wrapper(x):
        if not isinstance(x,(int, float)):
            print(f'Ошибка:ожидалось число')
            return None
        return func(x)
    return wrapper
@check_type
def square(x):
    return x * x
print(square(3))
print(square('hello'))


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls +=1
        print (f'функция вызвана {wrapper.calls} раз')
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
@count_calls
def hello():
    print('hello')
hello()
hello()