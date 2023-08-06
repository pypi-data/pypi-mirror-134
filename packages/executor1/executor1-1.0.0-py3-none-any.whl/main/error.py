# -*- coding: utf-8 -*-
# class ValueError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg


class ControlError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class OperationError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class FieldsError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class FieldsTypeError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


if __name__ == '__main__':
    raise FieldsTypeError('test')