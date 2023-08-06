import uiautomation


def control_dic(name, depth, control_type):
    """
    :param name: inspect name 列的值
    :param depth: 层数
    :param control_type:  control 类型 如 TextControl EditControl ButtonControl
    :return: obj
    """
    obj = None
    if control_type == 'TextControl':
        obj = uiautomation.TextControl(Depth=depth, Name=name)
    elif control_type == 'EditControl':
        obj = uiautomation.EditControl(Depth=depth, Name=name)
    elif control_type == 'ButtonControl':
        obj = uiautomation.ButtonControl(Depth=depth, Name=name)
    return obj


def get_next_control(name, depth, control_type):
    """
    获取当前control对象的下一个control
    :param name: inspect name 列的值
    :param depth: 层数
    :param control_type:  control 类型 如 TextControl EditControl ButtonControl
    :return: obj
    """
    obj = control_dic(name, depth, control_type)
    if not obj:
        raise Exception('control_type not exist')
    parent = obj.GetParentControl().GetChildren()
    for i, v in enumerate(parent):
        if v.Name == name:
            return parent[i+1]


def get_same_level_control_by_offset(name, depth, control_type, offset):
    """
    在同一层级中，通过name唯一的control得到相邻offset步的control对象
    offset: 如：1，2，-1，-3  | 1代表下边一位， -3代表上边3位
    正数代表 目标control = name + offset
    负数代表 目标control = name - offset
    :param name: inspect name 列的值
    :param depth: 层数
    :param control_type:  control 类型 如 TextControl EditControl ButtonControl
    :param offset: 相邻间隔步数
    :return: obj
    """
    obj = control_dic(name, depth, control_type)
    if not obj:
        raise Exception('control_type not exist')
    parent = obj.GetParentControl().GetChildren()
    for i, v in enumerate(parent):
        if v.Name == name:
            return parent[i+offset]


def get_value_from_edit_control(obj):
    """
    获取当前Control的value值，只支持EditControl
    """
    return obj.GetValuePattern().Value


def pattern_set_by_exit_control(obj, val):
    """
    不丢字符设置值，只支持EditControl
    特点: 1.不丢字符  普调SetValue() 会丢字符
         2.直接覆盖，不需要清空编辑框
         3.目前只支持EditControl,其他类型control无次方法
    :param obj: EditControl obj
    :param val: 要设置的值
    """
    obj.GetValuePattern().SetValue(str(val))


def get_legacy_iaccessible_value(obj):
    """
    获取当前Control的LegacyIAccessible value值
    有时候,inspect只有LegacyIAccessible有值, 当普调Value无值时用这个获取
    """
    return obj.GetLegacyIAccessiblePattern().Value
