from gtts import gTTS
import os


def main():
    gt = gTTS(text="hello", lang='en', slow=False)
    gt.save("unit_6/hello.mp3")
    os.system("mpg123 unit_6/hello.mp3")


if __name__ == '__main__':
    main()