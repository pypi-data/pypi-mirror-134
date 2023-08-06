import autoit
import uiautomation
import subprocess
import os
# from main import GAutoit, GUIA
import time
# time.sleep(3)
# autoit.win
from selenium import webdriver

# if autoit.win_exists("[CLASS:Notepad]"):
#     print(1)
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=0)  # hide
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=5)  # show
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=3)  # max
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=6)  # min
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=9)  # restore
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=1)  # normal
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=8)  # na
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=2)  # min
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=7)  # min no active
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=4)  # no activate
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=10)  # default
    # autoit.win_set_state(title="[CLASS:Notepad]", flag=)  # default
    # print(autoit.win_get_state(title="[CLASS:Notepad]"))
    # autoit.control_send_by_handle(hwnd=0x00000000000F0486, h_ctrl=0x0000000000110822, send_text='hello,python')
    # autoit.win_move_by_handle(handle=0x00000000000F0486, x=123, y=123)

# wy_dict = uiautomation.PaneControl(searchDepth=1, Name='网易有道词典')
# if wy_dict.Exists(maxSearchSeconds=30):
    # print(wy_dict)
    # print(wy_dict.GetWindowText())
    # print(wy_dict.GetPixelColor(x=100, y=100))
    # print(wy_dict.ToBitmap(x=100, y=100))
    # edit = uiautomation.EditControl(searchDepth=2, ClassName='Edit')
    # edit.GetLegacyIAccessiblePattern().SetValue('20211201')
    # print(edit)
    # wy_dict.SendKey(key=1)
    # print(wy_dict.Hide())
    # wy_dict.CaptureToImage(savePath=r'D:\BCZX\RPA\self\GExecutor\main\test.jpg')
    # wy_dict.SetTopmost(isTopmost=False)
    # print(wy_dict.MoveCursorToInnerPos())
    # state = wy_dict.Disappears(maxSearchSeconds=30, searchIntervalSeconds=0.1)
    # state = wy_dict.Refind(maxSearchSeconds=30)
    # print(state)
    # print(wy_dict.MoveCursorToMyCenter())

# subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')

# ################################ 邮政银行流水下载 ###################################
# browser = webdriver.Chrome(executable_path=r'D:\SoftwareFiles\chromedriver\97.0.4692.71\chromedriver.exe')
# browser.get('https://corpebankq.psbc.com/#/login?tab=customLogin')
# postal = uiautomation.PaneControl(Name='中国邮政储蓄银行企业网银 - Google Chrome', searchDepth=1)
# if postal.Exists(maxSearchSeconds=5):
#     postal.SetActive()
#     postal.ShowWindow(cmdShow=3)
# pwd = uiautomation.EditControl(searchDepth=18, AutomationId='customLogin')
# print(pwd)
# print(pwd.GetTextPattern())
# account = uiautomation.TextControl(Name='账户管理', searchDepth=15)
# print(account)
# 选择日期
# search_date = uiautomation.TextControl(Name='查询日期：', searchDepth=15)
# search_date = uiautomation.TextControl(Name='查询日期：', searchDepth=3)
# print(search_date)
# if search_date.Exists(maxSearchSeconds=5):
#     search_date_parents = search_date.GetParentControl()
#     sister = search_date_parents.GetNextSiblingControl()
#     start_sister_children = sister.GetChildren()[0].GetChildren()[0].GetChildren()[0].GetChildren()[0]
#     print(start_sister_children)
#     start_sister_children.SetFocus()
#     start_sister_children.SendKeys('{Ctrl}a{Delete}')
#     start_sister_children.SendKeys('2021-12-01')
#     end_sister_children = sister.GetChildren()[2].GetChildren()[0].GetChildren()[0].GetChildren()[0]
#     print(end_sister_children)
#     end_sister_children.SendKeys('{Ctrl}a{Delete}')
#     end_sister_children.SendKeys('2021-12-31')
# download_all = uiautomation.TextControl(Name='下载全部', searchDepth=15)
# print(download_all)
# download_all.Click()
# time.sleep(3)
# excel = uiautomation.TextControl(Name='EXCEL', searchDepth=17)
# excel.SetFocus()
# excel.Click()
# download = uiautomation.ButtonControl(Name='按交易日期正序下载', searchDepth=14)
# download.Click()

# ################################ 工商电子银行流水下载 ###################################


def GGetSameLevelControlByOffset(name, control, offset):
    children = control.GetParentControl().GetChildren()
    for i, v in enumerate(children):
        if v.Name == name:
            return children[i + offset]


icbc_root = uiautomation.WindowControl(SubName='中国工商银行企业网上银行', searchDepth=1)
if icbc_root.Exists(maxSearchSeconds=5):
    icbc_root.SetActive()
    icbc_root.ShowWindow(cmdShow=3)
flag = uiautomation.TextControl(Name='　1.日　期：　从', searchDepth=17)
if flag.Exists(maxSearchSeconds=5):
    start_year_ = GGetSameLevelControlByOffset(name='　1.日　期：　从', control=flag, offset=1)
    print(start_year_)
    start_month_ = GGetSameLevelControlByOffset(name='　1.日　期：　从', control=flag, offset=3)
    print(start_month_)
    start_day_ = GGetSameLevelControlByOffset(name='　1.日　期：　从', control=flag, offset=5)
    print(start_day_)
    end_year_ = GGetSameLevelControlByOffset(name='　1.日　期：　从', control=flag, offset=7)
    print(end_year_)
    end_month_ = GGetSameLevelControlByOffset(name='　1.日　期：　从', control=flag, offset=9)
    print(end_month_)
    end_day_ = GGetSameLevelControlByOffset(name='　1.日　期：　从', control=flag, offset=11)
    print(end_day_)
    end_day_.Click()
    a = uiautomation.ListItemControl(Name='30', searchDepth=2)
    parent = a.GetParentControl()
    parent.SetFocus()
    parent.SendKeys('{DOWN 30}')
    # parent.WheelDown(wheelTimes=30)
    # a.SetFocus()
    # a.WheelDown(x=1,y=1)

    # end_day_.WheelDown()


if __name__ == '__main__':
    a = ''
    # # a = a.split(',')
    # if a:
    #     print(1)
    # test()




