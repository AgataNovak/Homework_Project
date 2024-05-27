from functools import wraps


def log(filename=None):
    """ Функция-декоратор логирует в заданный аргументом декоратора файл или, при отсутствии файла для записи, в консоль
     информацию о работе заданной декоратору функции и/или о возникшей при работе функции ошибке """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if filename is None:
                try:
                    result = func(*args, **kwargs)
                    print(f"Function {func.__name__} ok. Returned {result}")
                except Exception as _ex:
                    print(f"{func.__name__} error: {_ex}. Inputs: {args}, {kwargs}")
            else:
                pass

        return wrapper

    return decorator


# @log()
# def addition(x, y):
#     return x + y
#
#
# addition(2, 3)
# addition(2, '3')
