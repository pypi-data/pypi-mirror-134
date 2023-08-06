import time
demo = {
    "serialNum": "",
    "isUIA": "False",
    "title": "",
    "control": "",
    "openApp": "",
    "searchFromControl": "",
    "searchDepth": '',
    "searchInterval": "0.5",
    "name": "name",
    "className": "",
    "subName": "",
    "automationId": "",
    "foundIndex": '',
    "controlType": "",
    "condiment": "",
    "childrenIndex": "",
    "operation": "HotKey",
    "value": ""
}
# ******************************************
# UIA 打开计算器，键入7*7
# ******************************************
calculator = [
    {
        "openApp": "calc.exe",
        "searchFromControl": "",
        "searchDepth": '1',
        "searchInterval": "0.5",
        "name": "计算器",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '1',
        "controlType": "WindowControl",
        "operation": "SetFocus",
        "value": ""
    },
    {
        "searchDepth": '4',
        "searchInterval": "0.5",
        "name": "标准运算符",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '1',
        "controlType": "GroupControl",
        "operation": "SetFocus",
        "value": ""
    },
    {
        "serialNum": "3",
        "searchFromControl": "",
        "searchDepth": '4',
        "searchInterval": "0.5",
        "name": "数字键盘",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '1',
        "controlType": "GroupControl",
        "operation": "SetFocus",
        "value": ""
    },
    {
        "serialNum": "4",
        "searchFromControl": "3",
        "searchDepth": '',
        "searchInterval": "",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '7',
        "operation": "Click",
        "value": ""
    },
    {
        "serialNum": "5",
        "searchFromControl": "2",
        "searchDepth": '',
        "searchInterval": "",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '1',
        "operation": 'Click',
        "value": ""
    },
    {
        "serialNum": "6",
        "searchFromControl": "3",
        "searchDepth": '',
        "searchInterval": "0.5",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '7',
        "operation": "Click",
        "value": ""
    },
    {
        "serialNum": "7",
        "searchFromControl": "2",
        "searchDepth": '',
        "searchInterval": "",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '4',
        "operation": "Click",
        "value": ""
    },

]
calculator1 = [
    {
        "openApp": "calc.exe",
        "searchFromControl": "",
        "searchDepth": '1',
        "searchInterval": "0.5",
        "name": "计算器",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '1',
        "controlType": "WindowControl",
        "operation": "SetFocus",
        "value": ""
    },
    {
        "searchDepth": '4',
        "searchInterval": "0.5",
        "name": "标准运算符",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '1',
        "controlType": "GroupControl",
        "operation": "SetFocus",
        "value": ""
    },
    {
        "serialNum": "3",
        "searchFromControl": "",
        "searchDepth": '4',
        "searchInterval": "0.5",
        "name": "数字键盘",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '1',
        "controlType": "GroupControl",
        "operation": "SetFocus",
        "value": ""
    },
    {
        "serialNum": "4",
        "searchFromControl":
            {
                "searchDepth": '4',
                "searchInterval": "0.5",
                "name": "数字键盘",
                "foundIndex": '1',
                "controlType": "GroupControl",
            },
        "searchDepth": '',
        "searchInterval": "",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '7',
        "operation": "Click",
        "value": ""
    },
    {
        "serialNum": "5",
        "searchFromControl": "2",
        "searchDepth": '',
        "searchInterval": "",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '1',
        "operation": 'Click',
        "value": ""
    },
    {
        "serialNum": "6",
        "searchFromControl": "3",
        "searchDepth": '',
        "searchInterval": "0.5",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '7',
        "operation": "Click",
        "value": ""
    },
    {
        "serialNum": "7",
        "searchFromControl": "2",
        "searchDepth": '',
        "searchInterval": "",
        "name": "",
        "className": "",
        "subName": "",
        "automationId": "",
        "foundIndex": '',
        "controlType": "",
        "condiment": "GetChildren",
        "childrenIndex": '4',
        "operation": "Click",
        "value": ""
    },

]
# ******************************************
# AutoIt 打开笔记本，写入hello world，并保存text.txt
# ******************************************
autoit_notepad = [
    {
        "serialNum": 1,
        "isUIA": "False",
        "openApp": "notepad.exe",
        "winTitle": "[CLASS:Notepad]",
        "winClass": "Notepad",
        "winHandle": 0x0000000000060A86,
        "ctlClassNameNN": "Edit1",
        "ctlClass": "Edit",
        "ctlHandle": 0x0000000000050A88,
        "operation": "CtlSend,WinClose",
        "ctlSendValue": "hello world"
    },
    {
        "serialNum": 2,
        "isUIA": "False",
        "winTitle": "记事本",
        "winClass": "#32770",
        "ctlClassNameNN": "Button1",
        "ctlClass": "Button",
        "operation": "CtlLeftClick,"
    },
    {
        "serialNum": 3,
        "isUIA": "False",
        "winTitle": "另存为",
        "winClass": "#32770",
        "winHandle": 0x00130640,
        "ctlClassNameNN": "Edit1",
        "ctlHandle": 0x00240B28,
        "operation": "Send",
        "sendValue": "{DEL}"
    },
    {
        "serialNum": 4,
        "isUIA": "False",
        "winTitle": "另存为",
        "winClass": "#32770",
        "winHandle": 0x00130640,
        "ctlClassNameNN": "Edit1",
        "ctlHandle": 0x00240B28,
        "operation": "CtlSend",
        "ctlSendValue": "text.txt"
    },
    {
        "serialNum": 5,
        "isUIA": "False",
        "winTitle": "另存为",
        "winClass": "#32770",
        "ctlClassNameNN": "Button2",
        "operation": "CtlLeftClick",
    },

]
# ******************************************
# UIA:打开有道词典输入 hello， 并将查询结果截图保存
# ******************************************
youdao_dict = [
    {
        'serialNum': 1,
        'openApp': r'D:\SoftwareFiles\Dict\YouDaoDict.exe',
        'searchDepth': 1,
        'name': '网易有道词典',
        'controlType': 'PaneControl',
        'operation': 'Click'
    },
    {
        'serialNum': 2,
        'searchFromControl': 1,
        'controlType': 'EditControl',
        'searchDepth': 2,
        'className': 'Edit',
        'operation': 'SendKeys',
        'value': 'hello'
    },
    {
        'serialNum': 3,
        'searchDepth': 1,
        'name': '网易有道词典',
        'controlType': 'PaneControl',
        'operation': 'SendKeys',
        'value': '{Enter}'
    },
    {
        'serialNum': 4,
        'searchDepth': 5,
        'name': '有道词典',
        'controlType': 'DocumentControl',
        'operation': 'CaptureToImage',
        'savePath': r'C:\Users\刘嘉怡\Desktop\youdao.jpg'
    },
]
youdao_dict1 = [
    {
        'serialNum': 1,
        'openApp': r'D:\SoftwareFiles\Dict\YouDaoDict.exe',
        'searchDepth': 1,
        'name': '网易有道词典',
        'controlType': 'PaneControl',
        'operation': 'Click'
    },
    {
        'searchFromControl':
            {
                'searchDepth': 1,
                'name': '网易有道词典',
                'controlType': 'PaneControl',
            },
        'controlType': 'EditControl',
        'searchDepth': 2,
        'className': 'Edit',
        'operation': 'SendKeys',
        'value': 'hello'
    },
    {
        'serialNum': 3,
        'searchDepth': 1,
        'name': '网易有道词典',
        'controlType': 'PaneControl',
        'operation': 'SendKeys',
        'value': '{Enter}'
    },
    {
        'serialNum': 4,
        'searchDepth': 5,
        'name': '有道词典',
        'controlType': 'DocumentControl',
        'operation': 'CaptureToImage',
        'savePath': r'C:\Users\刘嘉怡\Desktop\youdao.jpg'
    },
]
# ******************************************
# UIA:excel 操作
# ******************************************
excel = [
    {

    }
]

