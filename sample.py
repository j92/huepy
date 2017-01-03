from hue.bridge import Bridge

bridge = Bridge()

lights = bridge.get_lights()

lights[4].set('on', True)
