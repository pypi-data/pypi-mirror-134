""" AppName title

doc string of main module implemented via the Kivy framework.

TODO: after the creation of this module from the templates: REPLACE "AppName" with the name/title of your app
"""
from kivy.core.clipboard import Clipboard                                                       # type: ignore

from ae.kivy_app import KivyMainApp                                                             # type: ignore
from ae.kivy_sideloading import SideloadingMainAppMixin                                         # type: ignore


__version__ = '0.0.0'


class AppNameApp(SideloadingMainAppMixin, KivyMainApp):
    """ app class """

    def on_app_start(self):             # pylint: disable=useless-super-delegation
        """ app start event. """
        super().on_app_start()

    def on_clipboard_key_c(self, lit: str = ""):
        """ copy focused item or the currently displayed node items to the OS clipboard.

        :param lit:             string literal to copy (def=current_item_or_node_literal()).
        """
        self.vpo(f"AppName.on_clipboard_key_c: copying {lit}")
        Clipboard.copy(lit)

    def on_clipboard_key_v(self):
        """ paste copied item or all items of the current node from the OS clipboard into the current node.
        """
        lit = Clipboard.paste()
        self.vpo(f"AppName.on_clipboard_key_v: pasting {lit}")

    def on_clipboard_key_x(self):
        """ cut focused item or the currently displayed node items to the OS clipboard.
        """
        self.vpo("AppName.on_clipboard_key_x: cutting")
        # Clipboard.copy(lit) THEN cut

    def on_key_press(self, modifiers: str, key_code: str) -> bool:
        """ check key press event to be handled and processed as command/action. """
        popups_open = list(self.popups_opened())
        if popups_open:
            if key_code == 'escape':
                popups_open[-1].dismiss()
                return True
            return False

        # noinspection PyUnresolvedReferences
        return super().on_key_press(modifiers, key_code)        # pylint: disable=no-member

    def on_kivy_app_start(self):
        """ callback after app init/build to draw/refresh gui. """


# app start
if __name__ in ('__android__', '__main__'):
    AppNameApp(app_name='AppName').run_app()
