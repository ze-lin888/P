from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        # 这是为了确保打包成功的极简测试版
        return Label(text='Hello! Private Player Success!')

if __name__ == '__main__':
    TestApp().run()
