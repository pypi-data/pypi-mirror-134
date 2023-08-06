import os
import traceback
import inspect
from importlib import import_module
from typing import Dict, Any

from webx.core.exceptions import InvalidSettingsFile


ENVIRONMENT_VARIABLE = "WEBX_CUSTOM_SETTINGS"

class DEFAULT_PROFILE:
    SECRET_KEY = os.urandom(16).hex()

class State(dict): pass

class SettingsProfile:
    def __init__(self):
        settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
        default = False
        if settings_module is None:
            # just loads custom settings
            default = True

        try:
            if default is False:
                self.settings_module = import_module(settings_module)
            else:
                self.settings_module = DEFAULT_PROFILE
        except BaseException:
            exc = traceback.format_exc()
            raise InvalidSettingsFile(exc)

        self.settings: Dict[str, Any] = {}
        self.state = State()

        self._setup()

    def _setup(self):
        """
        Formally loads settings into a settings cache attached to the profile.
        """

        for attr, setting in inspect.getmembers(self.settings_module):
            if not attr.startswith("__"):
                # being not a standard object attribute
                self.settings[attr] = setting
        
    def _recreate(self, *, persist_state: bool = True) -> "SettingsProfile":
        _temp_profile = SettingsProfile() # create a new object to simply just run
        # settings loading, and then override the existing settings with the 'refreshed' ones.
        self.settings_module = _temp_profile.settings_module
        self.settings = _temp_profile.settings
        if persist_state is False:
            self.state.clear() # just clear it.
        return _temp_profile
    
    def clear(self):
        self.settings_module = None
        self.settings.clear()

    def get(self, setting_name: str) -> Any: # even None
        return self.settings.get(setting_name)
        

settings = SettingsProfile()