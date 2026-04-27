from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        # 这是一个简单的按钮，点击它会显示“Hello”
        return Button(text='Hello! This is my Private Player')

if __name__ == '__main__':
    MainApp().run()
