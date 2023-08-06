
import os
import pickle
import time
from functools import wraps


def cached(is_classmethod=False, expireFunc=None):
    def decorator(func):
        def save_cache(func):
            base_path = os.path.dirname(__file__)
            filename = f"{base_path}\\Cache_{func.__name__}.pkl"
            with open(filename, 'wb') as f:
                pickle.dump(func.cache, f)
        
        def load_cache(func):
            base_path = os.path.dirname(__file__)
            filename = f"{base_path}\\Cache_{func.__name__}.pkl"
            if os.path.isfile(filename):
                with open(filename, 'rb') as f:
                    return pickle.load(f)
            else:
                with open(filename, 'wb') as f:
                    pickle.dump({}, f)
                return {}
        
        func.cache = load_cache(func)
        
        @wraps(func)
        def wrapper(*args):
            is_valid = False
            tmp = func.cache.get(args[1:] if is_classmethod else args)
            if tmp != None:
                if expireFunc:
                    expire = expireFunc(tmp)
                    print(f"({expire:.0f})")
                    if expire>time.time():
                        is_valid = True
                else:
                    is_valid = True
            
            if is_valid:
                    print("유효한 캐시가 존재합니다.")
                    return tmp
            else:
                print("캐시 정보가 존재하지 않거나 유효하지 않습니다. api를 요청합니다.")
                func.cache[args[1:] if is_classmethod else args] = ret = func(*args)
                save_cache(func)
                return ret
        return wrapper
    return decorator