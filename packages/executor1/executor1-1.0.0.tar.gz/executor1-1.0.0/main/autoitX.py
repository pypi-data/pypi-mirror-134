import autoit
import time
import pyperclip as pyperclip
from PIL import ImageGrab


class GPyAutoIt(object):
    @staticmethod
    def open_exe(title, exe_path, timeout=30):
        """
        打开软件并等待加载完成，窗口最大化
        :return:
        """
        try:
            autoit.run(exe_path)
            autoit.win_wait_active(title, timeout)
            autoit.win_set_state(title, flag=autoit.autoit.Properties.SW_MAXIMIZE)
        except Exception as e:
            print(e)
            print('软件打开失败')
            exit(1)

    @staticmethod
    def send_keys(title, control, text):
        """
        指定输入框输入文本
        :param title: 主窗口标题
        :param control:  对应的控件的 Class name NN
        :param text: 要输入的文本
        :return:
        """
        autoit.control_click(title, control)
        time.sleep(0.1)

        # 复制
        pyperclip.copy(text)
        # ctrl + v
        autoit.send('{CTRL DOWN}')
        autoit.send('{v down}')
        autoit.send('{v up}')
        autoit.send('{CTRL UP}')

    @staticmethod
    def control_click(title, control):
        """
        点击该打开软件的某个控件
        :param title: 主窗口标题
        :param control: 对应的控件的 Class name NN
        :return: 返回点击控件后的界面的text control对
        """
        autoit.control_click(title, control)
        if title == 'xxxxxx':
            time.sleep(2)

        return GPyAutoIt.get_dic(title)

    @staticmethod
    def control_click_no_wait(title, control):
        """
        点击该打开软件的某个控件
        :param title: 主窗口标题
        :param control: 对应的控件的 Class name NN
        :return: 返回点击控件后的界面的text control对
        """
        autoit.control_click(title, control)

    @staticmethod
    def close_notice_window(title='提示', control=None, timeout=10):
        """
        点击该打开软件的提示窗口的某个控件
        :param title: 提示窗口标题
        :param control: 对应的控件的 Class name NN
        :param timeout: 超时时间
        :return:
        """
        def close_inform():
            autoit.send('{TAB}')
            autoit.send('{TAB}')
            autoit.send('{SPACE}')
            autoit.send('{TAB}')
            autoit.send('{SPACE}')

            autoit.send('{TAB}')
            autoit.send('{TAB}')
            autoit.send('{SPACE}')
            autoit.send('{TAB}')
            autoit.send('{SPACE}')

            autoit.send('{SPACE}')
            autoit.send('{SPACE}')

        try:
            if title == '提示':
                autoit.win_wait_active(title, timeout)
                autoit.control_click(title, control)
            elif title == '告知书':
                autoit.win_wait(title, timeout)
                autoit.mouse_click(x=800, y=400)  # 点击告知书提示框使其被选中
                close_inform()

                autoit.send('{SPACE}')
                autoit.send('{SPACE}')

        except Exception as e:
            print('{}窗口关闭失败, msg : {}'.format(title, str(e)))

    @staticmethod
    def ca_login(title='FormAccountPassword', psw_input_control=None, login_control=None, timeout=10):
        """
        增值税 一般纳税人
        进入该表时要用CA密码验证
        :param title:
        :param psw_input_control:
        :param login_control:
        :param timeout:
        :return:
        """
        autoit.win_wait_active(title, timeout)
        GPyAutoIt.send_keys(title, psw_input_control, 'xxxxxx')
        GPyAutoIt.control_click(title, login_control)

    @staticmethod
    def get_username(title, username_list):
        """
        获得账号名和对应的control组成的dict
        :param title:
        :param username_list: 账号（公司全称）构成的list
        :return:dict， key为公司全称， value为对应的control
        """
        dic = dict()

        for key, value in GPyAutoIt.get_dic(title).items():
            if key in username_list:
                dic[key] = value

        return dic

    @staticmethod
    def get_dic(title):
        # :param control ：要获取的控件的Class
        """
        :param title:
        :return: 由text和对应的control组成的字典， key：text， value：control
        """
        static_control = 'WindowsForms10.STATIC.app.0.33c0d9d'
        button_control = 'WindowsForms10.BUTTON.app.0.33c0d9d'
        edit_control = 'WindowsForms10.EDIT.app.0.33c0d9d'

        def get_d(control_str, n=500):
            d = dict()
            for s in (control_str + str(i) for i in range(1, n)):
                try:
                    key = autoit.control_get_text(title, s)
                    if key == '':
                        continue
                    elif key in d.keys():
                        if isinstance(d[key], list):
                            d[key] = d[key].append(s)
                        else:
                            d[key] = [d[key], s]
                    else:
                        d[key] = s
                except autoit.autoit.AutoItError:
                    continue
            return d

        return dict(get_d(static_control), **get_d(button_control), **get_d(edit_control))

    @staticmethod
    def get_text_control(title):
        """
        获取该界面中的text和其对应的control
        :param title: 窗口标题
        :return: 由text和对应的control组成的字典， key：text， value：control
        """
        return GPyAutoIt.get_dic(title)

    @staticmethod
    def switch_account(title, username, username_list):
        """
        切换账号
        :param title: 主窗口标题
        :param username_list: 公司全称列表
        :param username: 要切换的公司全称
        :return:
        """
        dic = GPyAutoIt.get_username(title, username_list)
        return GPyAutoIt.control_click(title, dic[username])

    @staticmethod
    def get_check_result(title, timeout=2):
        """
        获取审核结果
        :param title:
        :param timeout:
        :return:返回审核结果
        """
        autoit.win_wait_active(title, timeout)
        return autoit.win_get_text(title)

    @staticmethod
    def exit_table(title, control='WindowsForms10.BUTTON.app.0.33c0d9d1', timeout=5):
        """
        返回上一级，返回税表的上一级(提示要保存表格数据时，默认不保存)
        :param title:
        :param control:
        :param timeout:
        :return:
        """
        GPyAutoIt.control_click(title, control)
        try:
            autoit.win_wait_active('提示', timeout)
            GPyAutoIt.control_click('提示', 'Button2')
        except autoit.autoit.AutoItError:
            pass

    @staticmethod
    def get_text_by_control(title, control):
        """
        根据给定的control 获取对应的text
        :param title:
        :param control:
        :return: ctrl对应的text
        """
        return autoit.control_get_text(title, control)

    @staticmethod
    def screen_capture(title, control, text=''):
        """
        对相应的控件截图
        :param title:
        :param control:
        :param text:
        :return:
        """
        left, top, right, bottom = autoit.control_get_pos(title, control, text)
        img = ImageGrab.grab((left, top, right, bottom))
        img.show()


if __name__ == '__main__':

    pass