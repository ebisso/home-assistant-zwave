from homeassistant.components.light import ATTR_BRIGHTNESS, Light
from custom_components.zwave2 import DATA_ZWAVE2_CONTROLLER

DEPENDENCIES = ['zwave2']

#_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_devices, discovery_info=None):
    """Setup the sensor platform."""
    name = config.get('name')
    node = config.get('node')
    type = config.get('type')
    ctrl = hass.data[DATA_ZWAVE2_CONTROLLER]
    
    if type == 'switch_multilevel':
        async_add_devices([ZWaveLight(node, name, ctrl)])


class ZWaveLight(Light):
    """Representation of a z-wave light."""

    def __init__(self, node, name, ctrl):
        """Initialize a z-wave light."""
        self._ctrl = ctrl
        self._name = name
        self._node = node
        self._state = None
        self._brightness = None

    @property
    def name(self):
        """Return the display name of this light."""
        return self._name

    @property
    def brightness(self):
        """Return the brightness of the light.

        This method is optional. Removing it indicates to Home Assistant
        that brightness is not supported for this light.
        """
        return self._brightness

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Instruct the light to turn on.

        You can skip the brightness part if your light does not support
        brightness control.
        """
        self._brightness = kwargs.get(ATTR_BRIGHTNESS, 255) # self._light.brightness = kwargs.get(ATTR_BRIGHTNESS, 255)
        self._state = True
        self._ctrl.switch_multilevel_set(self._node, self._brightness) # self._light.turn_on()

    def turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        self._state = False #self._light.turn_off()
        self._ctrl.switch_multilevel_set(self._node, 0)

    def update(self):
        """Fetch new state data for this light.

        This is the only method that should fetch new data for Home Assistant.
        """
        #self._light.update()
        #self._light.is_on()
        pass #self._light.brightness
