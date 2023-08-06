# -*- coding: utf-8 -*-
# @Time : 2021/11/24 17:44
# @Author : Liu
# @File : UIAExecutor
# @Email : rejii0042@163.com
import subprocess
# import time
import uiautomation as uia
import platform
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as WebDriver_chrome
from main.decorator import *
from main.OperationSet import *
from main.GAutoit import execute as auto
import autoit
MAX_SEARCH_SECONDS = 30
SEARCH_INTERVAL = uia.SEARCH_INTERVAL
OPERATION_WAIT_TIME = uia.OPERATION_WAIT_TIME
ControlTypeNames = uia.ControlTypeNames
CONTROL = dict()
SW = uia.SW
CHROME_DRIVER = r'D:\SoftwareFiles\chromedriver\97.0.4692.71\chromedriver.exe'


class GUIAFieldsMap:
    serialNum = 'serialNum'
    openApp = 'openApp'
    searchFromControl = 'searchFromControl'
    searchInterval = 'searchInterval'
    searchDepth = 'searchDepth'
    controlName = 'name'
    subName = 'subName'
    className = 'className'
    automationId = 'automationId'
    foundIndex = 'foundIndex'
    controlType = 'controlType'
    condiment = 'condiment'
    childrenIndex = 'childrenIndex'
    maxSearchSeconds = 'maxSearchSeconds'
    operation = 'operation'
    value = 'value'
    searchIntervalSeconds = 'searchIntervalSeconds'
    printIfNotExist = 'printIfNotExist'
    raiseException = 'raiseException'
    printIfNotDisappear = 'printIfNotDisappear'
    x = 'x'
    y = 'y'
    ratioX = 'ratioX'
    ratioY = 'ratioY'
    simulateMove = 'simulateMove'
    waitTime = 'waitTime'
    dragDropX1 = 'dragDropX1'
    dragDropX2 = 'dragDropX2'
    dragDropY1 = 'dragDropY1'
    dragDropY2 = 'dragDropY2'
    moveSpeed = 'moveSpeed'
    wheelTimes = 'wheelTimes'
    interval = 'interval'
    cmdShow = 'cmdShow'
    moveWindowX = 'moveWindowX'
    moveWindowY = 'moveWindowY'
    moveWindowWidth = 'moveWindowWidth'
    moveWindowHeight = 'moveWindowHeight'
    repaint = 'repaint'
    text = 'text'
    savePath = 'savePath'
    imageX = 'imageX'
    imageY = 'imageY'
    imageWidth = 'imageWidth'
    imageHeight = 'imageHeight'
    bitMapX = 'bitMapX'
    bitMapY = 'bitMapY'
    bitMapWidth = 'bitMapWidth'
    bitMapHeight = 'bitMapHeight'
    key = 'key'
    hotKey = 'hotKey'
    raiseIfNotExist = 'raiseIfNotExist'
    legacyPatternValue='legacyPatternValue'


class GUIAControlMap:
    AppBarControl = 'AppBarControl'
    ButtonControl = 'ButtonControl'
    CalendarControl = 'CalendarControl'
    CheckBoxControl = 'CheckBoxControl'
    ComboBoxControl = 'ComboBoxControl'
    CustomControl = 'CustomControl'
    DataGridControl = 'DataGridControl'
    DataItemControl = 'DataItemControl'
    DocumentControl = 'DocumentControl'
    EditControl = 'EditControl'
    GroupControl = 'GroupControl'
    HeaderControl = 'HeaderControl'
    HeaderItemControl = 'HeaderItemControl'
    HyperlinkControl = 'HyperlinkControl'
    ImageControl = 'ImageControl'
    ListControl = 'ListControl'
    ListItemControl = 'ListItemControl'
    MenuBarControl = 'MenuBarControl'
    MenuControl = 'MenuControl'
    MenuItemControl = 'MenuItemControl'
    PaneControl = 'PaneControl'
    ProgressBarControl = 'ProgressBarControl'
    RadioButtonControl = 'RadioButtonControl'
    ScrollBarControl = 'ScrollBarControl'
    SemanticZoomControl = 'SemanticZoomControl'
    SeparatorControl = 'SeparatorControl'
    SliderControl = 'SliderControl'
    SpinnerControl = 'SpinnerControl'
    SplitButtonControl = 'SplitButtonControl'
    StatusBarControl = 'StatusBarControl'
    TabControl = 'TabControl'
    TabItemControl = 'TabItemControl'
    TableControl = 'TableControl'
    TextControl = 'TextControl'
    ThumbControl = 'ThumbControl'
    TitleBarControl = 'TitleBarControl'
    ToolBarControl = 'ToolBarControl'
    ToolTipControl = 'ToolTipControl'
    TreeControl = 'TreeControl'
    TreeItemControl = 'TreeItemControl'
    WindowControl = 'WindowControl'
    GetChildren = 'GetChildren'
    GetParentControl = 'GetParentControl'
    GetFirstChildControl = 'GetFirstChildControl'
    GetLastChildControl = 'GetLastChildControl'
    GetNextSiblingControl = 'GetNextSiblingControl'
    GetPreviousSiblingControl = 'GetPreviousSiblingControl'
    GetSameLevelControlByOffset = 'GetSameLevelControlByOffset'


class GOperationMap:
    SendKeys = 'SendKeys'
    SendKey = 'SendKey'
    Click = 'Click'
    DoubleClick = 'DoubleClick'
    MiddleClick = 'MiddleClick'
    RightClick = 'RightClick'
    SetFocus = 'SetFocus'
    Exists = 'Exists'
    ReFind = 'ReFind'
    Disappears = 'Disappears'
    MoveCursorToInnerPos = 'MoveCursorToInnerPos'
    MoveCursorToMyCenter = 'MoveCursorToMyCenter'
    DragDrop = 'DragDrop'
    RightDragDrop = 'RightDragDrop'
    WheelDown = 'WheelDown'
    WheelUp = 'WheelUp'
    ShowWindow = 'ShowWindow'
    Show = 'Show'
    Hide = 'Hide'
    GetWindowText = 'GetWindowText'
    MoveWindow = 'MoveWindow'
    SetWindowText = 'SetWindowText'
    CaptureToImage = 'CaptureToImage'
    ToBitMap = 'ToBitMap'
    SetTopMost = 'SetTopMost'
    SetActive = 'SetActive'
    HotKey = 'HotKey'
    LegacyPatternSetValue = 'LegacyPatternSetValue'


