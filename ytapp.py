import tkinter as tk
import cutomtkinter 
import colorama
from pytube import Youtube 
from colorama  import Fore , Back , Style   
from tkinter import filedialog
def startDownload(option):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "hq":
            video = ytObject.streams.get_highest_resolution()
            file_path_hq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_hq)
        elif option == "lq":
            video = ytObject.streams.get_lowest_resolution()
            file_path_lq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_lq)
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
            file_path_audio = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio files", "*.mp3")])
            video.download(file_path_audio)
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

       finishLabel.configure(text="Downloaded !!",  text_color"green")
except:
       finishLabel.configure(text="Download Error", text_color="red")

from tkinter.font import Font
 
 
def on_progress(stream,chunck, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size = bytes
    percentage_of_completion = bytes_download/total_size * 100
    perasconmanzana = str(int(percentage_of_completion))
    on_progress.configure(text= perasconmanzana + "%")
    progress.update()
progressbar.set(float(percentage_of_completion)/100 )

customtkinter.set_appeareance_mode("system")
customtkinter.set_default_color_theme("dark")

digoalejandroytapp= customtkinter.CTk()
digoalejandroytapp.icon("")
digoalejandroytapp.iconbitmap(iconit.icon)
digoalejandroytapp.geometry("720x480")
digoalejandroytapp.title("dev yt downloader link diego alejandro chavez ")
title = customtkinter.CTkLabel(digoalejandroytapp, text="Insertar un link para descargar ",width=200,height=10 font=("cursive,28"))
title.pack(padx=10,padx=10)

url_var = tk.StringVar()
link = customtkinter.CTkEntry(digoalejandroytapp, width=500 , height= 50 textvariable=url_var)
link.pack()
FinishLabel = custom.tkinter.CTkLabel(digoalejandroytapp, text="")
FinishLabel.pack()

progressbar = customtkinter.CTkLabel(digoalejandroytapp, text="%0")
progressbar.pack()

progressbar.customtkinter.CTkProgressBar(digoalejandroytapp, width=400)
progressbar.pack(padx=10, pady=10)
download_hq =customtkinter.CTkButton(digoalejandroytapp , text="Descargar en formato rapido  ", command=lambda: startDownlaod ("hightQuality") )
download_hq.pack(padx=10 , pady=10)
download_lq = customtkinter.CTkButton(digoalejandroytapp ,text="Descargando en baja calidad waiting please credits Diego Alejandro Zapata Chavez ", command=lambda: startDownlaod ("LowQuality"))
download_lq.pack(padx = 10 , pady=10)

download_audio = customtkinter.CTkButton(digoalejandroytapp, text="Descargar mp3 aux only css++  ")
download_audio.pack(padx= 10 , pady=10)


digoalejandroytapp.mainloop()
