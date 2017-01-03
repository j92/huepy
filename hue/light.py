class Light(object):
    """ Hue Light object
    Light settings can be accessed or set via the properties of this object.
    """
    def __init__(self, bridge, id):
        self.bridge = bridge
        self.id = id

        self.name = ''
        self.on = False
        self.reachable = False
        self.bri = 0

    def set(self, key, value):
        if key == 'on':
            self.on = value
        elif key == 'bri':
            self.bri = value
        else:
            return

        return self.bridge.set_light(self)

    @staticmethod
    def from_array(bridge, id, data):
        light = Light(bridge, int(id))

        light.on = data['state']['on']
        light.name = data['name']
        light.reachable = data['state']['reachable']
        light.bri = data['state']['bri']

        return light