class GControl:
    def __init__(self, operation_detail: dict, operation_index: (int, str)):
        self.operation_detail = operation_detail
        self.operation_index = operation_index

    @ControlFinder
    def GetControl(self):
        switch = self.__switch_middle()
        control_fun = switch.get(self.controlType, None)
        if control_fun:
            if isinstance(control_fun, uia.Control):
                return control_fun
            control = control_fun(search_from_control=self.searchFromControl,
                                  search_depth=self.searchDepth,
                                  search_interval=self.searchInterval,
                                  found_index=self.foundIndex,
                                  **self.SearchProperties)
            if control:
                return control
            else:
                return -1
        else:
            return 0

    def start(self):
        self.OpenAPP()
        control = self.GetControl()
        control = self.condimentHandle(control)
        CONTROL[self.serialNum] = control
        return control

    def test(self):
        print(self.searchFromControl)
        print(self.SearchProperties)
        print(self.foundIndex)
        # print(self.ControlName)
        return None

    def OpenAPP(self):
        if self.openApp == '':
            return
        else:
            if 'http' in self.openApp:
                pass
            elif 'exe' in self.openApp or 'EXE' in self.openApp:
                # autoit.run(self.openApp)
                subprocess.Popen(self.openApp, shell=True, encoding="utf-8")

    def __switch_middle(self):
        switch = dict()
        switch[GUIAControlMap.ButtonControl] = self.GButtonControl
        switch[GUIAControlMap.AppBarControl] = self.GAppBarControl
        switch[GUIAControlMap.CalendarControl] = self.GCalendarControl
        switch[GUIAControlMap.CheckBoxControl] = self.GCheckboxControl
        switch[GUIAControlMap.ComboBoxControl] = self.GComboboxControl
        switch[GUIAControlMap.CustomControl] = self.GCustomControl
        switch[GUIAControlMap.DataGridControl] = self.GDataGridControl
        switch[GUIAControlMap.DataItemControl] = self.GDataItemControl
        switch[GUIAControlMap.DocumentControl] = self.GDocumentControl
        switch[GUIAControlMap.EditControl] = self.GEditControl
        switch[GUIAControlMap.GroupControl] = self.GGroupControl
        switch[GUIAControlMap.HeaderControl] = self.GHeaderControl
        switch[GUIAControlMap.HeaderItemControl] = self.GHeaderItemControl
        switch[GUIAControlMap.HyperlinkControl] = self.GHyperlinkControl
        switch[GUIAControlMap.ImageControl] = self.GImageControl
        switch[GUIAControlMap.ListControl] = self.GListControl
        switch[GUIAControlMap.ListItemControl] = self.GListItemControl
        switch[GUIAControlMap.MenuBarControl] = self.GMenuBarControl
        switch[GUIAControlMap.MenuControl] = self.GMenuControl
        switch[GUIAControlMap.MenuItemControl] = self.GMenuItemControl
        switch[GUIAControlMap.PaneControl] = self.GPaneControl
        switch[GUIAControlMap.ProgressBarControl] = self.GProgressbarControl
        switch[GUIAControlMap.RadioButtonControl] = self.GRadiobuttonControl
        switch[GUIAControlMap.ScrollBarControl] = self.GScrollbarControl
        switch[GUIAControlMap.SpinnerControl] = self.GSpinnerControl
        switch[GUIAControlMap.SliderControl] = self.GSliderControl
        switch[GUIAControlMap.SeparatorControl] = self.GSeparatorControl
        switch[GUIAControlMap.SemanticZoomControl] = self.GSemanticZoomControl
        switch[GUIAControlMap.StatusBarControl] = self.GStatusBarControl
        switch[GUIAControlMap.SplitButtonControl] = self.GSplitButtonControl
        switch[GUIAControlMap.TabControl] = self.GTabControl
        switch[GUIAControlMap.TextControl] = self.GTextControl
        switch[GUIAControlMap.TreeControl] = self.GTreeControl
        switch[GUIAControlMap.TreeItemControl] = self.GTreeItemControl
        switch[GUIAControlMap.ThumbControl] = self.GThumbControl
        switch[GUIAControlMap.ToolTipControl] = self.GToolTipControl
        switch[GUIAControlMap.ToolBarControl] = self.GToolBarControl
        switch[GUIAControlMap.TableControl] = self.GTableControl
        switch[GUIAControlMap.TabItemControl] = self.GTabItemControl
        switch[GUIAControlMap.TitleBarControl] = self.GTitleBarControl
        switch[GUIAControlMap.WindowControl] = self.GWindowControl
        switch['None'] = self.searchFromControl
        return switch

    def __condiment_middle(self) -> dict:
        condiment_ = dict()
        condiment_[GUIAControlMap.GetChildren] = self.GGetChildren
        condiment_[GUIAControlMap.GetParentControl] = self.GGetParentControl
        condiment_[GUIAControlMap.GetFirstChildControl] = self.GGetFirstChildControl
        condiment_[GUIAControlMap.GetLastChildControl] = self.GGetLastChildControl
        condiment_[GUIAControlMap.GetPreviousSiblingControl] = self.GGetPreviousSiblingControl
        condiment_[GUIAControlMap.GetNextSiblingControl] = self.GGetNextSiblingControl
        condiment_[GUIAControlMap.GetSameLevelControlByOffset] = self.GGetSameLevelControlByOffset
        return condiment_

    @staticmethod
    def GetSearchFromControl(search_from_control) -> uia.Control:
        """
        从全局变量里获取到基控件
        search_from_control
        """
        control = CONTROL[search_from_control]
        return control

    @property
    def SearchProperties(self) -> dict:
        search_properties = dict()
        if self.controlName != '':
            search_properties['Name'] = self.controlName
        if self.className != '':
            search_properties['ClassName'] = self.className
        if self.automationId != '':
            search_properties['AutomationId'] = self.automationId
        if self.subName != '':
            search_properties['SubName'] = self.subName
        return search_properties

    @property
    # @RequiredField
    def serialNum(self) -> (str, None):
        """
        控件序号唯一值
        """
        serial_num = self.operation_detail.get(GUIAFieldsMap.serialNum, None)
        if not serial_num:
            serial_num = self.operation_index
        return str(serial_num)

    @property
    def openApp(self) -> str:
        """
        打开某个应用程序
        """
        open_app = self.operation_detail.get(GUIAFieldsMap.openApp, '')
        return open_app

    @property
    def raiseIfNotExist(self) -> str:
        """
        若控件没找到是否抛出异常
        """
        value = self.operation_detail.get(GUIAFieldsMap.raiseIfNotExist, True)
        return value

    @property
    def searchFromControl(self) -> (uia.Control, None):
        """
        控件查找条件：控件查找基点
        """
        search_from_control = self.operation_detail.get(GUIAFieldsMap.searchFromControl, None)
        control = None
        if search_from_control:
            if isinstance(search_from_control, (str, int)):
                control = self.GetSearchFromControl(search_from_control=search_from_control)
            if isinstance(search_from_control, dict):
                control = GControl(operation_detail=search_from_control, operation_index=self.serialNum)
                control = control.start()
        return control

    @property
    def searchInterval(self) -> float:
        """
        控件查找条件：控件查找时间间隔， 默认为0.5s
        """
        search_interval = self.operation_detail.get(GUIAFieldsMap.searchInterval, '')
        if search_interval == '':
            search_interval = SEARCH_INTERVAL
        return float(search_interval)

    @property
    # @RequiredField
    def searchDepth(self) -> (int, str):
        """
        控件查找条件：查找深度
        """

        search_depth = self.operation_detail.get(GUIAFieldsMap.searchDepth, '')
        if search_depth != '':
            search_depth = int(search_depth)
        return search_depth

    @property
    def controlName(self) -> str:
        """
        控件查找条件：控件名字
        """
        name = self.operation_detail.get(GUIAFieldsMap.controlName, '')
        return name

    @property
    def subName(self) -> str:
        """
        控件查找条件：控件部分名字
        """
        sub_name = self.operation_detail.get(GUIAFieldsMap.subName, '')
        return sub_name

    @property
    def className(self) -> str:
        """
        控件查找条件：控件的 class name
        """

        class_name = self.operation_detail.get(GUIAFieldsMap.className, '')
        return class_name

    @property
    def automationId(self) -> str:
        """
        控件查找条件：控件的 automation id 。注：AutomationId 有可能会变化
        """

        automation_id = self.operation_detail.get(GUIAFieldsMap.automationId, '')
        return automation_id

    @property
    def foundIndex(self):
        """
        控件查找条件：控件索引，默认为1
        """

        found_index = self.operation_detail.get(GUIAFieldsMap.foundIndex, 1)
        if found_index != '':
            found_index = int(found_index)
        return found_index

    @property
    def controlType(self) -> str:
        """
        控件查找条件：控件类型
        """
        control_type = self.operation_detail.get(GUIAFieldsMap.controlType, '')
        if control_type == '':
            control_type = 'None'
        return control_type

    @property
    def condiment(self):
        """
        condiment ：该参数值为可选 （GetChildren，GetFirstChildControl，GetLastChildControl，GetParentControl，
        GetNextSiblingControl，GetPreviousSiblingControl, GetSameLevelControlByOffset）六选一
        当值为 GetChildren 时，ChildrenIndex不能为空
        """
        condiment = self.operation_detail.get(GUIAFieldsMap.condiment, '')
        condiment = condiment.split(',')
        return condiment

    @property
    def childrenIndex(self):
        """
        获取控件的子控件索引
        """
        children_index = self.operation_detail.get(GUIAFieldsMap.childrenIndex, '')
        if self.condiment == GUIAControlMap.GetChildren:
            if children_index == '':
                raise ValueError('Condiment is GetChildren, ChildrenIndex cant not empty!')
        return int(children_index)

    def condimentHandle(self, control):
        """
        获取控件
        """
        if self.condiment == ['']:
            return control
        else:
            middle = self.__condiment_middle()
            for condiment in self.condiment:
                if GUIAControlMap.GetChildren in condiment:
                    children = condiment.split(':')
                    if len(children) != 2:
                        return -1
                    else:
                        children_index = int(children[1])
                        condiment_control = middle[children[0]](control)
                        condiment_control = condiment_control[children_index]
                        control = condiment_control
                        continue
                elif GUIAControlMap.GetSameLevelControlByOffset in condiment:
                    flag = condiment.split(':')
                    if len(flag) != 2:
                        return -2
                    else:
                        offset = int(flag[1])
                        condiment_control = middle[flag[0]](control, offset)
                        control = condiment_control
                else:
                    condiment_control = middle[condiment](control)
                    control = condiment_control
                    continue
            return control

    @property
    def maxSearchSeconds(self) -> int:
        max_search_seconds = self.operation_detail.get(GUIAFieldsMap.maxSearchSeconds, MAX_SEARCH_SECONDS)
        # if max_search_seconds == '':
        #     max_search_seconds = 30
        return int(max_search_seconds)

    @staticmethod
    def GGetChildren(control):
        """
        获取子控件
        """
        children = control.GetChildren()
        return children

    @staticmethod
    def GGetFirstChildControl(control):
        """
        获取第一个子控件
        """
        first_child = control.GetFirstChildControl()
        return first_child

    @staticmethod
    def GGetLastChildControl(control):
        """
        获取最后一个子控件
        :param control:
        :return:
        """

        last_child = control.GetLastChildControl()
        return last_child

    @staticmethod
    def GGetNextSiblingControl(control):
        """
        获取后一个邻居控件
        :param control:
        :return:
        """

        next_sibling = control.GetNextSiblingControl()
        return next_sibling

    @staticmethod
    def GGetPreviousSiblingControl(control):
        """
        获取前一个邻居控件
        :param control:
        :return:
        """
        previous_sibling = control.GetPreviousSiblingControl()
        return previous_sibling

    @staticmethod
    def GGetParentControl(control):
        """
        获取父控件
        :param control:
        :return:
        """
        parent = control.GetParentControl()
        return parent

    def GGetSameLevelControlByOffset(self, control, offset):
        children = control.GetParentControl().GetChildren()
        for i, v in enumerate(children):
            if v.Name == self.controlName:
                return children[i + offset]

    @staticmethod
    def GAppBarControl(search_from_control, search_depth: int, search_interval: float,
                       found_index: int,
                       **search_properties) -> (uia.AppBarControl, None):
        """
        :rtype: ButtonControl

        """
        app_bar = uia.AppBarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                    searchInterval=search_interval,
                                    foundIndex=found_index, **search_properties)
        if app_bar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return app_bar
        else:
            return None

    @staticmethod
    def GButtonControl(search_from_control, search_depth: int, search_interval: float,
                       found_index: int,
                       **search_properties) -> (uia.ButtonControl, None):
        """
        :rtype: ButtonControl

        """
        button = uia.ButtonControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                   searchInterval=search_interval,
                                   foundIndex=found_index, **search_properties)
        if button.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return button
        else:
            return None

    @staticmethod
    def GCalendarControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.CalendarControl, None):
        """

        :rtype: CalendarControl
        :return: CalendarControl obj
        """
        calendar = uia.CalendarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                       searchInterval=search_interval,
                                       foundIndex=found_index, **search_properties)

        if calendar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return calendar
        else:
            return None

    @staticmethod
    def GCheckboxControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.CheckBoxControl, None):
        """

        :rtype: CheckBoxControl
        """
        checkbox = uia.CheckBoxControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                       searchInterval=search_interval,
                                       foundIndex=found_index, **search_properties)
        if checkbox.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return checkbox
        else:
            return None

    @staticmethod
    def GComboboxControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.ComboBoxControl, None):
        """

        :rtype: ComboBoxControl
        """
        combobox = uia.ComboBoxControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                       searchInterval=search_interval,
                                       foundIndex=found_index, **search_properties)
        if combobox.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return combobox
        else:
            return None

    @staticmethod
    def GCustomControl(search_from_control, search_depth: int, search_interval,
                       found_index: int,
                       **search_properties) -> (uia.CustomControl, None):
        custom = uia.CustomControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                   searchInterval=search_interval,
                                   foundIndex=found_index, **search_properties)
        if custom.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return custom
        else:
            return None

    @staticmethod
    def GDataGridControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.DataGridControl, None):
        data_grid = uia.DataGridControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                        searchInterval=search_interval,
                                        foundIndex=found_index, **search_properties)
        if data_grid.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return data_grid
        else:
            return None

    @staticmethod
    def GDataItemControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.DataItemControl, None):
        data_item = uia.DataItemControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                        searchInterval=search_interval,
                                        foundIndex=found_index, **search_properties)
        if data_item.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return data_item
        else:
            return None

    @staticmethod
    def GDocumentControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.DocumentControl, None):
        document = uia.DocumentControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                       searchInterval=search_interval,
                                       foundIndex=found_index, **search_properties)
        if document.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return document
        else:
            return None

    @staticmethod
    def GEditControl(search_from_control, search_depth: int, search_interval: float,
                     found_index: int,
                     **search_properties) -> (uia.EditControl, None):
        edit = uia.EditControl(searchFromControl=search_from_control, searchDepth=search_depth,
                               searchInterval=search_interval,
                               foundIndex=found_index, **search_properties)
        if edit.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return edit
        else:
            return None

    @staticmethod
    def GGroupControl(search_from_control, search_depth: int, search_interval: float,
                      found_index: int,
                      **search_properties) -> (uia.GroupControl, None):
        group = uia.GroupControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                 searchInterval=search_interval,
                                 foundIndex=found_index, **search_properties)
        if group.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return group
        else:
            return None

    @staticmethod
    def GHeaderControl(search_from_control, search_depth: int, search_interval: float,
                       found_index: int,
                       **search_properties) -> (uia.HeaderControl, None):
        header = uia.HeaderControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                   searchInterval=search_interval,
                                   foundIndex=found_index, **search_properties)
        if header.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return header
        else:
            return None

    @staticmethod
    def GHeaderItemControl(search_from_control, search_depth: int, search_interval: float,
                           found_index: int,
                           **search_properties) -> (uia.HeaderItemControl, None):
        header_item = uia.HeaderItemControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                            searchInterval=search_interval,
                                            foundIndex=found_index, **search_properties)
        if header_item.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return header_item
        else:
            return None

    @staticmethod
    def GHyperlinkControl(search_from_control, search_depth: int, search_interval: float,
                          found_index: int,
                          **search_properties) -> (uia.HyperlinkControl, None):
        hyperlink = uia.HyperlinkControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                         searchInterval=search_interval,
                                         foundIndex=found_index, **search_properties)
        if hyperlink.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return hyperlink
        else:
            return None

    @staticmethod
    def GImageControl(search_from_control, search_depth: int, search_interval: float,
                      found_index: int,
                      **search_properties) -> (uia.ImageControl, None):
        image = uia.ImageControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                 searchInterval=search_interval,
                                 foundIndex=found_index, **search_properties)
        if image.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return image
        else:
            return None

    @staticmethod
    def GListControl(search_from_control, search_depth: int, search_interval: float,
                     found_index: int,
                     **search_properties) -> (uia.ListControl, None):
        list_control = uia.ListControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                       searchInterval=search_interval,
                                       foundIndex=found_index, **search_properties)

        if list_control.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            print(list_control)
            return list_control
        else:
            return None

    @staticmethod
    def GListItemControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.ListItemControl, None):
        # print(search_from_control)
        list_item = uia.ListItemControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                        searchInterval=search_interval,
                                        foundIndex=found_index, **search_properties)
        if list_item.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return list_item
        else:
            return None

    @staticmethod
    def GMenuBarControl(search_from_control, search_depth: int, search_interval: float,
                        found_index: int,
                        **search_properties) -> (uia.MenuBarControl, None):
        menu_bar = uia.MenuBarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                      searchInterval=search_interval,
                                      foundIndex=found_index, **search_properties)
        if menu_bar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return menu_bar
        else:
            return None

    @staticmethod
    def GMenuControl(search_from_control, search_depth: int, search_interval: float,
                     found_index: int,
                     **search_properties) -> (uia.MenuControl, None):
        menu = uia.MenuControl(searchFromControl=search_from_control, searchDepth=search_depth,
                               searchInterval=search_interval,
                               foundIndex=found_index, **search_properties)
        if menu.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return menu
        else:
            return None

    @staticmethod
    def GMenuItemControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.MenuItemControl, None):
        menu_item = uia.MenuItemControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                        searchInterval=search_interval,
                                        foundIndex=found_index, **search_properties)
        if menu_item.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return menu_item
        else:
            return None

    @staticmethod
    def GPaneControl(search_from_control, search_depth: int, search_interval: float,
                     found_index: int,
                     **search_properties) -> (uia.PaneControl, None):
        pane = uia.PaneControl(ssearchFromControl=search_from_control, searchDepth=search_depth,
                               searchInterval=search_interval,
                               foundIndex=found_index, **search_properties)
        if pane.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return pane
        else:
            return None

    @staticmethod
    def GProgressbarControl(search_from_control, search_depth: int, search_interval: float,
                            found_index: int,
                            **search_properties) -> (uia.ProgressBarControl, None):
        progressbar = uia.ProgressBarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                             searchInterval=search_interval,
                                             foundIndex=found_index, **search_properties)
        if progressbar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return progressbar
        else:
            return None

    @staticmethod
    def GRadiobuttonControl(search_from_control, search_depth: int, search_interval: float,
                            found_index: int,
                            **search_properties) -> (uia.RadioButtonControl, None):
        radiobutton = uia.RadioButtonControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                             searchInterval=search_interval,
                                             foundIndex=found_index, **search_properties)
        if radiobutton.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return radiobutton
        else:
            return None

    @staticmethod
    def GScrollbarControl(search_from_control, search_depth: int, search_interval: float,
                          found_index: int,
                          **search_properties) -> (uia.ScrollBarControl, None):
        scrollbar = uia.ScrollBarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                         searchInterval=search_interval,
                                         foundIndex=found_index, **search_properties)
        if scrollbar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return scrollbar
        else:
            return None

    @staticmethod
    def GSemanticZoomControl(search_from_control, search_depth: int, search_interval: float,
                             found_index: int,
                             **search_properties) -> (uia.SemanticZoomControl, None):
        semantic_zoom = uia.SemanticZoomControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                                searchInterval=search_interval,
                                                foundIndex=found_index, **search_properties)
        if semantic_zoom.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return semantic_zoom
        else:
            return None

    @staticmethod
    def GSeparatorControl(search_from_control, search_depth: int, search_interval: float,
                          found_index: int,
                          **search_properties) -> (uia.SeparatorControl, None):
        separator = uia.SeparatorControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                         searchInterval=search_interval,
                                         foundIndex=found_index, **search_properties)
        if separator.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return separator
        else:
            return None

    @staticmethod
    def GSliderControl(search_from_control, search_depth: int, search_interval: float,
                       found_index: int,
                       **search_properties) -> (uia.SliderControl, None):
        slider = uia.SliderControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                   searchInterval=search_interval,
                                   foundIndex=found_index, **search_properties)
        if slider.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return slider
        else:
            return None

    @staticmethod
    def GSplitButtonControl(search_from_control, search_depth: int, search_interval: float,
                            found_index: int,
                            **search_properties) -> (uia.SplitButtonControl, None):
        split_button = uia.SplitButtonControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                              searchInterval=search_interval,
                                              foundIndex=found_index, **search_properties)
        if split_button.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return split_button
        else:
            return None

    @staticmethod
    def GSpinnerControl(search_from_control, search_depth: int, search_interval: float,
                        found_index: int,
                        **search_properties) -> (uia.SpinnerControl, None):
        spinner = uia.SpinnerControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                     searchInterval=search_interval,
                                     foundIndex=found_index, **search_properties)
        if spinner.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return spinner
        else:
            return None

    @staticmethod
    def GStatusBarControl(search_from_control, search_depth: int, search_interval: float,
                          found_index: int,
                          **search_properties) -> (uia.StatusBarControl, None):
        status_bar = uia.StatusBarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                          searchInterval=search_interval,
                                          foundIndex=found_index, **search_properties)
        if status_bar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return status_bar
        else:
            return None

    @staticmethod
    def GTabControl(search_from_control, search_depth: int, search_interval: float,
                    found_index: int,
                    **search_properties) -> (uia.TabControl, None):
        tab_control = uia.TabControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                     searchInterval=search_interval,
                                     foundIndex=found_index, **search_properties)
        if tab_control.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return tab_control
        else:
            return None

    @staticmethod
    def GTabItemControl(search_from_control, search_depth: int, search_interval: float,
                        found_index: int,
                        **search_properties) -> (uia.TabItemControl, None):
        tab_item = uia.TabItemControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                      searchInterval=search_interval,
                                      foundIndex=found_index, **search_properties)
        if tab_item.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return tab_item
        else:
            return None

    @staticmethod
    def GTableControl(search_from_control, search_depth: int, search_interval: float,
                      found_index: int,
                      **search_properties) -> (uia.TableControl, None):
        table = uia.TableControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                 searchInterval=search_interval,
                                 foundIndex=found_index, **search_properties)
        if table.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return table
        else:
            return None

    @staticmethod
    def GTextControl(search_from_control, search_depth: int, search_interval: float,
                     found_index: int,
                     **search_properties) -> (uia.TextControl, None):
        text = uia.TextControl(searchFromControl=search_from_control, searchDepth=search_depth,
                               searchInterval=search_interval,
                               foundIndex=found_index, **search_properties)
        if text.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return text
        else:
            return None

    @staticmethod
    def GThumbControl(search_from_control, search_depth: int, search_interval: float,
                      found_index: int,
                      **search_properties) -> (uia.ThumbControl, None):
        thumb = uia.ThumbControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                 searchInterval=search_interval,
                                 foundIndex=found_index, **search_properties)
        if thumb.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return thumb
        else:
            return None

    @staticmethod
    def GTitleBarControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.TitleBarControl, None):
        title_bar = uia.TitleBarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                        searchInterval=search_interval,
                                        foundIndex=found_index, **search_properties)
        if title_bar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return title_bar
        else:
            return None

    @staticmethod
    def GToolBarControl(search_from_control, search_depth: int, search_interval: float,
                        found_index: int,
                        **search_properties) -> (uia.ToolBarControl, None):
        tool_bar = uia.ToolBarControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                      searchInterval=search_interval,
                                      foundIndex=found_index, **search_properties)
        if tool_bar.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return tool_bar
        else:
            return None

    @staticmethod
    def GToolTipControl(search_from_control, search_depth: int, search_interval: float,
                        found_index: int,
                        **search_properties) -> (uia.ToolTipControl, None):
        tool_tip = uia.ToolTipControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                      searchInterval=search_interval,
                                      foundIndex=found_index, **search_properties)
        if tool_tip.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return tool_tip
        else:
            return None

    @staticmethod
    def GTreeControl(search_from_control, search_depth: int, search_interval: float,
                     found_index: int,
                     **search_properties) -> (uia.TreeControl, None):
        tree = uia.TreeControl(searchFromControl=search_from_control, searchDepth=search_depth,
                               searchInterval=search_interval,
                               foundIndex=found_index, **search_properties)
        if tree.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return tree
        else:
            return None

    @staticmethod
    def GTreeItemControl(search_from_control, search_depth: int, search_interval: float,
                         found_index: int,
                         **search_properties) -> (uia.TreeItemControl, None):
        tree_item = uia.TreeItemControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                        searchInterval=search_interval,
                                        foundIndex=found_index, **search_properties)
        if tree_item.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return tree_item
        else:
            return None

    @staticmethod
    def GWindowControl(search_from_control, search_depth: int,
                       search_interval: float,
                       found_index: int,
                       **search_properties) -> (uia.WindowControl, None):
        window = uia.WindowControl(searchFromControl=search_from_control, searchDepth=search_depth,
                                   searchInterval=search_interval,
                                   foundIndex=found_index, **search_properties)
        if window.Exists(maxSearchSeconds=MAX_SEARCH_SECONDS):
            return window
        else:
            return None


