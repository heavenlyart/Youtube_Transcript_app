import customtkinter as custom
from youtube_transcript_api import YouTubeTranscriptApi
import pyperclip
from PIL import Image

win = custom.CTk()
#window details
custom.set_appearance_mode("dark")
custom.set_default_color_theme("green")
win.geometry("600x500")
win.title("Transcript Generator")
win.iconbitmap(r"iconimage.ico")
win.resizable(False, False)

input_box = custom.CTkEntry(win, width=300, height=80
                            ,placeholder_text="Enter the Video Id not Url", corner_radius=20)
input_box.place(x=90, y=70)

def trans_the_script():
    try:
        output_box.delete(0.0, 'end')
        v_id = input_box.get()
        print(f"The video Id give is: {v_id}")
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(v_id)
        copy = ""
        for snippet in fetched_transcript:
            copy += (snippet.text)+"\n"
        output_box.insert("0.0", copy)
        print("Transcript Recieved!")
    except Exception:
        output_box.insert("0.0", "Wrong video id or Subititle in english not available.")
    
def coping():
    pyperclip.copy(output_box.get("0.0","end"))
    print("Copied!")

Start_Button = custom.CTkButton(win,width=50, height=50, text="Start",corner_radius=40, command=trans_the_script)
Start_Button.place(x=400, y = 70)

output_box = custom.CTkTextbox(win,activate_scrollbars=True , width=300, height=200, corner_radius=20)
output_box.place(x=90, y=200)

Copy_Button = custom.CTkButton(win,width=40, height=50, text="Copy This" , corner_radius=40, command=coping)
Copy_Button.place(x=400, y = 200)

Special_Thanks = custom.CTkLabel(win, width=50, height=50, text='''Special_Thanks to:
Me_DCE
Immortal
Shaurya_Bhai, and''')
Special_Thanks.place(x=420,y=270)

image = custom.CTkImage(dark_image=Image.open(r"ujjwal.png"),size=(60,60))
ujjwal_Label = custom.CTkLabel(win, image=image, text="Ujjwal Bhai",compound="top")
ujjwal_Label.place(x=430,y=340)

win.mainloop()

