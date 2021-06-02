from functools import wraps
import time
import os


def get_len_or(v, default=0):
    try:
        return len(v)
    except:
        return default


class RootData:
    __data__ = dict()

    # __update__ = False

    @staticmethod
    def clearCache(key: str = None):
        if key is None:
            RootData.__data__.clear()
            return True
        if RootData.has(key):
            RootData.__data__.pop(key)
            return True
        return False

    @staticmethod
    def cache(arg, update=False, max_cache_time=-1):
        def _write2cache(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if isinstance(arg, str):
                    if update or not RootData.has(arg):
                        ret = func(*args, **kwargs)
                        print(max_cache_time,update,RootData.has(arg))
                        cache_time = 0 if max_cache_time < 0 else time.time() + max_cache_time
                        RootData.set(arg, ret, cache_time)
                        return ret
                    else:
                        return RootData.get(arg)
                else:
                    print(f"cache can't store name for type of {arg.__class__.__name__}")
                    return func(*args, **kwargs)

            return wrapper

        return _write2cache

    @staticmethod
    def set(key, value, cache_time=0):
        return RootData.__data__.update({key: (value, cache_time,)})

    @staticmethod
    def get(key, default=None):
        ret = RootData.__data__.get(key, None)
        if get_len_or(ret, 0) != 2:
            return default
        return ret[0]

    @staticmethod
    def has(key):
        if key in RootData.__data__.keys():
            if RootData.__data__.get(key)[1] > time.time() or RootData.__data__.get(key)[1] == 0:
                return True
        return False

    @staticmethod
    def __getattr__(item, default=None):
        return RootData.get(item, default)

    @staticmethod
    def dump(save_path: str = './config/Root.DataStore', keep_field: list = None, drop_field: list = None, show=False):
        try:
            import pickle
        except ImportError:
            print(f"No module pickle found dump Break!")
            return False
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        dp = {}
        if keep_field:
            for field in keep_field:
                if RootData.get(field, None) is not None:
                    dp.setdefault(field, RootData.__data__.get(field))
        elif drop_field:
            dp = RootData.__data__.copy()
            for field in drop_field:
                try:
                    dp.pop(field)
                except KeyError:
                    pass
        else:
            dp = RootData.__data__
        with open(save_path, 'wb') as f:
            pickle.dump(dp, f)
        if show:
            print(f"RootData Dump successfully at {save_path}")


    @staticmethod
    def load(path: str = './config/Root.DataStore', *fields):
        if os.path.exists(path):
            try:
                import pickle
            except ImportError:
                print(f"No module pickle found dump Break!")

                return False
            try:
                with open(path, 'rb') as f:
                    dic = pickle.load(f)
                if fields:
                    ret = {k: dic.get(k) for k in fields if dic.get(k, None) is not None}
                else:
                    ret = dic
                RootData.__data__.update(ret)
                # logger.system(f"RootData loaded successfully!")
            except Exception as e:
                print(f"load failed,Error={e}")


        else:
            print(f"config File not Exist!")

