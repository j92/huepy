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

    def _set(self, key, value):
        if key == 'name':
            self.name = value
        elif key == 'on':
            self.on = value
        elif key == 'reachable':
            self.reachable = value
        elif key == 'bri':
            self.id = value
        else:
            return

        return self.bridge.set_light(self)
