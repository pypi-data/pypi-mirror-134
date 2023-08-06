# -*- coding: utf-8 -*-
import time

import autoit as auto
from main.decorator import *

TIMEOUT = 30


class GAutoItMap:
    WinWait = 'WinWait'
    WinWaitByHandle = 'WinWaitByHandle'
    WinClose = 'WinClose'
    WinCloseByHandle = 'WinCloseByHandle'
    WinKill = 'WinKill'
    Send = 'Send'
    WinKillByHandle = 'WinKillByHandle'
    WinActivate = 'WinActivate'
    WinActivateByHandle = 'WinActivateByHandle'
    WinWaitActivate = 'WinWaitActivate'
    WinWaitActivateByHandle = 'WinWaitActivateByHandle'
    WinExists = 'WinExists'
    WinExistsByHandle = 'WinExistsByHandle'
    WinActive = 'WinActive'
    WinActiveByHandle = 'WinActiveByHandle'
    WinGetCaretPos = 'WinGetCaretPos'
    WinGetClassList = 'WinGetClassList'
    WinGetClassListByHandle = 'WinGetClassListByHandle'
    WinGetClientSize = 'WinGetClientSize'
    WinGetClientSizeByHandle = 'WinGetClientSizeByHandle'
    WinGetHandle = 'WinGetHandle'
    WinGetHandleAsText = 'WinGetHandleAsText'
    WinGetPos = 'WinGetPos'
    WinGetPosByHandle = 'WinGetPosByHandle'
    WinGetProcess = 'WinGetProcess'
    WinGetProcessByHandle = 'WinGetProcessByHandle'
    WinGetState = 'WinGetState'
    WinGetStateByHandle = 'WinGetStateByHandle'
    WinGetText = 'WinGetText'
    WinGetTextByHandle = 'WinGetTextByHandle'
    WinGetTitle = 'WinGetTitle'
    WinGetTitleByHandle = 'WinGetTitleByHandle'
    WinMenuSelectItem = 'WinMenuSelectItem'
    WinMenuSelectItemByHandle = 'WinMenuSelectItemByHandle'
    WinMinimizeAll = 'WinMinimizeAll'
    WinMinimizeAllUndo = 'WinMinimizeAllUndo'
    WinMove = 'WinMove'
    WinMoveByHandle = 'WinMoveByHandle'
    WinTopMost = 'WinTopMost'
    WinUnTop = 'WinUnTop'
    WinTopMostByHandle = 'WinTopMostByHandle'
    WinUnTopByHandle = 'WinUnTopByHandle'
    WinHide = 'WinHide'
    WinHideByHandle = 'WinHideByHandle'
    WinShow = 'WinShow'
    WinShowByHandle = 'WinShowByHandle'
    WinMin = 'WinMin'
    WinMinByHandle = 'WinMinByHandle'
    WinMax = 'WinMax'
    WinMaxByHandle = 'WinMaxByHandle'
    WinRestore = 'WinRestore'
    WinRestoreByHandle = 'WinRestoreByHandle'
    WinNormal = 'WinNormal'
    WinNormalByHandle = 'WinNormalByHandle'
    WinDisable = 'WinDisable'
    WinDisableByHandle = 'WinDisableByHandle'
    WinMinDisable = 'WinMinDisable'
    WinMinDisableByHandle = 'WinMinDisableByHandle'
    WinNa = 'WinNa'
    WinNaByHandle = 'WinNaByHandle'
    WinDefault = 'WinDefault'
    WinDefaultByHandle = 'WinDefaultByHandle'
    WinSetTile = 'WinSetTile'
    WinSetTitleByHandle = 'WinSetTitleByHandle'
    WinSetTrans = 'WinSetTrans'
    WinSetTransByHandle = 'WinSetTransByHandle'
    WinWaitClose = 'WinWaitClose'
    WinWaitCloseByHandle = 'WinWaitCloseByHandle'
    WinWaitNotActive = 'WinWaitNotActive'
    WinWaitNotActiveByHandle = 'WinWaitNotActiveByHandle'
    CtlLeftClick = 'CtlLeftClick'
    CtlLeftClickByHandle = 'CtlLeftClickByHandle'
    CtlDoubleclick = 'CtlDoubleclick'
    CtlDoubleClickByHandle = 'CtlDoubleClickByHandle'
    CtlRightClick = 'CtlRightClick'
    CtlRightClickByHandle = 'CtlRightClickByHandle'
    CtlRightDoubleClick = 'CtlRightDoubleClick'
    CtlRightDoubleClickByHandle = 'CtlRightDoubleClickByHandle'
    CtlSend = 'CtlSend'
    CtlSendByHandle = 'CtlSendByHandle'
    CtlSetText = 'CtlSetText'
    CtlSetTextByHandle = 'CtlSetTextByHandle'
    CtlCommand = 'CtlCommand'
    CtlCommandByHandle = 'CtlCommandByHandle'
    CtlListView = 'CtlListView'
    CtlListViewByHandle = 'CtlListViewByHandle'
    CtlDisable = 'CtlDisable'
    CtlDisableByHandle = 'CtlDisableByHandle'
    CtlEnable = 'CtlEnable'
    CtlEnableByHandle = 'CtlEnableByHandle'
    CtlFocus = 'CtlFocus'
    CtlFocusByHandle = 'CtlFocusByHandle'
    CtlGetFocus = 'CtlGetFocus'
    CtlGetFocusByHandle = 'CtlGetFocusByHandle'
    CtlGetHandle = 'CtlGetHandle'
    CtlGetHandleAsText = 'CtlGetHandleAsText'
    CtlGetPos = 'CtlGetPos'
    CtlGetPosByHandle = 'CtlGetPosByHandle'
    CtlGetText = 'CtlGetText'
    CtlGetTextByHandle = 'CtlGetTextByHandle'
    CtlHide = 'CtlHide'
    CtlHideByHandle = 'CtlHideByHandle'
    CtlMove = 'CtlMove'
    CtlMoveByHandle = 'CtlMoveByHandle'
    CtlShow = 'CtlShow'
    CtlShowByHandle = 'CtlShowByHandle'
    CtlTreeView = 'CtlTreeView'
    CtlTreeViewByHandle = 'CtlTreeViewByHandle'


