import kivy
import requests

kivy.require('1.9.1')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty, BooleanProperty
from hue.bridge import Bridge


class LightListItem(BoxLayout):

    def __init__(self, **kwargs):
        super(LightListItem, self).__init__(**kwargs)

    bridge = ObjectProperty()
    light_index = NumericProperty()
    name = StringProperty()
    on = BooleanProperty()
    text = StringProperty()
    state = StringProperty()


class MainController(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from the kv lang file.
    '''
    lights_layout = ObjectProperty(None)
    lights = ListProperty()

    def __init__(self, **kwargs):
        super(MainController, self).__init__(**kwargs)
        self.lights = Bridge().get_lights()

    def args_converter(self, row_index, item):
        text = 'Off'
        state = 'normal'
        if item.on:
            text = 'On'
            state = 'down'

        return {'light_index': row_index, 'on': item.on, 'bri': item.bri, 'text': text, 'state': state, 'name': item.name}


class HuePy(App):

    def build(self):
        self.main_controller = MainController()
        return self.main_controller

    def toggle_on_off(self, widget, state, light_index):
        widget.text = 'On'
        on = False

        if state is 'down':
            widget.text = 'Off'
            on = True

        self.main_controller.lights[light_index].set('on', on)

if __name__ == '__main__':
    HuePy().run()