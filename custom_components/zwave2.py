DOMAIN = 'zwave2'
REQUIREMENTS = ['pyzwave==1.0.1']

CONF_USB_PATH = 'usb_path'

DATA_ZWAVE2_CONTROLLER = 'zwave2_controller'

async def async_setup(hass, config):
    from pyzwave import Controller

    class Receiver:
        def on_central_scene_notification(self,
                                          node,
                                          sequence_number,
                                          slow_refresh,
                                          key_attribute,
                                          scene_number):
            pass

        def on_switch_binary_report(self, node, value):
            pass

        def on_switch_multilevel_report(self, node, value):
            pass

    receiver = Receiver()

    usb_path_config = config[DOMAIN][CONF_USB_PATH]

    controller = Controller()
    hass.data[DATA_ZWAVE2_CONTROLLER] = controller
    
    controller.set_receiver(receiver)
    controller.open(usb_path_config)
    return True