# ******************************************
# UIA:word 操作 输入文章 并插入图片，并保存到桌面
# ******************************************
word = [
    {
        'openApp': r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE',
        'searchDepth': 1,
        'controlType': 'WindowControl',
        'subName': 'Word',
        'className': 'OpusApp',
        'operation': 'Click,ShowWindow',
        'cmdShow': 3
    },  # 打开word, 并获取到头层控件, 并最大化窗口
    {
        'searchDepth': 5,
        'name': "开始",
        'controlType': 'GroupControl',
        'operation': 'SetFocus'
    },  # 获取 开始 层
    {
        'searchFromControl': {
            'searchDepth': 5,
            'name': "开始",
            'controlType': 'GroupControl',
        },
        'name': "空白文档",
        'searchDepth': 9,
        'controlType': 'ListItemControl',
        'operation': 'Click'
    },  # 空白文档
    # {
    #     'searchDepth': 8,
    #     'name': '下层功能区',
    #     'controlType': 'PaneControl',
    #     'condiment': 'GetChildren',
    #     'childrenIndex': 0
    # },  # 下层功能区
    # {
    #     'name': '样式',
    #     'searchDepth': 14,
    #     'controlType': 'DataGridControl',
    # },  # 样式组件，
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "死之默想"
    },  # 输入标题
    {
        'name': '标题 1',
        'searchDepth': 15,
        'controlType': 'ListItemControl',
        'operation': 'Click'
    },
    {
        'name': '居中',
        'searchDepth': 11,
        'controlType': 'ButtonControl',
        'operation': 'Click'
    },
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "{Enter}"
    },  # 回车
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "  4世纪时希腊厌世诗人巴拉达思作有一首小诗道：“你太饶舌了，人啊，不久将睡在地下；住口吧。你生存时且思索那死。”"
    },  # 输入文本
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "{Enter}"
    },  # 回车
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "  这是很有意思的话。关于死的问题，我无事时也曾默想过（但不坐在树下，大抵是在车上），可是想不出什么来，这或者因为我是个“乐天的诗人”的缘故吧。但其实我何尝一定崇拜死，有如曹慕管君，不过我不很能够感到死之神秘，所以不觉得有思索十日十夜之必要，于形而上的方面也就不能有所饶舌了。"
    },  # 输入文本
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "{Enter}"
    },  # 回车
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "  窥察世人怕死的原因，自有种种不同，“以愚观之”可以定为三项，其一是怕死时的苦痛，其二是合不得人世的快乐，其三是顾虑家族。苦痛比死还可怕，这是实在的事情。十多年前有一个远房的伯母，十分困苦，在十二月底想投河寻死（我们乡间的河是经冬不冻的），但是投了下去，她随即走了上来，说是因为水太冷了。有些人要笑她痴也未可知，但这却是真实的人情。倘若有人能够切实保证，诚如某生物学家所说，被猛兽咬死痒苏苏地很是愉快，我想一定有许多人裹粮入山去投身饲饿虎了。可惜这一层不能担保，有些对于别项已无留恋的人因此也就不得不稍为踌躇了。"
    },  # 输入文本
    {
        'searchDepth': 6,
        'name': '页面 1 内容',
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': "{Enter}"
    },  # 回车
    {
        'searchDepth': 9,
        'name': '插入',
        'controlType': 'TabItemControl',
        'operation': 'Click',

    },
    {
        'searchDepth': 11,
        'name': '图片',
        'controlType': 'MenuItemControl',
        'operation': 'Click',
    },
    {
        'searchDepth': 14,
        'name': '此设备...',
        'controlType': 'MenuItemControl',
        'operation': 'Click',
    },
    {
        'searchDepth': 5,
        'name': '文件名(N):',
        'controlType': 'EditControl',
        'operation': 'Click,SendKeys',
        'value': r'C:\Users\刘嘉怡\Pictures\Saved Pictures\ABT33410F98F2E5CCB902A740C7C2A7111F7B34BF0E845D291EFF6E6915E11262C5.jpg'
    },
    {
        'searchDepth': 3,
        'name': '插入(S)',
        'controlType': 'SplitButtonControl',
        'operation': 'Click',
    },
    #  保存
    # {
    #     'searchDepth': 8,
    #     'name': '“文件”选项卡',
    #     'controlType': 'ButtonControl',
    #     'operation': 'Click',
    # },
    # {
    #     'searchDepth': 6,
    #     'name': '另存为',
    #     'controlType': 'ListItemControl',
    #     'operation': 'Click',
    # },
    # {
    #     'searchDepth': 10,
    #     'name': '这台电脑',
    #     'controlType': 'TabItemControl',
    #     'operation': 'Click',
    # },
    {
        'isUIA': False,
        'winTitle': '[class:OpusApp]',
        'operation': 'WinClose'
    },
    {
        'name': '打开',
        'searchDepth': 7,
        'controlType': 'ButtonControl',
        'operation': 'Click'
    },
    {
        'name': '其他位置',
        'controlType': 'ListItemControl',
        'searchDepth': 9,
        'operation': 'Click',
    },
    {
        'name': '文件名:',
        'controlType': 'EditControl',
        'searchDepth': 8,
        'operation': 'SendKeys',
        'value': '{Ctrl}a{Delete}'
    },
    {
        'name': '文件名:',
        'controlType': 'EditControl',
        'searchDepth': 8,
        'operation': 'SendKeys',
        'value': r'C:\Users\刘嘉怡\Desktop\死之默想.docx'
    },
    {
        'name': '保存(S)',
        'controlType': 'ButtonControl',
        'searchDepth': 3,
        'operation': 'Click',
    }
]

