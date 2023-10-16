import tkinter as tk

class CableFlowApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cable Flow App")
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)

        self.devices = []
        self.cables = []
        self.start_point = None
        self.current_line = None

    def create_device(self, x, y):
        device = self.canvas.create_rectangle(x, y, x+50, y+50, fill="lightblue")
        self.devices.append(device)

    def create_cable(self, start, end):
        cable = self.canvas.create_line(start[0], start[1], end[0], end[1], fill="black")
        self.cables.append(cable)

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        self.create_device(x, y)
        if self.start_point:
            end_point = (x + 25, y + 25)
            self.create_cable(self.start_point, end_point)
            self.start_point = None
            self.current_line = None
        else:
            self.start_point = (x + 25, y + 25)
            self.current_line = self.canvas.create_line(self.start_point[0], self.start_point[1], event.x, event.y, fill="black")

    def on_drag(self, event):
        if self.current_line:
            self.canvas.coords(self.current_line, self.start_point[0], self.start_point[1], event.x, event.y)

if __name__ == "__main__":
    app = CableFlowApp()
    app.mainloop()
