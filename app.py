import tkinter as tk
import speech_recognition as sr
from word import wordDict

class app:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("일제강점기 잔재 언어 탐지기")

        # Full Screen
        self.window.attributes("-fullscreen", True)
        self.fullScreenState = True
        self.window.bind("f", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.window.configure(bg="white")

        self.defaultPage = tk.Frame(self.window, bg="white")
        self.defaultPage.pack(expand=True)

        self.defaultPageTitle = tk.Label(
            self.defaultPage,
            text="일제강점기 잔재 언어 탐지기",
            font=("Arial", 60),
            fg="black",
            bg="white",
        )
        self.defaultPageTitle.pack()

        self.nowSpeaking = tk.Label(
            self.defaultPage,
            text="",
            font=("Arial", 30),
            fg="black",
            bg="white",
        )
        self.nowSpeaking.pack()

        self.window.after(1000, self.sttStart)

        # Exit
        self.window.bind("q", lambda e: self.window.destroy())
        self.window.mainloop()

    def sttStart(self):
        self.stt()
        self.window.after(1, self.sttStart)
    
    def stt(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, phrase_time_limit=3)
        
        mySpeech = r.recognize_google(audio, language='ko', show_all=True)
        try:
            if mySpeech == []:
                return
            
            strData = mySpeech['alternative'][0]['transcript']
            print(strData)
            self.nowSpeaking.configure(text=strData)

            for banWord in wordDict.keys():
                if banWord in strData:
                    print(f"{banWord} -> {wordDict[banWord]}")
                    self.defaultPageTitle.configure(text=f"{banWord} -> {wordDict[banWord]}")

            self.window.update()
        except:
            return

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == "__main__":
    app = app()