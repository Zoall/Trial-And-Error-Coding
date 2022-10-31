import tkinter as tk

class Converter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Length Converter")
        self.window.geometry("400x150")
        self.window.resizable(width=False, height=False)
        self.window.rowconfigure([0, 1, 2, 3], weight=1)
        self.window.columnconfigure([0, 1, 2], weight=1)
    
        self.create_entry()
        self.convert()

    def meter_to_kilometer(self):
        self.meter = self.ent_meter.get()
        self.kilometer = (float(self.meter)) / 1000
        self.km_result["text"] = f"{self.kilometer} km"

    def kilometer_to_meter(self):
        self.kilometer = self.ent_km.get()
        self.meter = (1000) * (float(self.kilometer))
        self.meter_result["text"] = f"{self.meter} m"

    def create_entry(self):  
        self.meter_entry = tk.Frame(self.window)
        self.ent_meter = tk.Entry(self.meter_entry, width = 10)
        self.lbl_meter = tk.Label(self.meter_entry, text = "m")
        self.meter_title = tk.Label(self.meter_entry, text = "Meter to Kilometer:")  

        self.km_entry = tk.Frame(self.window)
        self.ent_km = tk.Entry(self.km_entry, width = 10)
        self.lbl_km = tk.Label(self.km_entry, text = "km")
        self.km_title = tk.Label(self.km_entry, text = "Kilometer to Meter:")

        self.meter_entry.grid(row=1, column = 0)
        self.ent_meter.grid(row = 1, column = 0)
        self.lbl_meter.grid(row = 1, column = 1)
        self.meter_title.grid(row = 0, column = 0)

        self.km_entry.grid(row = 3, column =0)
        self.ent_km.grid(row = 3, column = 0)
        self.lbl_km.grid(row = 3, column = 1)
        self.km_title.grid(row = 2, column = 0)

    def convert(self):
        self.meter_convert = tk.Button(
            self.window,
            text = "=",
            command = self.meter_to_kilometer
            )
        self.km_result = tk.Label(self.window, text="km")

        self.meter_convert.grid(row=1, column=1)
        self.km_result.grid(row=1, column=2)


        self.km_convert = tk.Button(
            self.window,
            text = "=",
            command = self.kilometer_to_meter
            )
        self.meter_result = tk.Label(self.window, text="m")

        self.km_convert.grid(row=3, column=1)
        self.meter_result.grid(row=3, column=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    conv = Converter()
    conv.run()



     