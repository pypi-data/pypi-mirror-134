from abc import ABCMeta, abstractmethod


class BaseManager(metaclass=ABCMeta):
    @abstractmethod
    async def connect(self, loop=None, **kwargs):
        pass

    @abstractmethod
    async def close(self):
        pass

    def parse_compare(self, k, v, model):
        if "__" in k:
            attr, compare = k.split("__")
            newk = attr
            res = None
            if compare == "gt":
                res = getattr(model.__table__.c, newk) > v
            elif compare == "gte":
                res = getattr(model.__table__.c, newk) >= v
            elif compare == "lt":
                res = getattr(model.__table__.c, newk) < v
            elif compare == "lte":
                res = getattr(model.__table__.c, newk) <= v
        else:
            newk = k
            res = getattr(model.__table__.c, newk) == v
        return newk, res

    def gen_model_query(self, params=None, model=None):
        query_judge = None
        for k, v in params.items():
            newk, newv = self.parse_compare(k, v, model)
            if hasattr(model.__table__.c, newk):
                if query_judge is not None:
                    query_judge = query_judge & newv
                else:
                    query_judge = newv
        query = model.__table__.select().where(query_judge)
        return query

    def query(self, params=None, model=None):
        query = self.gen_model_query(params=params, model=model)
        return query

    @abstractmethod
    async def get_by_param(self):
        pass

    @abstractmethod
    async def select_by_param(self):
        pass

    @abstractmethod
    async def get(self):
        pass

    @abstractmethod
    async def select(self):
        pass

    @abstractmethod
    async def set(self):
        pass

    @abstractmethod
    async def format_query(self):
        pass

    @abstractmethod
    async def set_multi(self):
        pass

    @abstractmethod
    async def all(self):
        pass

    @abstractmethod
    async def instance(self):
        pass

    @abstractmethod
    async def execute(self):
        pass
