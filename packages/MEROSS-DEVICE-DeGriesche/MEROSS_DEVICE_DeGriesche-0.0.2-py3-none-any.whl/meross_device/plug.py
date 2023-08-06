from fhem import Fhem
from meross_iot.controller.mixins.toggle import ToggleXMixin
from meross_iot.model.enums import Namespace

from src.meross_device.meross_device import _logger
from src.meross_device.meross_fhem_device import MerossFhemDevice


class Plug(MerossFhemDevice):

    STATE_ON = "on"
    STATE_OFF = "off"

    __meross_device: ToggleXMixin

    def __init__(self, meross_device: ToggleXMixin, fhem: Fhem):
        self.__meross_device = meross_device
        MerossFhemDevice.__init__(self, meross_device, fhem)

    async def _on_meross_push_notification(self, namespace: Namespace, data: dict, device_internal_id: str):
        if namespace == Namespace.CONTROL_TOGGLEX:
            self._set_fhem_state(self.STATE_OFF if data['togglex'][0]['onoff'] == 0 else self.STATE_ON)

    async def on_fhem_action(self, action):
        _logger.info("New Action: " + str(action))
        if action['reading'] == 'STATE':
            if action['value'] == self.STATE_ON:
                if not self._is_on():
                    await self._turn_on()
            elif action['value'] == self.STATE_OFF:
                if self._is_on():
                    await self._turn_off()
            elif action['value'] == "getStatus":
                self._set_fhem_state(self.STATE_ON if self._is_on() else self.STATE_OFF)
            elif action['value'] == "getDeviceType":
                self._set_fhem_device_type(self.__merossDevice.type())

    def _is_on(self):
        return self.__meross_device.is_on()

    async def _turn_on(self):
        _logger.info(f"Set {self.__meross_device.name} on...")
        await self.__meross_device.async_turn_on()
        _logger.debug("Door opened!")

    async def _turn_off(self):
        _logger.info(f"Set {self.__meross_device.name} off...")
        await self.__meross_device.async_turn_off()
        _logger.debug("Door closed!")
