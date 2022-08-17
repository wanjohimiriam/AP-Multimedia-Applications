import tkinter as tk

from tkinter import filedialog , Text
import os
root = tk.Tk()

apps=[]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",)
    filetypes= (("executales", "*exe"), ("all files", "*.*"))

    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app, bg="gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)

canvas= tk.Canvas(root, height=400, width=400, bg='#3498DB')
canvas.pack()

frame=tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile= tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#3498DB",command=addApp)
openFile.pack()

runApps=tk.Button(root, text="RunApps", padx=10, pady=5, fg="white", bg="#3498DB",command=runApps)
runApps.pack()

root.mainloop()