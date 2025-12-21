from tkinter import ttk, constants, messagebox


class AddLocationView:
    """Uuden paikan lisäämisestä vastaava näkymä."""

    def __init__(self, root, weather_service, handle_show_locations_view):
        """Luokan konstruktori. Luo uuden paikan lisäysnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            weather_service: Palvelu, joka tarjoaa säätiedot.
            handle_show_locations_view: Kutsuttava-arvo, jota kutsutaan kun siirrytään takaisin paikkalistaan."""
        self._root = root
        self._weather_service = weather_service
        self._handle_show_locations_view = handle_show_locations_view
        self._frame = None
        self._location_entry = None
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _handle_add_location(self):
        """Lisää uuden paikan."""
        location_name = self._location_entry.get().strip()

        if not location_name:
            messagebox.showwarning("Virhe", "Anna paikan nimi.")
            return

        success = self._weather_service.add_location(location_name)

        if success:
            messagebox.showinfo(
                "Onnistui", f"Paikka '{location_name}' lisätty.")
            self._handle_show_locations_view()
        else:
            messagebox.showwarning(
                "Virhe", f"Paikka '{location_name}' on jo listalla.")

    def _initialize(self):
        """Alustaa näkymän."""
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Lisää uusi paikka", font=("Arial", 14))
        label.pack(pady=20)

        instruction = ttk.Label(master=self._frame, text="Paikan nimi:")
        instruction.pack()

        self._location_entry = ttk.Entry(master=self._frame, width=30)
        self._location_entry.pack(pady=10)
        self._location_entry.focus()

        button_frame = ttk.Frame(master=self._frame)
        button_frame.pack(pady=20)

        add_button = ttk.Button(
            button_frame, text="Lisää", command=self._handle_add_location, width=10)
        add_button.pack(side=constants.LEFT, padx=5)

        cancel_button = ttk.Button(
            button_frame, text="Peruuta", command=self._handle_show_locations_view, width=10)
        cancel_button.pack(side=constants.LEFT, padx=5)

        self._location_entry.bind(
            '<Return>', lambda e: self._handle_add_location())
