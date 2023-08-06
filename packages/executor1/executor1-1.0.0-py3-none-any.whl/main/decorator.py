# -*- coding: utf-8 -*-
from functools import wraps
from main.error import *


def RequiredField(func):
    @wraps(func)
    def inner(*arg, **kwargs):
        value = func(*arg, **kwargs)
        if not value or value == '':
            raise ValueError('%s is required argument' % func.__name__)
            # return self.raise_error('%s can not None' % func.__name__)
        else:
            return value
    return inner


def ControlFinder(func):
    @wraps(func)
    def inner(self, *arg, **kwargs):
        value = func(self, *arg, **kwargs)
        if value == 0 or value == '':
            raise ControlError('%s is  not defined' % self.controlType)
            # return self.raise_error('%s can not None' % func.__name__)
        elif value == -1:
            print(self.raiseIfNotExist)
            if self.raiseIfNotExist:

                raise ControlError('Control not found: SerialNum is "%s" ' % self.serialNum)
            else:
                return value
        else:
            return value
    return inner


def OperationFinder(func):
    @wraps(func)
    def inner(self, *arg, **kwargs):
        value = func(self, *arg, **kwargs)
        if isinstance(value, str):
            raise ControlError('operation "%s" is not defined' % value)
        else:
            return value
    return inner


def RelatedFields(**kwargs):
    def func_outer(func):
        def func_inner(self, *fun_arg, **fun_kwargs):
            arg_ = list()
            for key, value in kwargs.items():
                fields = self.get_field()
                # if fields[value] or fields[value] == '' or fields[value] == 0:
                #     pass
                if fields[value] is None:
                    arg_.append(key)
                else:
                    pass
            if len(arg_) > 0:
                arg_str = ' '.join(arg_)
                raise FieldsError('%s operation is missing fields: %s ' % (func.__name__, arg_str))
            else:
                return func(self)
        return func_inner
    return func_outer


def TypeChecking(arg_type):
    def func_outer(func):
        def func_inner(self, *fun_arg, **fun_kwargs):
            fields = func(self)
            if isinstance(fields, arg_type) or fields is None:
                pass
            else:
                raise FieldsTypeError('The type of the "%s" field is %s' % (func.__name__, arg_type))
            return fields
        return func_inner
    return func_outer


@TypeChecking(int)
def test():
    return 'a'


if __name__ == '__main__':
    test()