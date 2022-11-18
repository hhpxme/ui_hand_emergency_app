import os
import time
import webbrowser
import account

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.cols = 1
        self.minimum_width = 720
        self.minimum_height = 480

        # initialize layout
        self.title_layout = GridLayout(cols=1, size_hint=(1.0, 0.175))
        self.element_layout = GridLayout(cols=2)

        self.h_nav_layout = GridLayout(cols=1, rows=4, size_hint=(0.125, 1.0))
        self.video_container_layout = GridLayout(cols=1)

        self.video_filter_layout = GridLayout(cols=3, size_hint=(1.0, 0.15))
        self.video_list_view = ScrollView()

        self.user_layout = GridLayout(cols=1, spacing=5)

        # build widget in layout
        # register and sign in account
        self.email_input = TextInput(text='Input email in here')
        self.password_input = TextInput(text='Input password in here')
        self.re_password_input = TextInput(text='Input password in here')
        self.code_input = TextInput(text='Input password in here')

        # user_layout
        self.log_state = 0
        self.log = False
        self.code = -1

        # title_layout
        self.title_label = 'HOME'
        self.title_color = 'FD4556'
        self.title_font = 'fonts/vlr_font.ttf'
        self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)

        # horizontal navigation layout
        self.nav_btn_user = Button(text='User', size_hint=(None, None), width=75, height=75)
        self.nav_btn_video = Button(text='Video', size_hint=(None, None), width=75, height=75)
        # self.nav_btn_email = Button(text='Email', size_hint=(None, None), width=75, height=75)
        # self.nav_btn_sms = Button(text='SMS', size_hint=(None, None), width=75, height=75)

        self.nav_btn_user.bind(on_press=self.nav_btn_user_on_press)
        self.nav_btn_video.bind(on_press=self.nav_btn_video_on_press)
        # self.nav_btn_email.bind(on_press=self.nav_btn_email_on_press)
        # self.nav_btn_sms.bind(on_press=self.nav_btn_sms_on_press)

        if not self.log:
            # self.nav_btn_sms.set_disabled(True)
            # self.nav_btn_email.set_disabled(True)
            self.nav_btn_video.set_disabled(True)
        else:
            self.nav_btn_sms.set_disabled(False)
            # self.nav_btn_email.set_disabled(False)
            # self.nav_btn_video.set_disabled(False)

        # video_filter_layout
        self.filter_button_none = Button(text='x', size_hint=(None, None), width=50, height=50)
        self.filter_button_name = Button(text='Search by Name', size_hint=(None, None), width=150, height=50)
        self.filter_button_time = Button(text='Search by Date', size_hint=(None, None), width=150, height=50)

        # video_list_scrollview
        self.cat = [[0, 'user'], [1, 'video']]
        self.current_state = self.cat[0][0]
        self.link = os.path.abspath(self.cat[1][1])
        self.video_list_layout = self.scrollview_layout(cat_path=self.cat[1][1])

        # add widget to layout
        # title_layout
        self.title_layout.add_widget(self.title)

        # horizontal navigation layout
        self.h_nav_layout.add_widget(self.nav_btn_user)
        self.h_nav_layout.add_widget(self.nav_btn_video)
        # self.h_nav_layout.add_widget(self.nav_btn_email)
        # self.h_nav_layout.add_widget(self.nav_btn_sms)

        # video_filter_layout
        self.video_filter_layout.add_widget(self.filter_button_none)
        self.video_filter_layout.add_widget(self.filter_button_name)
        self.video_filter_layout.add_widget(self.filter_button_time)

        # user_layout
        self.user_layout = self.account_layout()

        # self.user_layout.add_widget(self.email_label)
        # self.user_layout.add_widget(self.email_textinput)
        # self.user_layout.add_widget(self.password_label)
        # self.user_layout.add_widget(self.password_textinput)
        # self.user_layout.add_widget(self.v_password_label)
        # self.user_layout.add_widget(self.v_password_textinput)
        # self.user_layout.add_widget(self.code_label)
        # self.user_layout.add_widget(self.code_textinput)
        # self.user_layout.add_widget(self.btn_submit)

        # video_list_layout
        self.video_list_view.add_widget(self.video_list_layout)

        # add layout to layout
        if self.current_state == self.cat[0][0]:
            self.video_container_layout.add_widget(self.user_layout)
        else:
            self.video_container_layout.add_widget(self.video_filter_layout)
            self.video_container_layout.add_widget(self.video_list_view)

        self.element_layout.add_widget(self.h_nav_layout)
        self.element_layout.add_widget(self.video_container_layout)

        self.add_widget(self.title_layout)
        self.add_widget(self.element_layout)

    def nav_btn_user_on_press(self, instance):
        # replace title
        self.title_label = str(self.nav_btn_user.text)
        self.title_layout.remove_widget(self.title)
        self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)
        self.title_layout.add_widget(self.title)

        # replace scroll view
        self.log_state = 0
        self.video_container_layout.remove_widget(self.video_filter_layout)
        self.video_container_layout.remove_widget(self.video_list_view)
        self.video_container_layout.remove_widget(self.user_layout)
        self.user_layout = self.account_layout()
        self.video_container_layout.add_widget(self.user_layout)
        self.current_state = self.cat[0][0]

    def nav_btn_video_on_press(self, instance):
        # replace title
        self.title_label = str(self.nav_btn_video.text)
        self.title_layout.remove_widget(self.title)
        self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)
        self.title_layout.add_widget(self.title)

        # replace scroll view
        self.video_list_view.remove_widget(self.video_list_layout)
        self.video_list_layout = self.scrollview_layout(cat_path=self.cat[1][1])
        self.video_list_view.add_widget(self.video_list_layout)

        if self.current_state == self.cat[0][0]:
            self.video_container_layout.remove_widget(self.user_layout)
            self.video_container_layout.add_widget(self.video_filter_layout)
            self.video_container_layout.add_widget(self.video_list_view)

        self.current_state = self.cat[1][0]
        self.link = os.path.abspath(self.cat[1][1])

    # def nav_btn_email_on_press(self, instance):
    #     # replace title
    #     self.title_label = str(self.nav_btn_email.text)
    #     self.title_layout.remove_widget(self.title)
    #     self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)
    #     self.title_layout.add_widget(self.title)
    #
    #     # replace scroll view
    #     self.video_list_view.remove_widget(self.video_list_layout)
    #     self.video_list_layout = self.scrollview_layout(cat_path=self.cat[2][1])
    #     self.video_list_view.add_widget(self.video_list_layout)
    #
    #     if self.current_state == self.cat[0][0]:
    #         self.video_container_layout.remove_widget(self.user_layout)
    #         self.video_container_layout.add_widget(self.video_filter_layout)
    #         self.video_container_layout.add_widget(self.video_list_view)
    #
    #     self.current_state = self.cat[2][0]
    #     self.link = os.path.abspath(self.cat[2][1])

    # def nav_btn_sms_on_press(self, instance):
    #     # replace title
    #     self.title_label = str(self.nav_btn_sms.text)
    #     self.title_layout.remove_widget(self.title)
    #     self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)
    #     self.title_layout.add_widget(self.title)
    #
    #     # replace scroll view
    #     self.video_list_view.remove_widget(self.video_list_layout)
    #     self.video_list_layout = self.scrollview_layout(cat_path=self.cat[3][1])
    #     self.video_list_view.add_widget(self.video_list_layout)
    #
    #     if self.current_state == self.cat[0][0]:
    #         self.video_container_layout.remove_widget(self.user_layout)
    #         self.video_container_layout.add_widget(self.video_filter_layout)
    #         self.video_container_layout.add_widget(self.video_list_view)
    #
    #     self.current_state = self.cat[3][0]
    #     self.link = os.path.abspath(self.cat[3][1])

    def btn_login_on_press(self, instance):
        self.log_state = 1
        self.video_container_layout.remove_widget(self.user_layout)
        self.user_layout = self.account_layout()
        self.video_container_layout.add_widget(self.user_layout)

    def btn_reg_on_press(self, instance):
        self.log_state = 2
        self.video_container_layout.remove_widget(self.user_layout)
        self.user_layout = self.account_layout()
        self.video_container_layout.add_widget(self.user_layout)

    def btn_send_code(self, instance):
        e = self.email_input.text
        code = account.send_code(email=e)
        self.code = code
        if code == -1:
            print('error')
        else:
            print(code)

    def login_btn_press(self, instance):
        e = self.email_input.text
        p = self.password_input.text
        c = self.code_input.text
        if self.code == int(c):
            self.log = account.login(email=e, password=p)
        else:
            print('error')
        if not self.log:
            print('error')
        else:
            self.log_state = -1
            self.video_container_layout.remove_widget(self.user_layout)
            self.user_layout = self.account_layout()
            self.video_container_layout.add_widget(self.user_layout)
            self.nav_btn_sms.set_disabled(False)

    def register_btn_press(self, instance):
        e = self.email_input.text
        p = self.password_input.text
        rp = self.re_password_input.text
        c = self.code_input.text
        if rp == p:
            if self.code == int(c):
                self.log = account.register(email=e, password=p)
        else:
            print('re-password and password is not same')

        if not self.log:
            print('error')
        else:
            self.log_state = -1
            self.video_container_layout.remove_widget(self.user_layout)
            self.user_layout = self.account_layout()
            self.video_container_layout.add_widget(self.user_layout)
            self.nav_btn_sms.set_disabled(False)

    def logout_press(self, instance):
        self.log = False
        self.log_state = 0
        self.video_container_layout.remove_widget(self.user_layout)
        self.user_layout = self.account_layout()
        self.video_container_layout.add_widget(self.user_layout)

    def account_layout(self):
        layout = GridLayout(cols=1, spacing=25, pos_hint={"center_x": 0.5, "center_y": 0.5})
        top_layout = GridLayout(spacing=5)
        bot_layout = GridLayout(spacing=5)
        if not self.log:
            if self.log_state == 0:
                top_layout.cols = 1
                top_layout.size_hint = (0.75, 0.75)
                top_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                bot_layout.cols = 1
                bot_layout.size_hint = (0.75, 0.75)
                bot_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                btn_login = Button(text='Login', size_hint=(None, None), width=480, height=120)
                btn_signin = Button(text='Register New Account', size_hint=(None, None), width=480, height=120)
                btn_login.bind(on_press=self.btn_login_on_press)
                btn_signin.bind(on_press=self.btn_reg_on_press)
                top_layout.add_widget(btn_login)
                top_layout.add_widget(btn_signin)
            elif self.log_state == 1:
                top_layout.cols = 2
                top_layout.size_hint = (0.75, 0.3)
                top_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                bot_layout.cols = 1
                bot_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                email_label = Label(text='Email: ', size_hint_x=0.3, font_size=28)
                self.email_input = TextInput(font_size=28, multiline=False)
                password_label = Label(text='Password: ', size_hint_x=0.3, font_size=28)
                self.password_input = TextInput(font_size=28, multiline=False)
                code_layout = GridLayout(cols=3)
                v_code_label = Label(text='Verified Code: ', size_hint_x=0.3, font_size=28)
                self.code_input = TextInput(font_size=28, multiline=False)
                v_code_send_button = Button(text='Send Code', size_hint_x=0.3, font_size=18)
                v_code_send_button.bind(on_press=self.btn_send_code)
                btn_submit = Button(text='Submit', size_hint=(0.5, None), height=50, font_size=28)
                btn_submit.bind(on_press=self.login_btn_press)
                code_layout.add_widget(self.code_input)
                code_layout.add_widget(v_code_send_button)
                top_layout.add_widget(email_label)
                top_layout.add_widget(self.email_input)
                top_layout.add_widget(password_label)
                top_layout.add_widget(self.password_input)
                top_layout.add_widget(v_code_label)
                top_layout.add_widget(code_layout)
                bot_layout.add_widget(btn_submit)
            elif self.log_state == 2:
                top_layout.cols = 2
                top_layout.row_default_height = 60
                top_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                bot_layout.cols = 1
                bot_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                email_label = Label(text='Email: ', size_hint_x=0.3, font_size=28)
                self.email_input = TextInput(font_size=28, multiline=False)
                password_label = Label(text='Password: ', size_hint_x=0.3, font_size=28)
                self.password_input = TextInput(font_size=28, multiline=False)
                v_password_label = Label(text='Re-password: ', size_hint_x=0.3, font_size=28)
                self.re_password_input = TextInput(font_size=28, multiline=False)
                code_layout = GridLayout(cols=3)
                v_code_label = Label(text='Verified Code: ', size_hint_x=0.3, font_size=28)
                self.code_input = TextInput(font_size=28, multiline=False)
                v_code_send_button = Button(text='Send Code', size_hint_x=0.3, font_size=18)
                v_code_send_button.bind(on_press=self.btn_send_code)
                btn_submit = Button(text='Register', size_hint=(0.5, None), height=50, font_size=28)
                btn_submit.bind(on_press=self.register_btn_press)
                code_layout.add_widget(self.code_input)
                code_layout.add_widget(v_code_send_button)
                top_layout.add_widget(email_label)
                top_layout.add_widget(self.email_input)
                top_layout.add_widget(password_label)
                top_layout.add_widget(self.password_input)
                top_layout.add_widget(v_password_label)
                top_layout.add_widget(self.re_password_input)
                top_layout.add_widget(v_code_label)
                top_layout.add_widget(code_layout)
                bot_layout.add_widget(btn_submit)
        else:
            top_layout.cols = 2
            top_layout.size_hint = (0.75, 0.8)
            top_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            bot_layout.cols = 1
            bot_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            top_layout.add_widget(Label(text="Account", font_size=32, color=self.title_color, font_name=self.title_font))
            btn_logout = Button(text='Logout', size_hint=(0.5, None), height=50, font_size=28)
            btn_logout.bind(on_press=self.logout_press)
            bot_layout.add_widget(btn_logout)

        layout.add_widget(top_layout)
        layout.add_widget(bot_layout)

        return layout

    def scrollview_layout(self, cat_path):
        layout = GridLayout(cols=2, spacing=5, size_hint_y=None)
        btn_layout_widget = []
        buttons = []
        i = 0
        for f_name in os.listdir(cat_path):
            btn_layout_widget.append([str(f_name), str(time.ctime(os.stat(cat_path + '/' + f_name).st_ctime))])
            buttons.append(Button(text=btn_layout_widget[i][0], size_hint=(0.6, None), height=40))
            buttons[i].bind(on_press=self.link_press)
            layout.add_widget(buttons[i])
            layout.add_widget(Label(text=btn_layout_widget[i][1], size_hint=(0.4, None), height=40))
            i += 1

        return layout

    def link_press(self, instance):
        webbrowser.open(self.link + '/' + str(instance.text), new=2)
        print(instance)


class MyApp(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    MyApp().run()
