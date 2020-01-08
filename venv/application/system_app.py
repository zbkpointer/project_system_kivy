import kivy
kivy.require('1.11.1')

from kivy.config import Config
print(Config.get('kivy','default_font'))
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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.camera import Camera
import cv2
from kivy.uix.video import Video
from functools import partial
from datetime import date
import time
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
        # 计算网络速度
        self.last_bytes_recv = psutil.net_io_counters().bytes_recv
        self.last_bytes_sent = psutil.net_io_counters().bytes_sent

        self.ids.cpu_temp_id.text =  'CPU温度'
        self.ids.cpu_usage_id.text = 'CPU使用'

        self.ids.mem_usage_id.text = '内存使用'

        self.ids.down_net_speed_id.text = '下行速度'
        self.ids.up_net_speed_id.text = '上行速度'

        cpu_event = Clock.schedule_interval(self.display_cpu_percent,1.)
        Clock.schedule_interval(self.display_mem_percent,1.)
        Clock.schedule_interval(self.display_down_net_speed, 1.)
        Clock.schedule_interval(self.display_up_net_speed, 1.)
        Clock.schedule_interval(self.display_date_time, 1.)
        #Clock.schedule_once(self.pop_up_window, 2.)

    '''
        展示CPU使用率
    '''

    def display_cpu_percent(self,dt):
        percent = str(psutil.cpu_percent(interval=None))
        self.ids.cpu_percent.text = percent

    def display_cpu_temp(self,dt):
        print('hello,call_back')
        #print(psutil.cpu_percent())
        #self.ids.cpu_temp.text = str(temp)

    '''
        展示内存使用率
    '''
    def display_mem_percent(self,dt):
        percent = str(psutil.virtual_memory().percent)
        self.ids.mem_usage.text = percent

    '''
        展示下行网速
    '''
    def display_down_net_speed(self,dt):
        curr_recv_bytes = psutil.net_io_counters().bytes_recv
        delnet = (curr_recv_bytes - self.last_bytes_recv)/1024
        self.ids.down_net_speed.text = str(delnet)[:5] + 'KB/s'
        self.last_bytes_recv = curr_recv_bytes

    '''
        展示上行网速
    '''
    def display_up_net_speed(self, dt):
        curr_sent_bytes = psutil.net_io_counters().bytes_sent
        delnet = (curr_sent_bytes - self.last_bytes_sent) / 1024
        self.ids.up_net_speed.text = str(delnet)[:5] + 'KB/s'
        self.last_bytes_sent = curr_sent_bytes

    '''
        展示时间
    '''
    def display_date_time(self, dt):
        self.ids.time.text = time.strftime("%H:%M", time.localtime())
        self.ids.date.text = str(date.today()) + ' ' +'星期' + str(date.today().weekday()+1)

    '''
        测试弹出框
    '''

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

    '''
        打电话
    '''
    def phone(self):
        button = Button(text='挂断',size_hint=(0.3,0.15),pos_hint= {'x':.35, 'y':.05})
        #button.pos_x = 370
        #label = Label(text='内容',size_hint=(None, None),size=(300,500))

        #初始化摄像头，此时Play=False
        camera = Camera(id='camera',resolution=(480, 640),play=False,pos=(0,-80))

        #filename = 'E:\\PythonProjects\\project_kivy\\venv\\share\\kivy-examples\\widgets\\cityCC0.mpg'
        #filename = 'http://192.168.0.100:8080/'
        #filename = 'udp://@192.168.0.100:1234'
        #filename = 'rtsp://192.168.0.100:8554/'
        filename = 'http://192.168.0.100:6060'
        video = Video(source=filename,play='True',pos=(0,120),volume=0.8)

        relaytiveLayout = RelativeLayout(id='phone')
        relaytiveLayout.add_widget(camera)
        relaytiveLayout.add_widget(video)
        relaytiveLayout.add_widget(button)

        # label = Label(text='内容',size_hint=(None, None))
        # floatLayout = FloatLayout(size_hint=(None, None),size=(400, 600))
        # floatLayout.add_widget(label)
        # floatLayout.add_widget(relaytiveLayout)

        #覆盖整个窗口
        popup = Popup(title='正在与谁通话',
                      content=relaytiveLayout,
                      size_hint=(None, None),size=(300,500), auto_dismiss=False)

        #self.proxy_ref.add_widget(popup)
        print(popup.parent)

        popup.id = 'popup'

        #button.pos_x = popup.center_x + (popup.size[0] - button.size[0])/2
        #print(camera.size)

        #print(self.children[0].children)
        #print(self.ids.popup)



        #print(camera.properties())


        #print(self.id['camera'])
        #print(type(self.id['popup']))

        #print(popup.proxy_ref)


        '''
            摄像头没有释放,因为属性play值为True
        '''
        button.bind(on_press=popup.dismiss)

        #button.bind(on_touch_down=cv2.)

        #button.bind(on_press=)
        #popup.bind(on_dismiss=self.play)

        popup.open()

        for widget in self.walk():
            print('{} -> {}'.format(widget, widget.id))
            # if isinstance(widget,RelativeLayout):
            #     #print('{} -> {}'.format(widget,widget.id))
            #     for child in widget.walk():
            #         print('{} -> {}'.format(child, child.id))

        #为什么需要obj,其他值也可以，或许需要它来绑定事件的对象
        def closeCamera(obj):
            print(camera.play)
            #print(str(obj))
            camera.play = False
            print(camera.play)

        def closeVideo(obj):
            video.play = False

        button.bind(on_press=closeCamera)
        button.bind(on_press=closeVideo)


        # 稍后启动摄像头
        camera.play = True
        #video.paly = True


    def dismiss(self,instance):
        #self.id['camera'].paly = False
        #self.id['popup'].dismiss()
        print(self.ids['camera'].paly)
        #self.get
        print(self.id['popup'])



    '''
        循环列表
    '''
    def view(self):

        print(self.ids.rv.data)
        print(self.ids.cpu_temp)
        self.ids.rv.data = product_data()
        #print(self.ids.view.state)
        #print(self.ids.view.__self__)
        print(self.ids.rv.data[9])
        #print(self.ids.row)


class SystemApp(App):

    #重写这个方法创建APP
    def build(self):
        #基于类名自动创建初始文件
        print('系统配置文件存储位置为：' + str(App.get_application_config(self)))
        #config = self.config


        return SystemLayout()



if __name__ == '__main__':
    SystemApp().run()