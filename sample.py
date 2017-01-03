from hue.bridge import Bridge

bridge = Bridge()
# print vars(bridge)
lights = bridge.get_lights()

lights[4]._set('on', True)