class GOperator:
    def __init__(self, control: (uia.Control, uia.WindowControl, uia.PaneControl), operation_detail: dict):
        self.operation_detail = operation_detail
        self.control = control

    @property
    def operation(self) -> list:
        operation = self.operation_detail.get(GUIAFieldsMap.operation, '')
        if operation != '':
            operation = operation.split(',')
            return operation
        else:
            return []

    @property
    def value(self):
        value = self.operation_detail.get(GUIAFieldsMap.value, None)
        # if GOperationMap.SendKeys in self.operation or GOperationMap.SendKey in self.operation:
        #     if not value:
        #         raise ValueError('Operation is "SendKeys" or "SendKey","Value" can not be None')
        #     else:
        #         pass
        return value

    @property
    def maxSearchSeconds(self):
        value = self.operation_detail.get(GUIAFieldsMap.maxSearchSeconds, MAX_SEARCH_SECONDS)
        return value

    @property
    def searchIntervalSeconds(self):
        value = self.operation_detail.get(GUIAFieldsMap.searchIntervalSeconds, SEARCH_INTERVAL)
        return value

    @property
    def printIfNotExist(self):
        value = self.operation_detail.get(GUIAFieldsMap.printIfNotExist, False)
        return value

    @property
    def raiseException(self):
        value = self.operation_detail.get(GUIAFieldsMap.raiseException, True)
        return value

    @property
    def printIfNotDisappear(self):
        value = self.operation_detail.get(GUIAFieldsMap.printIfNotDisappear, False)
        return value

    @property
    def x(self):
        value = self.operation_detail.get(GUIAFieldsMap.x, None)
        return value

    @property
    def y(self):
        value = self.operation_detail.get(GUIAFieldsMap.y, None)
        return value

    @property
    def ratioX(self):
        value = self.operation_detail.get(GUIAFieldsMap.ratioX, 0.5)
        return value

    @property
    def ratioY(self):
        value = self.operation_detail.get(GUIAFieldsMap.ratioY, 0.5)
        return value

    @property
    def simulateMove(self):
        value = self.operation_detail.get(GUIAFieldsMap.simulateMove, True)
        return value

    @property
    def dragDropX1(self):
        value = self.operation_detail.get(GUIAFieldsMap.dragDropX1, '')
        return value

    @property
    def dragDropX2(self):
        value = self.operation_detail.get(GUIAFieldsMap.dragDropX2, '')
        return value

    @property
    def dragDropY1(self):
        value = self.operation_detail.get(GUIAFieldsMap.dragDropY1, '')
        return value

    @property
    def dragDropY2(self):
        value = self.operation_detail.get(GUIAFieldsMap.dragDropY2, '')
        return value

    @property
    def moveSpeed(self):
        value = self.operation_detail.get(GUIAFieldsMap.moveSpeed, 1)
        return value

    @property
    def waitTime(self):
        value = self.operation_detail.get(GUIAFieldsMap.waitTime, OPERATION_WAIT_TIME)
        return value

    @property
    def wheelTimes(self):
        value = self.operation_detail.get(GUIAFieldsMap.wheelTimes, 1)
        return value

    @property
    def interval(self):
        value = self.operation_detail.get(GUIAFieldsMap.interval, 0.05)
        return value

    @property
    def cmdShow(self):
        value = self.operation_detail.get(GUIAFieldsMap.cmdShow, None)
        return value

    @property
    def moveWindowX(self):
        value = self.operation_detail.get(GUIAFieldsMap.moveWindowX, None)
        return value

    @property
    def moveWindowY(self):
        value = self.operation_detail.get(GUIAFieldsMap.moveWindowY, None)
        return value

    @property
    def moveWindowWidth(self):
        value = self.operation_detail.get(GUIAFieldsMap.moveWindowWidth, None)
        return value

    @property
    def moveWindowHeight(self):
        value = self.operation_detail.get(GUIAFieldsMap.moveWindowHeight, None)
        return value

    @property
    def repaint(self):
        value = self.operation_detail.get(GUIAFieldsMap.repaint, None)
        return value

    @property
    def text(self):
        value = self.operation_detail.get(GUIAFieldsMap.text, None)
        return value

    @property
    def savePath(self):
        value = self.operation_detail.get(GUIAFieldsMap.savePath, None)
        return value

    @property
    def imageX(self):
        value = self.operation_detail.get(GUIAFieldsMap.imageX, 0)
        return value

    @property
    def imageY(self):
        value = self.operation_detail.get(GUIAFieldsMap.imageY, 0)
        return value

    @property
    def imageWidth(self):
        value = self.operation_detail.get(GUIAFieldsMap.imageWidth, 0)
        return value

    @property
    def imageHeight(self):
        value = self.operation_detail.get(GUIAFieldsMap.imageHeight, 0)
        return value

    @property
    def bitMapX(self):
        value = self.operation_detail.get(GUIAFieldsMap.bitMapX, 0)
        return value

    @property
    def bitMapY(self):
        value = self.operation_detail.get(GUIAFieldsMap.bitMapY, 0)
        return value

    @property
    def bitMapWidth(self):
        value = self.operation_detail.get(GUIAFieldsMap.bitMapWidth, 0)
        return value

    @property
    def bitMapHeight(self):
        value = self.operation_detail.get(GUIAFieldsMap.bitMapHeight, 0)
        return value

    @property
    def key(self):
        value = self.operation_detail.get(GUIAFieldsMap.key, None)
        return value

    @property
    def hotKey(self):
        value = self.operation_detail.get(GUIAFieldsMap.hotKey, None)
        return value

    @property
    def legacyPatternValue(self):
        value = self.operation_detail.get(GUIAFieldsMap.legacyPatternValue, None)
        return value

    def __fields_middle(self):
        fields = dict()
        fields[GUIAFieldsMap.value] = self.value
        fields[GUIAFieldsMap.maxSearchSeconds] = self.maxSearchSeconds
        fields[GUIAFieldsMap.searchIntervalSeconds] = self.searchIntervalSeconds
        fields[GUIAFieldsMap.printIfNotExist] = self.printIfNotExist
        fields[GUIAFieldsMap.raiseException] = self.raiseException
        fields[GUIAFieldsMap.printIfNotDisappear] = self.printIfNotDisappear
        fields[GUIAFieldsMap.operation] = self.operation
        fields[GUIAFieldsMap.x] = self.x
        fields[GUIAFieldsMap.y] = self.y
        fields[GUIAFieldsMap.ratioX] = self.ratioX
        fields[GUIAFieldsMap.ratioY] = self.ratioY
        fields[GUIAFieldsMap.simulateMove] = self.simulateMove
        fields[GUIAFieldsMap.dragDropX1] = self.dragDropX1
        fields[GUIAFieldsMap.dragDropX2] = self.dragDropX2
        fields[GUIAFieldsMap.dragDropY1] = self.dragDropY1
        fields[GUIAFieldsMap.dragDropY2] = self.dragDropY2
        fields[GUIAFieldsMap.moveWindowX] = self.moveWindowX
        fields[GUIAFieldsMap.moveWindowY] = self.moveWindowY
        fields[GUIAFieldsMap.moveWindowHeight] = self.moveWindowHeight
        fields[GUIAFieldsMap.moveWindowWidth] = self.moveWindowWidth
        fields[GUIAFieldsMap.moveSpeed] = self.moveSpeed
        fields[GUIAFieldsMap.waitTime] = self.waitTime
        fields[GUIAFieldsMap.interval] = self.interval
        fields[GUIAFieldsMap.cmdShow] = self.cmdShow
        fields[GUIAFieldsMap.repaint] = self.repaint
        fields[GUIAFieldsMap.text] = self.text
        fields[GUIAFieldsMap.savePath] = self.savePath
        fields[GUIAFieldsMap.imageX] = self.imageX
        fields[GUIAFieldsMap.imageY] = self.imageY
        fields[GUIAFieldsMap.imageHeight] = self.imageHeight
        fields[GUIAFieldsMap.imageWidth] = self.imageWidth
        fields[GUIAFieldsMap.bitMapX] = self.bitMapX
        fields[GUIAFieldsMap.bitMapY] = self.bitMapY
        fields[GUIAFieldsMap.bitMapHeight] = self.bitMapHeight
        fields[GUIAFieldsMap.bitMapWidth] = self.bitMapWidth
        fields[GUIAFieldsMap.key] = self.key
        fields[GUIAFieldsMap.hotKey] = self.hotKey
        fields[GUIAFieldsMap.wheelTimes] = self.wheelTimes
        fields[GUIAFieldsMap.legacyPatternValue] = self.legacyPatternValue
        return fields

    def get_field(self):
        return self.__fields_middle()
    
    def __operation_middle(self):
        operation_ = dict()
        operation_[GOperationMap.SetFocus] = self.SetFocus
        operation_[GOperationMap.SendKey] = self.SendKey
        operation_[GOperationMap.SendKeys] = self.SendKeys
        operation_[GOperationMap.Click] = self.Click
        operation_[GOperationMap.DoubleClick] = self.DoubleClick
        operation_[GOperationMap.MiddleClick] = self.MiddleClick
        operation_[GOperationMap.RightClick] = self.RightClick
        operation_[GOperationMap.CaptureToImage] = self.CaptureToImage
        operation_[GOperationMap.Exists] = self.Exists
        operation_[GOperationMap.ReFind] = self.ReFind
        operation_[GOperationMap.Disappears] = self.Disappears
        operation_[GOperationMap.MoveCursorToMyCenter] = self.MoveCursorToMyCenter
        operation_[GOperationMap.MoveCursorToInnerPos] = self.MoveCursorToInnerPos
        operation_[GOperationMap.DragDrop] = self.DragDrop
        operation_[GOperationMap.RightDragDrop] = self.RightDragDrop
        operation_[GOperationMap.WheelUp] = self.WheelUp
        operation_[GOperationMap.WheelDown] = self.WheelDown
        operation_[GOperationMap.Show] = self.Show
        operation_[GOperationMap.ShowWindow] = self.ShowWindow
        operation_[GOperationMap.Hide] = self.Hide
        operation_[GOperationMap.MoveWindow] = self.MoveWindow
        operation_[GOperationMap.SetWindowText] = self.SetWindowText
        operation_[GOperationMap.GetWindowText] = self.GetWindowText
        operation_[GOperationMap.ToBitMap] = self.ToBitMap
        operation_[GOperationMap.SetActive] = self.SetActive
        operation_[GOperationMap.SetTopMost] = self.SetTopMost
        operation_[GOperationMap.HotKey] = self.HotKey
        return operation_

    @OperationFinder
    def start(self) -> (None, int):
        switch = self.__operation_middle()
        for operation in self.operation:
            operation_func = switch.get(operation, None)
            if operation_func:
                if self.control == -1:
                    continue
                else:
                    operation_func()
            else:
                return operation

    def test(self):
        print(self.control)
        print(self.operation)
        print(self.value)

    def GetChildren(self):
        control = self.control.GetChildren()
        return control

    def GetFirstChildControl(self):
        control = self.control.GetFirstChildControl()
        return control

    def GetLastChildControl(self):
        control = self.control.GetLastChildControl()
        return control

    def GetNextSiblingControl(self):
        control = self.control.GetNextSiblingControl()
        return control

    def GetPreviousSiblingControl(self):
        control = self.control.GetPreviousSiblingControl()
        return control

    def Click(self) -> None:
        self.control.Click()
        return None

    def DoubleClick(self) -> None:
        self.control.DoubleClick()
        return None

    def MiddleClick(self) -> None:
        self.control.MiddleClick()
        return None

    def RightClick(self) -> None:
        self.control.RightClick()
        return None

    @RelatedFields(key=GUIAFieldsMap.key)
    def SendKey(self) -> None:
        """
        参数 key 需参考 class Key
        :return:
        """
        return self.control.SendKey(key=self.key)

    @RelatedFields(maxSearchSeconds=GUIAFieldsMap.value)
    def SendKeys(self) -> None:
        return self.control.SendKeys(self.value)

    def SetFocus(self) -> None:
        self.control.SetFocus()
        return None

    @RelatedFields(maxSearchSeconds=GUIAFieldsMap.maxSearchSeconds,
                   searchIntervalSeconds=GUIAFieldsMap.searchIntervalSeconds,
                   printIfNotExist=GUIAFieldsMap.printIfNotExist)
    def Exists(self):
        state = self.control.Exists(maxSearchSeconds=self.maxSearchSeconds,
                                    searchIntervalSeconds=self.searchIntervalSeconds,
                                    printIfNotExist=self.printIfNotExist)
        return state

    @RelatedFields(maxSearchSeconds=GUIAFieldsMap.maxSearchSeconds,
                   searchIntervalSeconds=GUIAFieldsMap.searchIntervalSeconds,
                   raiseException=GUIAFieldsMap.raiseException)
    def ReFind(self):
        state = self.control.Refind(maxSearchSeconds=self.maxSearchSeconds,
                                    searchIntervalSeconds=self.searchIntervalSeconds,
                                    raiseException=self.raiseException)
        return state

    @RelatedFields(maxSearchSeconds=GUIAFieldsMap.maxSearchSeconds,
                   searchIntervalSeconds=GUIAFieldsMap.searchIntervalSeconds,
                   printIfNotDisappear=GUIAFieldsMap.printIfNotDisappear)
    def Disappears(self):
        state = self.control.Disappears(maxSearchSeconds=self.maxSearchSeconds,
                                        searchIntervalSeconds=self.searchIntervalSeconds,
                                        printIfNotDisappear=self.printIfNotDisappear)
        return state

    @RelatedFields(x=GUIAFieldsMap.x, y=GUIAFieldsMap.y, ratioX=GUIAFieldsMap.ratioX, ratioY=GUIAFieldsMap.ratioY,
                   simulateMove=GUIAFieldsMap.simulateMove)
    def MoveCursorToInnerPos(self):
        """
        将光标移动到控件的内部位置，默认居中。
        :return: (x,y) / None
        """
        x_y = self.control.MoveCursorToInnerPos(x=self.x, y=self.y, ratioX=self.ratioX, ratioY=self.ratioY,
                                                simulateMove=self.simulateMove)
        return x_y

    @RelatedFields(simulateMove=GUIAFieldsMap.simulateMove)
    def MoveCursorToMyCenter(self):
        """
        将光标移动到控件的中心。
        :return: (x,y) / None
        """
        x_y = self.control.MoveCursorToMyCenter(simulateMove=self.simulateMove)
        return x_y

    @RelatedFields(dragDropX1=GUIAFieldsMap.dragDropX1, dragDropX2=GUIAFieldsMap.dragDropX2,
                   dragDropY1=GUIAFieldsMap.dragDropY1, dragDropY2=GUIAFieldsMap.dragDropY2,
                   moveSpeed=GUIAFieldsMap.moveSpeed, waitTime=GUIAFieldsMap.waitTime)
    def DragDrop(self):
        """
        拖拽
        :return:
        """
        self.control.DragDrop(x1=self.dragDropX1, x2=self.dragDropX2, y1=self.dragDropY1, y2=self.dragDropY2,
                              moveSpeed=self.moveSpeed, waitTime=self.waitTime)
        return None

    @RelatedFields(dragDropX1=GUIAFieldsMap.dragDropX1, dragDropX2=GUIAFieldsMap.dragDropX2,
                   dragDropY1=GUIAFieldsMap.dragDropY1, dragDropY2=GUIAFieldsMap.dragDropY2,
                   moveSpeed=GUIAFieldsMap.moveSpeed, waitTime=GUIAFieldsMap.waitTime)
    def RightDragDrop(self):
        self.control.RightDragDrop(x1=self.dragDropX1, x2=self.dragDropX2, y1=self.dragDropY1, y2=self.dragDropY2,
                                   moveSpeed=self.moveSpeed, waitTime=self.waitTime)
        return None

    @RelatedFields(ratioX=GUIAFieldsMap.ratioX, ratioY=GUIAFieldsMap.ratioY,
                   wheelTimes=GUIAFieldsMap.wheelTimes, interval=GUIAFieldsMap.interval,
                   waitTime=GUIAFieldsMap.waitTime)
    def WheelDown(self):
        """
        鼠标滚轮, 向下滚动
        :return:
        """
        self.control.WheelDown(x=self.x, y=self.y, ratioX=self.ratioX, ratioY=self.ratioY, wheelTimes=self.wheelTimes,
                               interval=self.interval, waitTime=self.waitTime)
        return None

    @RelatedFields(x=GUIAFieldsMap.x, y=GUIAFieldsMap.y, ratioX=GUIAFieldsMap.ratioX, ratioY=GUIAFieldsMap.ratioY,
                   wheelTimes=GUIAFieldsMap.wheelTimes, interval=GUIAFieldsMap.interval,
                   waitTime=GUIAFieldsMap.waitTime)
    def WheelUp(self):
        """
        鼠标滚轮 向上滚
        :return:
        """
        self.control.WheelUp(ratioX=self.ratioX, ratioY=self.ratioY, wheelTimes=self.wheelTimes,
                             interval=self.interval, waitTime=self.waitTime)
        return None

    @RelatedFields(cmdShow=GUIAFieldsMap.cmdShow, waitTime=GUIAFieldsMap.waitTime)
    def ShowWindow(self):
        """
        控件显示状态
        cmdShow：   Hide = 0
                    ShowNormal = 1
                    Normal = 1
                    ShowMinimized = 2
                    ShowMaximized = 3
                    Maximize = 3
                    ShowNoActivate = 4
                    Show = 5
                    Minimize = 6
                    ShowMinNoActive = 7
                    ShowNA = 8
                    Restore = 9
                    ShowDefault = 10
                    ForceMinimize = 11
                    Max = 11
        :return:
        """
        self.control.ShowWindow(cmdShow=self.cmdShow, waitTime=self.waitTime)
        return None

    @RelatedFields(waitTime=GUIAFieldsMap.waitTime)
    def Show(self) -> bool:
        """
        窗口状态：显示
        Return bool, True if succeed otherwise False.
        """
        return self.control.ShowWindow(cmdShow=SW.Show, waitTime=self.waitTime)

    @RelatedFields(waitTime=GUIAFieldsMap.waitTime)
    def Hide(self) -> bool:
        """
        窗口状态：隐藏
        waitTime: float
        Return bool, True if succeed otherwise False.
        """
        return self.control.ShowWindow(cmdShow=SW.Hide, waitTime=self.waitTime)

    def GetWindowText(self):
        return self.control.GetWindowText()

    @RelatedFields(moveWindowX=GUIAFieldsMap.moveWindowX, moveWindowY=GUIAFieldsMap.moveWindowY,
                   moveWindowHeight=GUIAFieldsMap.moveWindowHeight, moveWindowWidth=GUIAFieldsMap.moveWindowWidth,
                   repaint=GUIAFieldsMap.repaint)
    def MoveWindow(self):
        return self.control.MoveWindow(x=self.moveWindowX, y=self.moveWindowY, width=self.moveWindowWidth,
                                       height=self.moveWindowHeight, repaint=self.repaint)

    @RelatedFields(text=GUIAFieldsMap.text)
    def SetWindowText(self):
        return self.control.SetWindowText(text=self.text)

    @RelatedFields(savePath=GUIAFieldsMap.savePath, imageX=GUIAFieldsMap.imageX, imageY=GUIAFieldsMap.imageY,
                   imageWidth=GUIAFieldsMap.imageWidth, imageHeight=GUIAFieldsMap.imageHeight)
    def CaptureToImage(self):
        """
        将控件转为图片
        :return: 
        """
        return self.control.CaptureToImage(savePath=self.savePath, x=self.imageX, y=self.imageY, width=self.imageWidth,
                                           height=self.imageHeight)

    @RelatedFields(bitMapX=GUIAFieldsMap.bitMapX, bitMapY=GUIAFieldsMap.bitMapY, bitMapWidth=GUIAFieldsMap.bitMapWidth,
                   bitMapHeight=GUIAFieldsMap.bitMapHeight)
    def ToBitMap(self):
        """
        将控件转为位图
        :return: 
        """
        return self.control.ToBitmap(x=self.bitMapX, y=self.bitMapY, width=self.bitMapWidth, height=self.bitMapHeight)

    def SetTopMost(self):
        if isinstance(self.control, (uia.PaneControl, uia.WindowControl)):
            return self.control.SetTopmost(isTopmost=True)
        else:
            return -1

    def SetActive(self):
        if isinstance(self.control, (uia.PaneControl, uia.WindowControl)):
            return self.control.SetActive()
        else:
            return -1

    @RelatedFields(hotKey='hotKey')
    def HotKey(self):
        return self.control.SendKeys(text=self.hotKey)

    @RelatedFields(LegacyPatternSetValue=GUIAFieldsMap.legacyPatternValue)
    def LegacyPatternSetValue(self):
        return self.control.GetLegacyIAccessiblePattern().SetValue(self.legacyPatternValue)


def execute(operation_list: [dict]):
    global CONTROL
    for i, operation in enumerate(operation_list):
        is_uia = operation.get('isUIA', '')
        if is_uia == '' or is_uia is True:
            g_control_obj = GControl(operation_detail=operation, operation_index=i+1)
            g_control = g_control_obj.start()
            print('序号：{} ==== '.format(i+1), g_control)
            g_operator = GOperator(control=g_control, operation_detail=operation)
            g_operator.start()
            print('-' * 50)
        else:
            auto(operation)


if __name__ == '__main__':
    windows_version = platform.platform().split('-')[1]
    # youdao_dict = youdao_dict1[1]
    # word = word[0]
    # g_control_obj = GControl(operation_detail=word, operation_index=1)
    # g_control_obj.test()