class GAutoItFieldsMap:
    openApp = 'openApp'
    winTitle = 'winTitle'
    winHandle = 'winHandle'
    winText = 'winText'
    ctlHandle = 'ctlHandle'
    ctlClassNameNN = 'ctlClassNameNN'
    treeViewCommand = 'treeViewCommand'
    treeViewExtra1 = 'treeViewExtra1'
    treeViewExtra2 = 'treeViewExtra2'
    ctlMoveX = 'ctlMoveX'
    ctlMoveY = 'ctlMoveY'
    ctlMoveWidth = 'ctlMoveWidth'
    ctlMoveHeight = 'ctlMoveHeight'
    listViewCommand = 'listViewCommand'
    listViewExtra1 = 'listViewExtra1'
    listViewExtra2 = 'listViewExtra2'
    command = 'command'
    commandExtra = 'commandExtra'
    ctlText = 'ctlText'
    menuItem = 'menuItem'
    winMoveX = 'winMoveX'
    winMoveY = 'winMoveY'
    winMoveHeight = 'winMoveHeight'
    winMoveWeight = 'winMoveWeight'
    winNewTitle = 'winNewTitle'
    winTrans = 'winTrans'
    operation = 'operation'
    ctlSendValue = 'ctlSendValue'
    sendValue = 'sendValue'
    raiseIfNotExist = 'raiseIfNotExist'


