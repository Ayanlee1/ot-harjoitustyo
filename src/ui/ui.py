from ui.locations_view import LocationsView
from ui.add_location_view import AddLocationView


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root, weather_service):
        """Luokan konstruktori.

        Args:
            root: TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
            weather_service: Palvelu, joka tarjoaa säätiedot."""
        self._root = root
        self._weather_service = weather_service
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_locations_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_locations_view(self):
        self._hide_current_view()
        self._current_view = LocationsView(
            self._root, self._weather_service, self._show_add_location_view)
        self._current_view.pack()

    def _show_add_location_view(self):
        self._hide_current_view()
        self._current_view = AddLocationView(
            self._root, self._weather_service, self._show_locations_view)
        self._current_view.pack()
