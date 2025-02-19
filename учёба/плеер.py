import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Видео Плеер на Tkinter")

        # Метка для отображения видео
        self.label = tk.Label(root)
        self.label.pack()

        # Кнопки управления
        self.btn_open = tk.Button(root, text="Открыть видео", command=self.open_file)
        self.btn_open.pack()

        self.cap = None
        self.is_playing = False

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Видео файлы", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.cap = cv2.VideoCapture(file_path)
            self.is_playing = True
            self.play_video()

    def play_video(self):
        if self.cap and self.is_playing:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)
                self.root.after(10, self.play_video)  # Обновляем кадры

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