class GAutoIt:
    def __init__(self, **kwargs):
        self.kwargs = kwargs.get('operation_detail')

    def start(self):
        self.OpenAPP()
        switch = self.__switch_middle()
        for operation in self.Operation:
            fuc = switch.get(operation, None)
            # print(fuc)
            if fuc:
                fuc()
            else:
                pass

    def OpenAPP(self):
        if self.OpenApp == '':
            pass
        else:
            # print(self.OpenApp)
            auto.run(self.OpenApp)

    def __switch_middle(self):
        switch = dict()
        # 控件操作
        switch[GAutoItMap.CtlLeftClick] = self.CtlLeftClick
        switch[GAutoItMap.CtlLeftClickByHandle] = self.CtlLeftClickByHandle
        switch[GAutoItMap.CtlRightClick] = self.CtlRightClick
        switch[GAutoItMap.CtlRightClickByHandle] = self.CtlRightClickByHandle
        switch[GAutoItMap.CtlDoubleclick] = self.CtlDoubleclick
        switch[GAutoItMap.CtlDoubleClickByHandle] = self.CtlDoubleClickByHandle
        switch[GAutoItMap.CtlRightDoubleClick] = self.CtlRightDoubleClick
        switch[GAutoItMap.CtlRightDoubleClickByHandle] = self.CtlRightDoubleClickByHandle
        switch[GAutoItMap.CtlSend] = self.CtlSend
        switch[GAutoItMap.CtlSendByHandle] = self.CtlSendByHandle
        switch[GAutoItMap.CtlSetText] = self.CtlSetText
        switch[GAutoItMap.CtlSetTextByHandle] = self.CtlSetTextByHandle
        switch[GAutoItMap.CtlShow] = self.CtlShow
        switch[GAutoItMap.CtlShowByHandle] = self.CtlShowByHandle
        switch[GAutoItMap.CtlTreeView] = self.CtlTreeView
        switch[GAutoItMap.CtlTreeViewByHandle] = self.CtlTreeViewByHandle
        switch[GAutoItMap.CtlCommand] = self.CtlCommand
        switch[GAutoItMap.CtlCommandByHandle] = self.CtlCommandByHandle
        switch[GAutoItMap.CtlDisable] = self.CtlDisable
        switch[GAutoItMap.CtlDisableByHandle] = self.CtlDisableByHandle
        switch[GAutoItMap.CtlEnable] = self.CtlEnable
        switch[GAutoItMap.CtlEnableByHandle] = self.CtlEnableByHandle
        switch[GAutoItMap.CtlFocus] = self.CtlFocus
        switch[GAutoItMap.CtlFocusByHandle] = self.CtlFocusByHandle
        switch[GAutoItMap.CtlGetFocus] = self.CtlGetFocus
        switch[GAutoItMap.CtlGetFocusByHandle] = self.CtlGetFocusByHandle
        switch[GAutoItMap.CtlGetHandle] = self.CtlGetHandle
        switch[GAutoItMap.CtlGetHandleAsText] = self.CtlGetHandleAsText
        switch[GAutoItMap.CtlGetPos] = self.CtlGetPos
        switch[GAutoItMap.CtlGetPosByHandle] = self.CtlGetPosByHandle
        switch[GAutoItMap.CtlGetText] = self.CtlGetText
        switch[GAutoItMap.CtlGetTextByHandle] = self.CtlGetTextByHandle
        switch[GAutoItMap.CtlHide] = self.CtlHide
        switch[GAutoItMap.CtlHideByHandle] = self.CtlHideByHandle
        switch[GAutoItMap.CtlSend] = self.CtlSend
        switch[GAutoItMap.CtlListView] = self.CtlListView
        switch[GAutoItMap.CtlListViewByHandle] = self.CtlListViewByHandle
        switch[GAutoItMap.CtlMove] = self.CtlMove
        switch[GAutoItMap.CtlMoveByHandle] = self.CtlMoveByHandle
        # 窗口操作
        switch[GAutoItMap.WinClose] = self.WinClose
        switch[GAutoItMap.WinCloseByHandle] = self.WinCloseByHandle
        switch[GAutoItMap.WinActivate] = self.WinActivate
        switch[GAutoItMap.WinActivateByHandle] = self.WinActivateByHandle
        switch[GAutoItMap.WinExists] = self.WinExists
        switch[GAutoItMap.WinExistsByHandle] = self.WinExistsByHandle
        switch[GAutoItMap.WinWait] = self.WinWait
        switch[GAutoItMap.WinWaitByHandle] = self.WinWaitByHandle
        switch[GAutoItMap.WinWaitActivate] = self.WinWaitActivate
        switch[GAutoItMap.WinWaitActivateByHandle] = self.WinWaitActivateByHandle
        switch[GAutoItMap.WinWaitNotActive] = self.WinWaitNotActive
        switch[GAutoItMap.WinWaitNotActiveByHandle] = self.WinWaitNotActiveByHandle
        switch[GAutoItMap.WinActive] = self.WinActive
        switch[GAutoItMap.WinActiveByHandle] = self.WinActiveByHandle
        switch[GAutoItMap.WinWaitClose] = self.WinWaitClose
        switch[GAutoItMap.WinWaitCloseByHandle] = self.WinWaitCloseByHandle
        switch[GAutoItMap.WinGetCaretPos] = self.WinGetCaretPos
        switch[GAutoItMap.WinGetClassList] = self.WinGetClassList
        switch[GAutoItMap.WinGetClassListByHandle] = self.WinGetClassListByHandle
        switch[GAutoItMap.WinGetClientSize] = self.WinGetClientSize
        switch[GAutoItMap.WinGetClientSizeByHandle] = self.WinGetClientSizeByHandle
        switch[GAutoItMap.WinGetHandle] = self.WinGetHandle
        switch[GAutoItMap.WinGetHandleAsText] = self.WinGetHandleAsText
        switch[GAutoItMap.WinGetProcess] = self.WinGetProcess
        switch[GAutoItMap.WinGetProcessByHandle] = self.WinGetProcessByHandle
        switch[GAutoItMap.WinGetState] = self.WinGetState
        switch[GAutoItMap.WinGetStateByHandle] = self.WinGetStateByHandle
        switch[GAutoItMap.WinGetText] = self.WinGetText
        switch[GAutoItMap.WinGetTextByHandle] = self.WinGetTextByHandle
        switch[GAutoItMap.WinGetPos] = self.WinGetPos
        switch[GAutoItMap.WinGetPosByHandle] = self.WinGetPosByHandle
        switch[GAutoItMap.WinGetTitle] = self.WinGetTitle
        switch[GAutoItMap.WinGetTitleByHandle] = self.WinGetTitleByHandle
        switch[GAutoItMap.WinSetTile] = self.WinSetTile
        switch[GAutoItMap.WinSetTitleByHandle] = self.WinSetTitleByHandle
        switch[GAutoItMap.WinSetTrans] = self.WinSetTrans
        switch[GAutoItMap.WinSetTransByHandle] = self.WinSetTransByHandle
        switch[GAutoItMap.WinTopMost] = self.WinTopMost
        switch[GAutoItMap.WinTopMostByHandle] = self.WinTopMostByHandle
        switch[GAutoItMap.WinUnTop] = self.WinUnTop
        switch[GAutoItMap.WinUnTopByHandle] = self.WinUnTopByHandle
        switch[GAutoItMap.WinMin] = self.WinMin
        switch[GAutoItMap.WinMinByHandle] = self.WinMinByHandle
        switch[GAutoItMap.WinMax] = self.WinMax
        switch[GAutoItMap.WinMaxByHandle] = self.WinMaxByHandle
        switch[GAutoItMap.WinMenuSelectItem] = self.WinMenuSelectItem
        switch[GAutoItMap.WinMenuSelectItemByHandle] = self.WinMenuSelectItemByHandle
        switch[GAutoItMap.WinMinDisable] = self.WinMinDisable
        switch[GAutoItMap.WinMinDisableByHandle] = self.WinMinDisableByHandle
        switch[GAutoItMap.WinMinimizeAll] = self.WinMinimizeAll
        switch[GAutoItMap.WinMinimizeAllUndo] = self.WinMinimizeAllUndo
        switch[GAutoItMap.WinMove] = self.WinMove
        switch[GAutoItMap.WinMoveByHandle] = self.WinMoveByHandle
        switch[GAutoItMap.WinNa] = self.WinNa
        switch[GAutoItMap.WinNaByHandle] = self.WinNaByHandle
        switch[GAutoItMap.WinNormal] = self.WinNormal
        switch[GAutoItMap.WinNormalByHandle] = self.WinNormalByHandle
        switch[GAutoItMap.WinRestore] = self.WinRestore
        switch[GAutoItMap.WinRestoreByHandle] = self.WinRestoreByHandle
        switch[GAutoItMap.WinHide] = self.WinHide
        switch[GAutoItMap.WinHideByHandle] = self.WinHideByHandle
        switch[GAutoItMap.WinShow] = self.WinShow
        switch[GAutoItMap.WinShowByHandle] = self.WinShowByHandle
        switch[GAutoItMap.WinDefault] = self.WinDefault
        switch[GAutoItMap.WinDefaultByHandle] = self.WinDefaultByHandle
        switch[GAutoItMap.WinDisable] = self.WinDisable
        switch[GAutoItMap.WinDisableByHandle] = self.WinDisableByHandle
        switch[GAutoItMap.WinKill] = self.WinKill
        switch[GAutoItMap.WinKillByHandle] = self.WinKillByHandle
        switch[GAutoItMap.Send] = self.Send
        # 鼠标操作
        # process 操作
        return switch

    def __fields_middle(self):
        fields = dict()
        fields[GAutoItFieldsMap.openApp] = self.OpenApp
        fields[GAutoItFieldsMap.winTitle] = self.WinTitle
        fields[GAutoItFieldsMap.winText] = self.WinText
        fields[GAutoItFieldsMap.winHandle] = self.WinHandle
        fields[GAutoItFieldsMap.ctlHandle] = self.CtlHandle
        fields[GAutoItFieldsMap.ctlClassNameNN] = self.CtlClassNameNN
        fields[GAutoItFieldsMap.operation] = self.Operation
        fields[GAutoItFieldsMap.sendValue] = self.SendValue
        fields[GAutoItFieldsMap.ctlSendValue] = self.CtlSendValue
        # 控件操作 可选字段
        fields[GAutoItFieldsMap.treeViewCommand] = self.TreeViewCommand
        fields[GAutoItFieldsMap.treeViewExtra1] = self.TreeViewExtra1
        fields[GAutoItFieldsMap.treeViewExtra2] = self.TreeViewExtra2
        fields[GAutoItFieldsMap.ctlMoveX] = self.CtlMoveX
        fields[GAutoItFieldsMap.ctlMoveY] = self.CtlMoveY
        fields[GAutoItFieldsMap.ctlMoveHeight] = self.CtlMoveHeight
        fields[GAutoItFieldsMap.ctlMoveWidth] = self.CtlMoveWidth
        fields[GAutoItFieldsMap.listViewCommand] = self.ListViewCommand
        fields[GAutoItFieldsMap.listViewExtra1] = self.ListViewExtra1
        fields[GAutoItFieldsMap.listViewExtra2] = self.ListViewExtra2
        fields[GAutoItFieldsMap.command] = self.Command
        fields[GAutoItFieldsMap.commandExtra] = self.Command
        fields[GAutoItFieldsMap.ctlText] = self.CtlText

        # 窗口操作 可选字段
        fields[GAutoItFieldsMap.menuItem] = self.MenuItem
        fields[GAutoItFieldsMap.winMoveHeight] = self.WinMoveHeight
        fields[GAutoItFieldsMap.winMoveWeight] = self.WinMoveWeight
        fields[GAutoItFieldsMap.winMoveX] = self.WinMoveX
        fields[GAutoItFieldsMap.winMoveY] = self.WinMoveY
        fields[GAutoItFieldsMap.winNewTitle] = self.WinNewTitle
        fields[GAutoItFieldsMap.winTrans] = self.WinTrans
        fields[GAutoItFieldsMap.raiseIfNotExist] = self.raiseIfNotExist
        return fields

    def get_field(self):
        return self.__fields_middle()

    @property
    @TypeChecking(str)
    def OpenApp(self):
        app = self.kwargs.get(GAutoItFieldsMap.openApp, '')
        return app

    @property
    @TypeChecking(str)
    def WinTitle(self) -> str:
        win_title = self.kwargs.get(GAutoItFieldsMap.winTitle, '')
        return win_title

    # @property
    # def WinClass(self):
    #     win_class = self.kwargs.get('WinClass', '')
    #     return win_class

    @property
    @TypeChecking(int)
    def WinHandle(self):
        win_handle = self.kwargs.get(GAutoItFieldsMap.winHandle, '')
        if win_handle == '':
            return None
        return win_handle

    @property
    def WinText(self):
        win_text = self.kwargs.get(GAutoItFieldsMap.winText, '')
        return win_text

    # @property
    # def CtlClass(self):
    #     ctl_class = self.kwargs.get('CtlClass', '')
    #     return ctl_class

    @property
    @TypeChecking(int)
    def CtlHandle(self):
        ctl_handle = self.kwargs.get(GAutoItFieldsMap.ctlHandle, '')
        if ctl_handle == '':
            return None
        else:
            return ctl_handle

    # @property
    # def CtlText(self):
    #     ctl_text = self.kwargs.get('CtlText', '')
    #     return ctl_text

    def raiseIfNotExist(self):
        value = self.kwargs.get(GAutoItFieldsMap.ctlHandle, True)
        if value == '':
            return value
        return value

    @property
    def CtlClassNameNN(self):
        ctl_class_name_nn = self.kwargs.get(GAutoItFieldsMap.ctlClassNameNN, '')
        if ctl_class_name_nn == '':
            return None
        return ctl_class_name_nn

    @property
    def Operation(self):
        operation = self.kwargs.get(GAutoItFieldsMap.operation, '')
        if operation != '':
            operation = operation.split(',')
            return operation
        else:
            return []

    @property
    def SendValue(self):
        value = self.kwargs.get('SendValue', '')
        return value

    @property
    def CtlSendValue(self):
        value = self.kwargs.get(GAutoItFieldsMap.ctlSendValue, '')
        return value

    @property
    def TreeViewCommand(self):
        tree_view_command = self.kwargs.get(GAutoItFieldsMap.treeViewCommand, '')
        if tree_view_command == '':
            return None
        return tree_view_command

    @property
    def TreeViewExtra1(self):
        tree_view_extra1 = self.kwargs.get(GAutoItFieldsMap.treeViewExtra1, '')
        return tree_view_extra1

    @property
    def TreeViewExtra2(self):
        tree_view_extra2 = self.kwargs.get(GAutoItFieldsMap.treeViewExtra2, '')
        return tree_view_extra2

    @property
    # @TypeChecking(int)
    def CtlMoveX(self):
        ctl_move_x = self.kwargs.get(GAutoItFieldsMap.ctlMoveX, '')
        if ctl_move_x == '':
            return None
        return ctl_move_x

    @property
    # @TypeChecking(int)
    def CtlMoveY(self):
        ctl_move_y = self.kwargs.get(GAutoItFieldsMap.ctlMoveY, '')
        if ctl_move_y == '':
            return None
        return ctl_move_y

    @property
    @TypeChecking(int)
    def CtlMoveWidth(self):
        ctl_move_width = self.kwargs.get(GAutoItFieldsMap.ctlMoveWidth, -1)
        return int(ctl_move_width)

    @property
    # @TypeChecking(int)
    def CtlMoveHeight(self):
        ctl_move_height = self.kwargs.get(GAutoItFieldsMap.ctlMoveHeight, -1)
        return int(ctl_move_height)

    @property
    def ListViewCommand(self):
        list_view_command = self.kwargs.get(GAutoItFieldsMap.listViewCommand, '')
        if list_view_command == '':
            return None
        return list_view_command

    @property
    def ListViewExtra1(self):
        list_view_extra1 = self.kwargs.get(GAutoItFieldsMap.listViewExtra1, '')
        # if list_view_extra1 == '':
        #     return None
        return list_view_extra1

    @property
    def ListViewExtra2(self):
        list_view_extra2 = self.kwargs.get(GAutoItFieldsMap.listViewExtra2, '')
        # if list_view_extra2 == '':
        #     return None
        return list_view_extra2

    @property
    def Command(self):
        command = self.kwargs.get(GAutoItFieldsMap.command, '')
        if command == '':
            return None
        return command

    @property
    def CommandExtra(self):
        command_extra = self.kwargs.get(GAutoItFieldsMap.commandExtra, '')
        return command_extra

    @property
    def CtlText(self):
        ctl_text = self.kwargs.get(GAutoItFieldsMap.ctlText, '')
        return ctl_text

    @property
    def MenuItem(self):
        menu_item = self.kwargs.get(GAutoItFieldsMap.menuItem, '')
        return menu_item

    @property
    # @TypeChecking(int)
    def WinMoveX(self):
        move_x = self.kwargs.get(GAutoItFieldsMap.winMoveX, '')
        if move_x == '':
            return None
        return move_x

    @property
    # @TypeChecking(int)
    def WinMoveY(self):
        move_y = self.kwargs.get(GAutoItFieldsMap.winMoveY, '')
        if move_y == '':
            return None
        return move_y

    @property
    # @TypeChecking(int)
    def WinMoveHeight(self):
        move_height = self.kwargs.get(GAutoItFieldsMap.winMoveHeight, -1)
        return move_height

    @property
    # @TypeChecking(int)
    def WinMoveWeight(self):
        move_weight = self.kwargs.get(GAutoItFieldsMap.winMoveWeight, -1)
        return move_weight

    @property
    def WinNewTitle(self):
        new_title = self.kwargs.get(GAutoItFieldsMap.winNewTitle, '')
        return new_title

    @property
    # @TypeChecking(int)
    def WinTrans(self):
        trans = self.kwargs.get(GAutoItFieldsMap.winTrans, 255)
        return trans

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinWait(self):
        # print(self.WinTitle)
        return auto.win_wait(title=self.WinTitle, text=self.WinText, timeout=TIMEOUT)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinWaitByHandle(self):
        return auto.win_wait_by_handle(self.WinHandle, timeout=TIMEOUT)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinClose(self):
        # # if self.WinWait():
        return auto.win_close(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinCloseByHandle(self):
        return auto.win_close_by_handle(self.WinHandle)

    @RelatedFields(SendValue=GAutoItFieldsMap.sendValue)
    def Send(self):
        return auto.send(send_text=self.SendValue)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinKill(self):
        if self.WinExists():
            return auto.win_kill(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinKillByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_kill_by_handle(self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinActivate(self):
        return auto.win_activate(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinActivateByHandle(self):
        return auto.win_activate_by_handle(self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinWaitActivate(self):
        return auto.win_wait_active(title=self.WinTitle, text=self.WinText, timeout=TIMEOUT)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinWaitActivateByHandle(self):
        return auto.win_wait_active_by_handle(self.WinHandle, timeout=TIMEOUT)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinExists(self):
        return auto.win_exists(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinExistsByHandle(self):
        return auto.win_exists_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinActive(self):
        return auto.win_active(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinActiveByHandle(self):
        return auto.win_activate_by_handle(handle=self.WinHandle)

    def WinGetCaretPos(self):
        return auto.win_get_caret_pos()

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetClassList(self):
        if self.WinExists():
            return auto.win_get_class_list(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinGetClassListByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_get_class_list_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetClientSize(self):
        if self.WinExists():
            return auto.win_get_client_size(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinGetClientSizeByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_get_client_size_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetHandle(self):
        if self.WinExists():
            return auto.win_get_handle(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetHandleAsText(self):
        if self.WinExists():
            return auto.win_get_handle_as_text(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetPos(self):
        if self.WinExists():
            return auto.win_get_pos(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinGetPosByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_get_pos_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetProcess(self):
        if self.WinExists():
            return auto.win_get_process(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinGetProcessByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_get_process_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetState(self):
        if self.WinExists():
            return auto.win_get_state(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinGetStateByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_get_state_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetText(self):
        if self.WinExists():
            return auto.win_get_text(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinGetTextByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_get_text_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinGetTitle(self):
        if self.WinExists():
            return auto.win_get_title(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinGetTitleByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_get_title_by_handle(handle=self.WinHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText,
                   MenuItem=GAutoItFieldsMap.menuItem)
    def WinMenuSelectItem(self):
        if self.WinExists():
            return auto.win_menu_select_item(title=self.WinTitle, text=self.WinText, *self.MenuItem)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, MenuItem=GAutoItFieldsMap.menuItem)
    def WinMenuSelectItemByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_menu_select_item_by_handle(handle=self.WinHandle, *self.MenuItem)

    def WinMinimizeAll(self):
        return auto.win_minimize_all()

    def WinMinimizeAllUndo(self):
        return auto.win_minimize_all_undo()

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText,
                   WinMoveX=GAutoItFieldsMap.winMoveX,
                   WinMoveY=GAutoItFieldsMap.winMoveY,
                   WinMoveHeight=GAutoItFieldsMap.winMoveHeight, WinMoveWeight=GAutoItFieldsMap.winMoveWeight)
    def WinMove(self):
        if self.WinExists():
            return auto.win_move(title=self.WinTitle, text=self.WinText, x=self.WinMoveX, y=self.WinMoveY,
                                 height=self.WinMoveHeight, weight=self.WinMoveWeight)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, WinMoveX=GAutoItFieldsMap.winMoveX,
                   WinMoveY=GAutoItFieldsMap.winMoveY,
                   WinMoveHeight=GAutoItFieldsMap.winMoveHeight,
                   WinMoveWeight=GAutoItFieldsMap.winMoveWeight)
    def WinMoveByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_move_by_handle(handle=self.WinHandle, x=self.WinMoveX, y=self.WinMoveY,
                                           height=self.WinMoveHeight, weight=self.WinMoveWeight)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinTopMost(self):
        if self.WinExists():
            return auto.win_set_on_top(title=self.WinTitle, text=self.WinText, flag=1)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinUnTop(self):
        if self.WinExists():
            return auto.win_set_on_top(title=self.WinTitle, text=self.WinText, flag=0)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinTopMostByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_on_top_by_handle(handle=self.WinHandle, flag=1)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinUnTopByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_on_top_by_handle(handle=self.WinHandle, flag=0)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinHide(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_HIDE)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinHideByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_HIDE)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinShow(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_SHOW)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinShowByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_SHOW)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinMin(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_MINIMIZE)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinMinByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_MINIMIZE)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinMax(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_MAXIMIZE)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinMaxByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_MAXIMIZE)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinRestore(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_RESTORE)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinRestoreByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_RESTORE)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinNormal(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_SHOWNORMAL)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinNormalByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_SHOWNORMAL)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinDisable(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_SHOWNOACTIVATE)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinDisableByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_SHOWNOACTIVATE)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinMinDisable(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_SHOWMINNOACTIVE)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinMinDisableByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_SHOWMINNOACTIVE)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinNa(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_SHOWNA)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinNaByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_SHOWNA)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinDefault(self):
        if self.WinExists():
            return auto.win_set_state(title=self.WinTitle, text=self.WinText, flag=auto.properties.SW_SHOWDEFAULT)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinDefaultByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_state_by_handle(handle=self.WinHandle, flag=auto.properties.SW_SHOWDEFAULT)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText,
                   WinNewTitle=GAutoItFieldsMap.winNewTitle)
    def WinSetTile(self):
        if self.WinExists():
            return auto.win_set_title(title=self.WinTitle, text=self.WinText, new_title=self.WinNewTitle)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, WinNewTitle=GAutoItFieldsMap.winNewTitle)
    def WinSetTitleByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_title_by_handle(handle=self.WinHandle, new_title=self.WinNewTitle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText,
                   WinTrans=GAutoItFieldsMap.winTrans)
    def WinSetTrans(self):
        if self.WinExists():
            return auto.win_set_trans(title=self.WinTitle, text=self.WinText, trans=self.WinTrans)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, WinTrans=GAutoItFieldsMap.winTrans)
    def WinSetTransByHandle(self):
        if self.WinExistsByHandle():
            return auto.win_set_trans_by_handle(handle=self.WinHandle, trans=self.WinTrans)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinWaitClose(self):
        return auto.win_wait_close(title=self.WinTitle, text=self.WinText, timeout=TIMEOUT)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinWaitCloseByHandle(self):
        return auto.win_wait_close_by_handle(handle=self.WinHandle, timeout=TIMEOUT)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def WinWaitNotActive(self):
        return auto.win_wait_not_active(title=self.WinTitle, text=self.WinText, timeout=TIMEOUT)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def WinWaitNotActiveByHandle(self):
        return auto.win_wait_not_active_by_handle(handle=self.WinHandle, timeout=TIMEOUT)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlLeftClick(self):
        # print(self.WinTitle)
        if self.WinExists():
            return auto.control_click(title=self.WinTitle, text=self.WinText, control=self.CtlClassNameNN,
                                      button='left')

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlLeftClickByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_click_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle, button='left')

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlDoubleclick(self):
        if self.WinExists():
            return auto.control_click(title=self.WinTitle, text=self.WinText, control=self.CtlClassNameNN,
                                      button='left', click='2')

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlDoubleClickByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_click_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle, button='left', click='2')

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlRightClick(self):
        if self.WinExists():
            return auto.control_click(title=self.WinTitle, text=self.WinText, contrl=self.CtlClassNameNN,
                                      button='right')

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlRightClickByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_click_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle, button='right')

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlRightDoubleClick(self):
        if self.WinExists():
            return auto.control_click(title=self.WinTitle, text=self.WinText, contrl=self.CtlClassNameNN,
                                      button='right', click='2')

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlRightDoubleClickByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_click_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle, button='right', click='2')

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   CtlText=GAutoItFieldsMap.ctlText, SendValue=GAutoItFieldsMap.sendValue)
    def CtlSend(self):
        if self.WinExists():
            return auto.control_send(title=self.WinTitle, text=self.WinText, control=self.CtlClassNameNN,
                                     send_text=self.CtlSendValue, mode=0)
        # else:
        #     return None

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle,
                   SendValue=GAutoItFieldsMap.sendValue)
    def CtlSendByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_send_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle, send_text=self.CtlSendValue,
                                               mode=0)
        # else:
        #     return None

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   CtlText=GAutoItFieldsMap.ctlText, WinText=GAutoItFieldsMap.winText)
    def CtlSetText(self):
        if self.WinExists():
            return auto.control_set_text(title=self.WinTitle, text=self.WinText, control=self.CtlClassNameNN,
                                         control_text=self.CtlText)
        # else:
        #     return None

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle,
                   CtlText=GAutoItFieldsMap.ctlText)
    def CtlSetTextByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_set_text_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle,
                                                   control_text=self.CtlText)
        # else:
        #     return None

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   Command=GAutoItFieldsMap.command, CommandExtra=GAutoItFieldsMap.commandExtra,
                   WinText=GAutoItFieldsMap.winText)
    def CtlCommand(self):
        if self.WinExists():
            return auto.control_command(title=self.WinTitle, text=self.WinText, control=self.CtlClassNameNN,
                                        command=self.Command, extra=self.CommandExtra)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle,
                   Command=GAutoItFieldsMap.command,
                   CommandExtra=GAutoItFieldsMap.commandExtra)
    def CtlCommandByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_command_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle, command=self.Command,
                                                  extra=self.CommandExtra)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText,
                   CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   ListViewCommand=GAutoItFieldsMap.listViewCommand,
                   ListViewExtra1=GAutoItFieldsMap.listViewExtra1, ListViewExtra2=GAutoItFieldsMap.listViewExtra2)
    def CtlListView(self):
        if self.WinExists():
            return auto.control_list_view(title=self.WinTitle, text=self.WinText, command=self.ListViewCommand,
                                          control=self.CtlClassNameNN,
                                          extra1=self.ListViewExtra1, extra2=self.ListViewExtra2)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle,
                   ListViewCommand=GAutoItFieldsMap.listViewCommand,
                   ListViewExtra1=GAutoItFieldsMap.listViewExtra1, ListViewExtra2=GAutoItFieldsMap.listViewExtra2)
    def CtlListViewByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_list_view_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle,
                                                    command=self.ListViewCommand,
                                                    extra1=self.ListViewExtra1, extra2=self.ListViewExtra2)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlDisable(self):
        if self.WinExists():
            return auto.control_disable(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlDisableByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_disable_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlEnable(self):
        if self.WinExists():
            return auto.control_enable(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlEnableByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_enable_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlFocus(self):
        if self.WinExists():
            return auto.control_focus(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlFocusByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_focus_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText)
    def CtlGetFocus(self):
        if self.WinExists():
            return auto.control_get_focus(title=self.WinTitle, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle)
    def CtlGetFocusByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_get_focus_by_handle(hwnd=self.WinHandle)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN)
    def CtlGetHandle(self):
        if self.WinExistsByHandle():
            return auto.control_get_handle(hwnd=self.WinHandle, control=self.CtlClassNameNN)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlGetHandleAsText(self):
        if self.WinExists():
            return auto.control_get_handle_as_text(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlGetPos(self):
        if self.WinExists():
            return auto.control_get_pos(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlGetPosByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_get_pos_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlGetText(self):
        if self.WinExists():
            return auto.control_get_text(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlGetTextByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_get_text_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlHide(self):
        if self.WinExists():
            return auto.control_hide(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlHideByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_hide_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, WinText=GAutoItFieldsMap.winText,
                   CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN, CtlMoveX=GAutoItFieldsMap.ctlMoveX,
                   CtlMoveY=GAutoItFieldsMap.ctlMoveY, CtlMoveWidth=GAutoItFieldsMap.ctlMoveWidth,
                   CtlMoveHeight=GAutoItFieldsMap.ctlMoveHeight)
    def CtlMove(self):
        if self.WinExists():
            return auto.control_move(title=self.WinTitle, text=self.WinText, control=self.CtlClassNameNN,
                                     x=self.CtlMoveX,
                                     y=self.CtlMoveY, width=self.CtlMoveWidth, height=self.CtlMoveHeight)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle,
                   CtlMoveX=GAutoItFieldsMap.ctlMoveX,
                   CtlMoveY=GAutoItFieldsMap.ctlMoveY,
                   CtlMoveWidth=GAutoItFieldsMap.ctlMoveWidth, CtlMoveHeight=GAutoItFieldsMap.ctlMoveHeight)
    def CtlMoveByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_move_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle, x=self.CtlMoveX,
                                               y=self.CtlMoveY,
                                               width=self.CtlMoveWidth, height=self.CtlMoveHeight)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   WinText=GAutoItFieldsMap.winText)
    def CtlShow(self):
        if self.WinExists():
            return auto.control_show(title=self.WinTitle, control=self.CtlClassNameNN, text=self.WinText)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle)
    def CtlShowByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_show_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle)

    @RelatedFields(WinTitle=GAutoItFieldsMap.winTitle, CtlClassNameNN=GAutoItFieldsMap.ctlClassNameNN,
                   TreeViewCommand=GAutoItFieldsMap.treeViewCommand,
                   WinText=GAutoItFieldsMap.winText, TreeViewExtra1=GAutoItFieldsMap.treeViewExtra1,
                   TreeViewExtra2=GAutoItFieldsMap.treeViewExtra2)
    def CtlTreeView(self):
        if self.WinExists():
            return auto.control_tree_view(title=self.WinTitle, control=self.CtlClassNameNN,
                                          command=self.TreeViewCommand,
                                          text=self.WinText, extras1=self.TreeViewExtra1, extras2=self.TreeViewExtra2)

    @RelatedFields(WinHandle=GAutoItFieldsMap.winHandle, CtlHandle=GAutoItFieldsMap.ctlHandle,
                   TreeViewCommand=GAutoItFieldsMap.treeViewCommand,
                   TreeViewExtra1=GAutoItFieldsMap.treeViewExtra1, TreeViewExtra2=GAutoItFieldsMap.treeViewExtra2)
    def CtlTreeViewByHandle(self):
        if self.WinExistsByHandle():
            return auto.control_tree_view_by_handle(hwnd=self.WinHandle, h_ctrl=self.CtlHandle,
                                                    command=self.TreeViewCommand,
                                                    extra1=self.TreeViewExtra1, extra2=self.TreeViewExtra2)


def execute(operations: (list, dict)):
    if isinstance(operations, list):
        for operation in operations:
            g_control_obj = GAutoIt(operation_detail=operation)
            g_control_obj.start()
    else:
        g_control_obj = GAutoIt(operation_detail=operations)
        g_control_obj.start()


if __name__ == '__main__':
    demo = {
        "SerialNum": "",
        "IsUIA": "False",
        "Title": "",
        "Control": "",
        "OpenApp": "",
        "SearchFromControl": "",
        "SearchDepth": '',
        "SearchInterval": "0.5",
        "Name": "name",
        "ClassName": "",
        "SubName": "",
        "AutomationId": "",
        "FoundIndex": '',
        "ControlType": "",
        "Condiment": "",
        "ChildrenIndex": "",
        "Operation": "HotKey",
        "Value": "",
        "CtlHandle": 1
    }
    g = GAutoIt(operation_detail=demo)
    print(g.CtlTreeViewByHandle())
