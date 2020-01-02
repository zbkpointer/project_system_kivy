import kivy
kivy.require('1.11.1')

from kivy.config import Config
# 设置中文字体
Config.set('kivy','default_font',['chinese','..\\fonts\\Alibaba-PuHuiTi-Regular.ttf','..\\fonts\\msgothic.ttc','..\\fonts\\ChangFangSong.ttf'])
# Config.write()


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial
import psutil

# load the kv file
# with open('.\\system.kv',encoding='utf-8') as f:
#     Builder.load_string(f.read())


def product_data() ->list:
    dictsList = [{'value': ''.join('a simple message')}
     for x in range(10)]
    return dictsList


class SystemLayout(BoxLayout):



    def __init__(self, **kwargs):
        super(SystemLayout, self).__init__(**kwargs)
        #Clock.schedule_interval(self.display_cpu_temp,1/2.)
        self.ids.cpu_temp_id.text =  'CPU温度'
        self.ids.cpu_usage_id.text = 'CPU使用'

        self.ids.mem_usage_id.text = '内存使用'

        cpu_event = Clock.schedule_interval(self.display_cpu_percent,1.)
        Clock.schedule_interval(self.display_mem_percent,1.)
        Clock.schedule_once(self.pop_up_window, 2.)


    def display_cpu_percent(self,dt):
        percent = str(psutil.cpu_percent(interval=None))
        self.ids.cpu_percent.text = percent

    def display_cpu_temp(self,dt):
        print('hello,call_back')
        #print(psutil.cpu_percent())
        #self.ids.cpu_temp.text = str(temp)

    def display_mem_percent(self,dt):
        percent = str(psutil.virtual_memory().percent)
        self.ids.mem_usage.text = percent

    def pop_up_window(self,dt):
        button = Button(text="关闭",size_hint=(0.8,0.3))

        label = Label(text='Hello world')
        gridLayout = GridLayout(cols=1)
        gridLayout.add_widget(label)
        gridLayout.add_widget(button)
        popup = Popup(title='温馨提示',
                      content=gridLayout,
                      size_hint=(None, None), size=(400, 400),auto_dismiss=False)
        button.bind(on_press=popup.dismiss)
        popup.open()



    def view(self):

        print(self.ids.rv.data)
        print(self.ids.cpu_temp)
        self.ids.rv.data = product_data()
        #print(self.ids.view.state)
        #print(self.ids.view.__self__)
        print(self.ids.rv.data[9])




class SystemApp(App):

    def build(self):
        return SystemLayout()



if __name__ == '__main__':
    SystemApp().run()