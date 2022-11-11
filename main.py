import os
import time

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button


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


        # build widget in layout
        # title_layout
        self.title_label = 'HOME'
        self.title_color = 'FD4556'
        self.title_font = 'fonts/vlr_font.ttf'
        self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)

        # horizontal navigation layout
        self.nav_btn_user = Button(text='User', size_hint=(None, None), width=75, height=75)
        self.nav_btn_video = Button(text='Video', size_hint=(None, None), width=75, height=75)
        self.nav_btn_email = Button(text='Email', size_hint=(None, None), width=75, height=75)
        self.nav_btn_sms = Button(text='SMS', size_hint=(None, None), width=75, height=75)

        self.nav_btn_user.bind(on_press=self.nav_btn_user_on_press)
        self.nav_btn_video.bind(on_press=self.nav_btn_video_on_press)
        self.nav_btn_email.bind(on_press=self.nav_btn_email_on_press)
        self.nav_btn_sms.bind(on_press=self.nav_btn_sms_on_press)

        # video_filter_layout
        self.filter_button_none = Button(text='x', size_hint=(None, None), width=50, height=50)
        self.filter_button_name = Button(text='Search by Name', size_hint=(None, None), width=150, height=50)
        self.filter_button_time = Button(text='Search by Date', size_hint=(None, None), width=150, height=50)

        # video_list_scrollview
        self.cat = [[0, 'user'], [1, 'video'], [2, 'email'], [3, 'sms']]
        self.current_state = self.cat[1][0]
        self.video_list_layout = self.scrollview_layout(cat_path=self.cat[1][1])


        # add widget to layout
        # title_layout
        self.title_layout.add_widget(self.title)

        # horizontal navigation layout
        self.h_nav_layout.add_widget(self.nav_btn_user)
        self.h_nav_layout.add_widget(self.nav_btn_video)
        self.h_nav_layout.add_widget(self.nav_btn_email)
        self.h_nav_layout.add_widget(self.nav_btn_sms)

        # video_filter_layout
        self.video_filter_layout.add_widget(self.filter_button_none)
        self.video_filter_layout.add_widget(self.filter_button_name)
        self.video_filter_layout.add_widget(self.filter_button_time)

        # video_list_layout
        self.video_list_view.add_widget(self.video_list_layout)


        # add layout to layout
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
        self.current_state = self.cat[1][0]

    def nav_btn_email_on_press(self, instance):
        # replace title
        self.title_label = str(self.nav_btn_email.text)
        self.title_layout.remove_widget(self.title)
        self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)
        self.title_layout.add_widget(self.title)

        # replace scroll view
        self.video_list_view.remove_widget(self.video_list_layout)
        self.video_list_layout = self.scrollview_layout(cat_path=self.cat[2][1])
        self.video_list_view.add_widget(self.video_list_layout)
        self.current_state = self.cat[2][0]

    def nav_btn_sms_on_press(self, instance):
        # replace title
        self.title_label = str(self.nav_btn_sms.text)
        self.title_layout.remove_widget(self.title)
        self.title = Label(text=self.title_label, font_size=32, color=self.title_color, font_name=self.title_font)
        self.title_layout.add_widget(self.title)

        # replace scroll view
        self.video_list_view.remove_widget(self.video_list_layout)
        self.video_list_layout = self.scrollview_layout(cat_path=self.cat[3][1])
        self.video_list_view.add_widget(self.video_list_layout)
        self.current_state = self.cat[3][0]

    def scrollview_layout(self, cat_path):
        layout = GridLayout(cols=2, spacing=5, size_hint_y=None)
        btn_layout_widget = []
        i = 0
        for f_name in os.listdir(cat_path):
            btn_layout_widget.append([str(f_name), str(time.ctime(os.stat(cat_path + '/' + f_name).st_ctime))])
            layout.add_widget(Button(text=btn_layout_widget[i][0], size_hint=(0.6, None), height=40))
            layout.add_widget(Label(text=btn_layout_widget[i][1], size_hint=(0.4, None), height=40))
            i += 1

        return layout


class MyApp(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    MyApp().run()
