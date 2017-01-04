import requests
from hue.exceptions.discovery_exception import DiscoveryException
from hue.exceptions.bridge_api_exception import BridgeApiException
from hue.light import Light
import json

class Bridge(object):
    """ Hue Light object
    Light settings can be accessed or set via the properties of this object.
    """
    discovery_url = 'https://www.meethue.com/api/nupnp'

    def __init__(self, internal_ip=None, id=None):
        self.id = id
        self.internal_ip = internal_ip
        self.username = 'ZL7DOFq1lDUiZCS3eNh9qcr5RyNDcBgri-4Rfqox'

        self.lights = []

        if self.internal_ip is None or self.id is None:
            self.discover_bridge()

    def get_internal_ip(self):
        return self.internal_ip

    def get_id(self):
        return self.id

    def get_lights(self):
        r = requests.get('http://' + self.internal_ip + '/api/' + self.username + '/lights/')

        if r.status_code <> 200:
            raise BridgeApiException('Unable to make the request. ' + r.reason)

        lights = r.json()

        for i in lights:
            self._add_light(Light.from_array(self, i, lights[i]))

        return self.lights

    def set_light(self, light):
        self._add_light(light)

        requests.put(
            'http://' + self.internal_ip + '/api/' + self.username + '/lights/' + str(light.id) + '/state',
            data=json.dumps({'on': light.on, 'bri': light.bri})
        )

        print 'Light ' + light.name + ' was updated successfully'

    def discover_bridge(self):
        r = requests.get(self.discovery_url)

        if r.status_code <> 200:
            raise DiscoveryException('The bridge discovery service responded with HTTP status code ' + r.status_code)

        bridges = r.json()

        if len(bridges) == 0:
            raise DiscoveryException('The bridge discovery service could not locate any bridge in your network.')

        self.internal_ip = bridges[0]['internalipaddress']
        self.id = bridges[0]['id']

    def _add_light(self, light):
        self.lights.append(light)