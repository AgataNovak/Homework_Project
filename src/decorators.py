import os.path
from functools import wraps
from typing import Callable, Any


def log(filename: Any = None) -> Callable:
    """Функция-декоратор логирует в заданный аргументом декоратора файл или, при отсутствии файла для записи,
    в консоль информацию о работе заданной декоратору функции и/или о возникшей при работе функции ошибке"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if filename:
                if not os.path.exists(r"logs"):
                    os.mkdir(r"logs")
                with open(os.path.join(r"logs", filename), "at") as file:
                    try:
                        result = func(*args, **kwargs)
                        log_str = f"Function {func.__name__} ok. Returned {result}"
                        file.write(f"{log_str}\n")
                        return result

                    except Exception as _ex:
                        log_str = f"{func.__name__} error: {_ex}. Inputs: {args}, {kwargs}"
                        file.write(f"{log_str}\n")
            else:
                try:
                    result = func(*args, **kwargs)
                    log_str = f"Function {func.__name__} ok. Returned {result}"
                    print(log_str)
                    return result

                except Exception as _ex:
                    log_str = f"{func.__name__} error: {_ex}. Inputs: {args}, {kwargs}"
                    print(log_str)
                    return None

        return wrapper

    return decorator
