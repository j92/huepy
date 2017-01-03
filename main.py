import kivy
import requests

kivy.require('1.9.1')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.app import App
from kivy.properties import ObjectProperty
from hue.bridge import Bridge


class MainController(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from the kv lang file.
    '''
    lights_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainController, self).__init__(**kwargs)

        bridge = Bridge()
        self.lights = bridge.get_lights()

        for i in self.lights:
            self.lights_layout.add_widget(Label(text=self.lights[i].name))

            state = 'normal'
            if self.lights[i].on is True:
                state = 'down'

            tgl_btn = ToggleButton(text='On', id=str(i), state=state)
            tgl_btn.bind(state=self.toggle_on_off)

            self.lights_layout.add_widget(tgl_btn)

    def toggle_on_off(self, button, state):

        if state is 'down':
            button.text = 'Off'
            self.lights[int(button.id)]._set('on', True);
        elif state is 'normal':
            button.text = 'On'
            self.lights[int(button.id)]._set('on', False);


class HuePy(App):

    def build(self):
        return MainController()


if __name__ == '__main__':
    HuePy().run()