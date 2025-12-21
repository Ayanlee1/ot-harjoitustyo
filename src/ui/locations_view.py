import tkinter as tk
from tkinter import ttk, constants, messagebox


class LocationsView:
    """Tallennettujen paikkojen ja säätietojen näyttämisestä vastaava näkymä."""

    def __init__(self, root, weather_service, handle_show_add_location_view):
        """Luokan konstruktori. Luo uuden paikkalista-näkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            weather_service: Palvelu, joka tarjoaa säätiedot.
            handle_show_add_location_view: Kutsuttava-arvo, jota kutsutaan kun siirrytään paikan lisäysnäkymään."""
        self._root = root
        self._weather_service = weather_service
        self._handle_show_add_location_view = handle_show_add_location_view
        self._frame = None
        self._location_listbox = None
        self._current_weather_text = None
        self._forecast_text = None
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _handle_delete_location(self):
        """Poistaa valitun paikan."""

        selection = self._location_listbox.curselection()

        if not selection:
            messagebox.showwarning(
                "Virhe", "Valitse poistettava paikka listasta.")
            return

        location_name = self._location_listbox.get(selection[0])

        if messagebox.askyesno("Vahvista poisto", f"Haluatko varmasti poistaa paikan '{location_name}'?"):
            success = self._weather_service.remove_location(location_name)

            if success:
                self._update_location_list()
                messagebox.showinfo(
                    "Onnistui", f"Paikka '{location_name}' poistettu.")
            else:
                messagebox.showerror(
                    "Virhe", f"Paikan '{location_name}' poistaminen epäonnistui.")

    def _handle_get_weather(self):
        """hakee säätiedot valitulle paikalle."""
        selection = self._location_listbox.curselection()
        if not selection:
            messagebox.showwarning("Virhe", "Valitse paikka listasta.")
            return

        location_name = self._location_listbox.get(selection[0])

        self._current_weather_text.config(state=tk.NORMAL)
        self._current_weather_text.delete(1.0, tk.END)
        self._current_weather_text.insert(1.0, "Haetaan säätietoja...")
        self._current_weather_text.config(state=tk.DISABLED)

        weather = self._weather_service.get_weather(location_name)
        self._current_weather_text.config(state=tk.NORMAL)
        self._current_weather_text.delete(1.0, tk.END)
        self._current_weather_text.insert(1.0, weather)
        self._current_weather_text.config(state=tk.DISABLED)

    def _handle_get_forecast(self):
        """hakee ennusteen valitulle paikalle."""
        selection = self._location_listbox.curselection()

        if not selection:
            messagebox.showwarning("Virhe", "Valitse paikka listasta.")
            return

        location_name = self._location_listbox.get(selection[0])

        self._forecast_text.config(state=tk.NORMAL)
        self._forecast_text.delete(1.0, tk.END)
        self._forecast_text.insert(1.0, "Haetaan ennustetta...")
        self._forecast_text.config(state=tk.DISABLED)

        forecasts = self._weather_service.get_5day_forecast(location_name)
        self._forecast_text.config(state=tk.NORMAL)
        self._forecast_text.delete(1.0, tk.END)

        if forecasts:
            for forecast in forecasts:
                self._forecast_text.insert(tk.END, forecast + "\n\n")

        self._forecast_text.config(state=tk.DISABLED)

    def _update_location_list(self):
        """päivittää paikkalistan."""
        if self._location_listbox:
            self._location_listbox.delete(0, tk.END)
            locations = self._weather_service.get_locations()
            for location in locations:
                self._location_listbox.insert(tk.END, location)

    def _initialize_location_list(self):
        """alustaa paikkalistan."""
        list_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=list_frame, text="Tallennetut paikat")
        label.pack(pady=5)

        self._location_listbox = tk.Listbox(list_frame, height=15, width=30)
        self._location_listbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            list_frame, orient=tk.VERTICAL, command=self._location_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._location_listbox.config(yscrollcommand=scrollbar.set)
        button_frame = ttk.Frame(master=list_frame)
        button_frame.pack(pady=5)

        add_button = ttk.Button(
            button_frame, text="Lisää uusi", command=self._handle_show_add_location_view)
        add_button.pack(side=tk.LEFT, padx=2)

        delete_button = ttk.Button(
            button_frame, text="Poista valittu", command=self._handle_delete_location)
        delete_button.pack(side=tk.LEFT, padx=2)

        refresh_button = ttk.Button(
            button_frame, text="Päivitä lista", command=self._update_location_list)
        refresh_button.pack(side=tk.LEFT, padx=2)

        list_frame.grid(row=1, column=0, padx=5, pady=5, sticky="ns")

        self._update_location_list()

    def _initialize_weather_info(self):
        """alustaa säätieto-osan."""
        weather_frame = ttk.Frame(master=self._frame)

        current_label = ttk.Label(
            weather_frame, text="Nykyinen sää:", font=("Arial", 10, "bold"))
        current_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self._current_weather_text = tk.Text(weather_frame, height=8, width=40)
        self._current_weather_text.grid(
            row=1, column=0, padx=5, pady=5, sticky="nsew")
        self._current_weather_text.config(state=tk.DISABLED)

        forecast_label = ttk.Label(
            weather_frame, text="5 päivän ennuste:", font=("Arial", 10, "bold"))
        forecast_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self._forecast_text = tk.Text(weather_frame, height=10, width=40)
        self._forecast_text.grid(
            row=3, column=0, padx=5, pady=5, sticky="nsew")
        self._forecast_text.config(state=tk.DISABLED)

        button_frame = ttk.Frame(weather_frame)
        button_frame.grid(row=4, column=0, pady=10)

        weather_button = ttk.Button(
            button_frame, text="Hae sää", command=self._handle_get_weather)
        weather_button.pack(side=tk.LEFT, padx=5)

        forecast_button = ttk.Button(
            button_frame, text="Hae ennuste", command=self._handle_get_forecast)
        forecast_button.pack(side=tk.LEFT, padx=5)

        weather_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        weather_frame.grid_columnconfigure(0, weight=1)
        weather_frame.grid_rowconfigure(1, weight=1)
        weather_frame.grid_rowconfigure(3, weight=1)

    def _initialize(self):
        """Alustaa näkymän."""
        self._frame = ttk.Frame(master=self._root)

        title_label = ttk.Label(
            self._frame, text="Sääsovellus", font=("Arial", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self._initialize_location_list()
        self._initialize_weather_info()

        quit_button = ttk.Button(
            self._frame, text="Lopeta", command=self._root.destroy)
        quit_button.grid(row=2, column=0, columnspan=2, pady=20)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=2)
        self._frame.grid_rowconfigure(1, weight=1)