# ******************************************
# UIA:邮政银行 下载流水
# ******************************************
pwd = '8she2229'
user_name = '10000013045714'
user_id = '0002'
postal_login = [
    {
        'openApp': r'C:\Program Files\Google\Chrome\Application\Chrome.exe',
        'searchFromControl':
            {
                'subName': '新标签页',
                'searchDepth': 1,
                'controlType': 'PaneControl',
                'operation': 'SetActive,ShowWindow',
            },
        'name': '地址和搜索栏',
        'searchDepth': 8,
        'controlType': 'EditControl',
        'operation': 'Click,SendKeys,HotKey',
        'value': 'https://corpebankq.psbc.com/#/login?tab=userLogin',
        'hotKey': '{ENTER}'
    },
    {
        'subName': '中国邮政储蓄银行企业网银',
        'searchDepth': 1,
        'controlType': 'PaneControl',
        'operation': 'SetActive,ShowWindow',
        'cmdShow': 3
    },
    {
        'name': '客户编号',
        'searchDepth': 18,
        'controlType': 'TextControl',
        'operation': 'Click'
    },
    {
        'name': '客户编号',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetPreviousSiblingControl',
        'operation': 'Click,SendKeys',
        'value': user_name
    },
    {
        'name': '操作员ID',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetPreviousSiblingControl',
        'operation': 'Click,SendKeys',
        'value': user_id
    },
    {
        # 'name': '登录密码',
        'searchDepth': 18,
        'automationId': 'customLogin',
        'controlType': 'EditControl',
        'operation': 'Click,SendKeys',
        'value': pwd
    }
]
postal_login_btn = [
    {
        'name': '登录',
        'searchDepth': 14,
        'controlType': 'ButtonControl',
        'operation': 'Click',
    }
]
postal_choose_date = [
    # 选择日期
    {
        'name': '查询日期：',
        'searchDepth': 15,
        'controlType': 'TextControl',
        'condiment': 'GetParentControl',
    },
    {
        'searchFromControl':
            {
                'name': '查询日期：',
                'searchDepth': 15,
                'controlType': 'TextControl',
                'condiment': 'GetParentControl',
            },
        'condiment': 'GetNextSiblingControl',
    },
    # {
    #     'searchFromControl':
    #         {
    #             'searchFromControl':
    #                 {
    #                     'name': '查询日期：',
    #                     'searchDepth': 15,
    #                     'controlType': 'TextControl',
    #                     'condiment': 'GetParentControl',
    #                 },
    #             'condiment': 'GetNextSiblingControl',
    #         },
    #     'condiment': 'GetChildren',
    #     'childrenIndex': 0
    # },
    # {
    #     'searchFromControl':
    #         {
    #             'searchFromControl':
    #                 {
    #                     'searchFromControl':
    #                         {
    #                             'name': '查询日期：',
    #                             'searchDepth': 15,
    #                             'controlType': 'TextControl',
    #                             'condiment': 'GetParentControl',
    #                         },
    #                     'condiment': 'GetNextSiblingControl',
    #                 },
    #             'condiment': 'GetChildren',
    #             'childrenIndex': 0
    #         },
    #     'condiment': 'GetChildren',
    #     'childrenIndex': 0
    # },
    # {
    #     'searchFromControl':
    #         {
    #             'searchFromControl':
    #                 {
    #                     'searchFromControl':
    #                         {
    #                             'searchFromControl':
    #                                 {
    #                                     'name': '查询日期：',
    #                                     'searchDepth': 15,
    #                                     'controlType': 'TextControl',
    #                                     'condiment': 'GetParentControl',
    #                                 },
    #                             'condiment': 'GetNextSiblingControl',
    #                         },
    #                     'condiment': 'GetChildren',
    #                     'childrenIndex': 0
    #                 },
    #             'condiment': 'GetChildren',
    #             'childrenIndex': 0
    #         },
    #     'condiment': 'GetChildren',
    #     'childrenIndex': 0
    # },
    {
        'searchFromControl':
            {
                'searchFromControl':
                    {
                        'searchFromControl':
                            {
                                'searchFromControl':
                                    {
                                        'searchFromControl':
                                            {
                                                'name': '查询日期：',
                                                'searchDepth': 15,
                                                'controlType': 'TextControl',
                                                'condiment': 'GetParentControl',
                                            },
                                        'condiment': 'GetNextSiblingControl',
                                    },
                                'condiment': 'GetChildren',
                                'childrenIndex': 0
                            },
                        'condiment': 'GetChildren',
                        'childrenIndex': 0
                    },
                'condiment': 'GetChildren',
                'childrenIndex': 0
            },
        'condiment': 'GetChildren',
        'childrenIndex': 0,
        'operation': 'SetFocus,HotKey,SendKeys',
        'hotKey': '{Ctrl}a{Delete}',
        'value': '2021-12-01'
    },
    {
        'searchFromControl':
            {
                'searchFromControl':
                    {
                        'searchFromControl':
                            {
                                'searchFromControl':
                                    {
                                        'searchFromControl':
                                            {
                                                'name': '查询日期：',
                                                'searchDepth': 15,
                                                'controlType': 'TextControl',
                                                'condiment': 'GetParentControl',
                                            },
                                        'condiment': 'GetNextSiblingControl',
                                    },
                                'condiment': 'GetChildren',
                                'childrenIndex': 2
                            },
                        'condiment': 'GetChildren',
                        'childrenIndex': 0
                    },
                'condiment': 'GetChildren',
                'childrenIndex': 0
            },
        'condiment': 'GetChildren',
        'childrenIndex': 0,
        'operation': 'SetFocus,HotKey,SendKeys',
        'hotKey': '{Ctrl}a{Delete}',
        'value': '2021-12-31'
    }
]
postal_search = [
    # {
    #     'isUIA': False,
    #     'title': '中国邮政储蓄银行企业网银',
    #     'operation': 'WinShow,WinMax'
    # },
    {
        'subName': '中国邮政储蓄银行企业网银',
        'searchDepth': 1,
        'controlType': 'PaneControl',
        'operation': 'SetActive,ShowWindow',
        'cmdShow': 3
    },
    {
        'name': '中国邮政储蓄银行企业网银',
        'searchDepth': 2,
        'controlType': 'DocumentControl',
    },
    {
        'name': '账户管理',
        'searchDepth': 15,
        'controlType': 'TextControl',
        'operation': 'Click'
    },
    {
        'name': '明细查询',
        'controlType': 'MenuItemControl',
        'searchDepth': 11,
        'operation': 'Click'
    },
    # 选择日期
    {
        'name': '查询日期：',
        'searchDepth': 15,
        'controlType': 'TextControl',
        'condiment': 'GetParentControl,GetNextSiblingControl,GetChildren:0,GetChildren:0,GetChildren:0,GetChildren:0',
        'operation': 'SetFocus,HotKey,SendKeys',
        'hotKey': '{Ctrl}a{Delete}',
        'value': '2021-12-01'
    },
    {
        'name': '查询日期：',
        'searchDepth': 15,
        'controlType': 'TextControl',
        'condiment': 'GetParentControl,GetNextSiblingControl,GetChildren:2,GetChildren:0,GetChildren:0,GetChildren:0',
        'operation': 'SetFocus,HotKey,SendKeys',
        'hotKey': '{Ctrl}a{Delete}',
        'value': '2021-12-31'
    },
    {
        'name': '明细列表',
        'searchDepth': 14,
        'controlType': 'TextControl',
        'operation': 'Click',
    },
    {
        'name': '查询',
        'searchDepth': 13,
        'controlType': 'ButtonControl',
        'operation': 'Click'
    },
    {
        'name': "下载全部",
        'searchDepth': 15,
        'controlType': 'TextControl',
        'operation': 'Click'
    },
    {
        'name': 'EXCEL',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'operation': 'SetFocus,Click'
    },
    {
        'name': '按交易日期正序下载',
        'searchDepth': 14,
        'controlType': 'ButtonControl',
        'operation': 'SetFocus,Click'
    }
]
save_time = time.strftime('%Y%m%d_%H%M%S')
save_path = r'C:\Users\刘嘉怡\Desktop\postal\postal_{}.xls'.format(save_time)
postal_save = [
    {
        'name': '文件名:',
        'searchDepth': 8,
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': '{Ctrl}a{Delete}'
    },
    {
        'name': '文件名:',
        'searchDepth': 8,
        'controlType': 'EditControl',
        'operation': 'SendKeys',
        'value': save_path
    },
    {
        'name': '保存(S)',
        'searchDepth': 3,
        'controlType': 'ButtonControl',
        'operation': 'Click',
    },
    {
        'subName': '中国邮政储蓄银行企业网银',
        'searchDepth': 1,
        'controlType': 'PaneControl',
        'operation': 'ShowWindow',
        'cmdShow': 2
    }
]
postal_choose_date1 = [
    {
        'subName': '中国邮政储蓄银行企业网银',
        'searchDepth': 1,
        'controlType': 'PaneControl',
        'operation': 'SetActive,ShowWindow',
        'cmdShow': 3
    },
    {
        'name': '查询日期：',
        'searchDepth': 15,
        'controlType': 'TextControl',
        'condiment': 'GetParentControl,GetNextSiblingControl,GetChildren:0,GetChildren:0,GetChildren:0,GetChildren:0',
        'operation': 'SetFocus,HotKey,SendKeys',
        'hotKey': '{Ctrl}a{Delete}',
        'value': '2021-12-01'
    },
    {
        'name': '查询日期：',
        'searchDepth': 15,
        'controlType': 'TextControl',
        'condiment': 'GetParentControl,GetNextSiblingControl,GetChildren:2,GetChildren:0,GetChildren:0,GetChildren:0',
        'operation': 'SetFocus,HotKey,SendKeys',
        'hotKey': '{Ctrl}a{Delete}',
        'value': '2021-12-31'
    }
]
# ******************************************
# UIA:工商电子银行 下载流水
# ******************************************
icbc_ele_pwd1 = 'Gsyh955883'
icbc_ele_user1 = '9558832015000034488'
icbc_ele_pwd2 = 'lk260128'
icbc_ele_user2 = '6232712102000529350'
start_year = '2021'
start_month = '12'
start_day = '1'
end_year = '2021'
end_month = '12'
end_day = '31'
icbc_save_path = r'C:\Users\刘嘉怡\Desktop\icbc\icbc_{}.txt'.format(save_time)
icbc_ele_login = [
    {

    }

]
icbc_ele_search = [
    {
        'subName': '中国工商银行企业网上银行',
        'searchDepth': 1,
        'controlType': 'WindowControl',
        'operation': 'SetActive,ShowWindow',
        'cmdShow': 3
    },
    {
        'name': '历史明细',
        'searchDepth': 16,
        'controlType': 'TextControl',
        'operation': 'Click',
        'raiseIfNotExist': True
    },
    {
        'name': '　1.日　期：　从',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetSameLevelControlByOffset:1,GetChildren:1',
        'operation': 'Click'
    },  # 开始日期 年份选择
    {
        'name': start_year,
        'searchDepth': 2,
        'controlType': 'ListItemControl',
        'operation': 'Click'
    },
    {
        'name': '　1.日　期：　从',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetSameLevelControlByOffset:3,GetChildren:1',
        'operation': 'Click'
    },  # 开始日期 月份选择
    {
        'name': start_month,
        'searchDepth': 2,
        'controlType': 'ListItemControl',
        'operation': 'Click'
    },
    {
        'name': '　1.日　期：　从',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetSameLevelControlByOffset:5,GetChildren:1',
        'operation': 'Click'
    },  # 开始日期 日期选择
    {
        'name': start_day,
        'searchDepth': 2,
        'controlType': 'ListItemControl',
        'operation': 'Click'
    },
    {
        'name': '　1.日　期：　从',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetSameLevelControlByOffset:7,GetChildren:1',
        'operation': 'Click'
    },  # 结束日期 年份选择
    {
        'name': end_year,
        'searchDepth': 2,
        'controlType': 'ListItemControl',
        'operation': 'Click'
    },
    {
        'name': '　1.日　期：　从',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetSameLevelControlByOffset:9,GetChildren:1',
        'operation': 'Click'
    },  # 结束日期 月份选择
    {
        'name': end_month,
        'searchDepth': 2,
        'controlType': 'ListItemControl',
        'operation': 'Click'
    },
    {
        'name': '　1.日　期：　从',
        'searchDepth': 17,
        'controlType': 'TextControl',
        'condiment': 'GetSameLevelControlByOffset:11,GetChildren:1',
        'operation': 'Click'
    },  # 结束日期 日期选择
    {
        'name': end_day,
        'searchDepth': 2,
        'controlType': 'ListItemControl',
        'condiment': 'GetParentControl',
        'operation': 'HotKey',
        'hotKey': '{DOWN 30}'
    },
    {
        'name': end_day,
        'searchDepth': 2,
        'controlType': 'ListItemControl',
        'operation': 'Click',
    },
    {
        'automationId': 'download',
        'searchDepth': 15,
        'controlType': 'HyperlinkControl',
        'operation': 'Click'
    }
]
icbc_ele_save = [
    {
        'raiseIfNotExist': False,
        'name': '通知',
        'automationId': 'IENotificationBar',
        'searchDepth': 3,
        'controlType': 'ToolBarControl',
        'operation': 'SetFocus'
    },
    {
        'name': '保存',
        'searchDepth': 4,
        'controlType': 'SplitButtonControl',
        'condiment': 'GetChildren:0',
        'operation': 'Click'
    },
    {
        'name': '另存为(A)',
        'searchDepth': 2,
        'controlType': 'MenuItemControl',
        'operation': 'Click'
    },
    {
        'name': '文件名:',
        'searchDepth': 7,
        'controlType': 'EditControl',
        'operation': 'HotKey,SendKeys',
        'hotKey': '{Ctrl}a{Delete}',
        'value': icbc_save_path
    },
    {
        'name': '保存类型:',
        'searchDepth': 6,
        'controlType': 'ComboBoxControl',
        'condiment': 'GetChildren:1',
        'operation': 'Click,HotKey',
        'hotKey': '{DOWN}{ENTER}'
    },
    # {
    #     'name': '所有文件 (*.*)',
    #     'controlType': 'ListItemControl',
    #     'searchDepth': 2,
    #     'operation': 'Click'
    # },
    # {
    #     'name': '保存类型:',
    #     'controlType': 'ListControl',
    #     'searchDepth': 1,
    #     'condiment': 'GetChildren:1',
    #     'operation': 'Click'
    # },
    {
        'name': '保存(S)',
        'controlType': 'ButtonControl',
        'searchDepth': 2,
        'operation': 'Click',
    },
    {
        'subName': '中国工商银行企业网上银行',
        'searchDepth': 1,
        'controlType': 'WindowControl',
        'operation': 'ShowWindow',
        'cmdShow': 2
    }
]