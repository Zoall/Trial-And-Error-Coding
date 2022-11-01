import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class MainApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My Note Editor")
        self.window.rowconfigure(0, minsize = 800, weight = 1)
        self.window.columnconfigure(1, minsize = 800, weight = 1)

        self.create_layout()
        self.create_buttons()

    def create_layout(self):
        self.txt_editor = tk.Text(self.window, font = "Verdana")
        self.button_frame = tk.Frame(self.window, relief = tk.RAISED, bd = 2)

        self.txt_editor.grid(row = 0, column = 1, sticky = "NSEW")
        self.button_frame.grid(row = 0, column = 0, sticky = "NS")

    def create_buttons(self):
        self.openfile_button = tk.Button(self.button_frame, text = "Open", command = self.open_file)
        self.savefile_button = tk.Button(self.button_frame, text = "Save As", command = self.save_file)

        self.openfile_button.grid(row = 0, column = 0, sticky = "EW", padx = 5, pady = 5)
        self.savefile_button.grid(row = 1, column = 0, sticky = "EW", padx = 5)

    def open_file(self):
        
        self.filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
     )
        if not self.filepath:
            return

        self.txt_editor.delete("1.0", tk.END)
        with open(self.filepath, mode="r", encoding="utf-8") as input_file:
            self.text = input_file.read()
            self.txt_editor.insert(tk.END, self.text)
        self.window.title(f"My Note Editor - {self.filepath}")

    def save_file(self):
        self.filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not self.filepath:
            return
        with open(self.filepath, mode="w", encoding="utf-8") as output_file:
            self.text = self.txt_editor.get("1.0", tk.END)
            output_file.write(self.text)
        self.window.title(f"My Note Editor - {self.filepath}")


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    conv = MainApp()
    conv.run()
    


