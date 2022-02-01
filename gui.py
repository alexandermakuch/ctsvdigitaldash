from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '390')
from kivy.core.window import Window
import main

RPM = 0
SPEED = 0
TEMP_C = 0

#~~~ MODE = 0 -> standard; MODE = 1 -> experimental speed based on rpm calculation ~~~# # not added yet
MODE = 0

 
class MyPaintApp(App):
    def build(self):
        self.rpm_label=Label(text='RPM: {}'.format(RPM))
        self.speed_label=Label(text='Speed: {}mph'.format(SPEED))
        self.temp_label=Label(text='Oil Temperature: {} celsius'.format(TEMP_C))
        self.start=Button(text='Start measurements')
        root = GridLayout(cols=4)
        root.add_widget(self.rpm_label)
        root.add_widget(self.speed_label)
        root.add_widget(self.temp_label)
        root.add_widget(self.start)

        self.start.bind(on_release=self.record)
        return root

    def update_labels(self):
        self.rpm_label.text = 'RPM: {}'.format(RPM)
        self.speed_label.text = 'Speed: {}mph'.format(SPEED)
        self.temp_label.text = 'Temperature: {} celsius'.format(TEMP_C)
    
    def record(self, _):
        if not MODE:
            global RPM, SPEED, TEMP_C
            for _ in range(9999):
                RPM, SPEED, TEMP_C = main.routine1()
                self.update_labels()
        # else:
        #     main.routine2()


if __name__ == '__main__':
    MyPaintApp().run()