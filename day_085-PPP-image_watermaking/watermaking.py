import customtkinter as ctk
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk, ImageGrab
import io

BACKGROUND_COLOR = "#f2f8ff"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.minsize(1000,600)
        self.title('Watermarking')
        self.configure(fg_color = BACKGROUND_COLOR)
        self.rowconfigure(list(range(4)), weight=1, uniform='a')
        self.columnconfigure(0, weight=2, uniform = 'a')
        self.columnconfigure(1, weight=7, uniform='a')
        
        ctk.CTkButton(self, text = 'Open image', command = lambda : self.open_dialog(self.import_image)).grid(row=0, column=0)
        

        self.mainloop()

    def open_dialog(self, func):
            try:
                path = filedialog.askopenfile().name
                func(path)       
            except:
                None

    def import_image(self, path):
        self.image = Image.open(path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas = MainCanvas(self, self.resize_image)
        TextButton(self, self.add_text)
        ctk.CTkButton(self, text = 'Add image', command = lambda : self.open_dialog(self.add_image)).grid(row=2, column=0)
        ctk.CTkButton(self, text = 'Save image', command = lambda : self.save_image()).grid(row=3, column=0)

    def resize_image(self, event):
        self.event_width = event.width
        self.event_height = event.height
        ratio = self.image.size[0] / self.image.size[1]
        
        canvas_ratio = self.event_width / self.event_height
        if canvas_ratio > ratio: # canvas is wider than the image
            self.image_height = int( self.event_height)
            self.image_width = int( self.image_height * ratio)
        else: 
            self.image_width = int(self.event_width)
            self.image_height = int( self.image_width / ratio)

        self.canvas.delete('all')

        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image( self.event_width /2, self.event_height /2, image=self.image_tk)
        try: 
            if self.watermark_image:
                self.add_image(self.watermark_image)
        except:
            None
        try: 
            if self.new_text:
                self.add_text(self.new_text)
        except:
            None

    def add_text(self, added_text):
        self.new_text = added_text
        self.text_added = self.canvas.create_text(self.event_width  / 2,  self.event_height / 2, text=self.new_text, fill="black", font=('Helvetica 20 bold'))
       

    def add_image(self, path):
        self.watermark_image = path
        self.water_image = Image.open(self.watermark_image)
        ratio = self.water_image.size[0] / self.water_image.size[1]
        
        canvas_ratio = self.event_width / self.event_height
        if canvas_ratio > ratio: 
            waterimage_height = 100
            waterimage_width = int(waterimage_height * ratio)
        else: 
            waterimage_width = 100
            waterimage_height = int(waterimage_width / ratio)
        
        resized_image = self.water_image.resize((waterimage_width, waterimage_height))
        self.water_image_tk = ImageTk.PhotoImage(resized_image)

        # calculating watermarking image position
        width_place = int((self.event_width - self.image_width) /2) + 100
        height_place = int((self.event_height - self.image_height) /2) + 100

        # adding watermarking image to canvas
        self.image_added = self.canvas.create_image( width_place, height_place, image=self.water_image_tk)
    
    def save_image(self):
        path = filedialog.asksaveasfile(defaultextension='.jpg',
                                        filetypes = (('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),('PNG', '*.png'),('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
        if path:
            x= self.winfo_rootx()+ self.canvas.winfo_x() + int((self.event_width - self.image_width) /2)
            y= self.winfo_rooty() + self.canvas.winfo_y() + int((self.event_height - self.image_height) /2)
            x1= x + self.image_width
            y1= y + self.image_height
            ImageGrab.grab(bbox=(x, y, x1, y1)).save(path.name)


class MainCanvas(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master = parent, background = BACKGROUND_COLOR)
        self.grid(column=1, row=0, rowspan=4, sticky='nsew')
        self.bind('<Configure>', resize_image)


class TextButton(ctk.CTkFrame):
    def __init__(self, parent, func):
        super().__init__(master = parent, fg_color = BACKGROUND_COLOR)
        self.grid(column=0, row=1,sticky='nsew', pady= 40)
        self.rowconfigure([0,1], weight=1, uniform='b')
        self.columnconfigure(0, weight=1, uniform='b')
        self.func = func
        
        ctk.CTkButton(self, text = 'Add text', command = self.get_text).grid(row=0, column=0)
        self.text_entry = ctk.CTkEntry(self)
        self.text_entry.grid(row=1, column=0)

    def get_text(self):
        text = self.text_entry.get()
        self.func(text)



if __name__ == "__main__":
    App()