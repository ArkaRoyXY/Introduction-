from pathlib import Path

from gtts import gTTS


def main() -> None:
    text = "Hello Arka, hope you have a good afternoon and a happy Chathth Puja!"
    output_file = Path(__file__).with_name("voice.mp3")

    speech = gTTS(text=text, lang="en")
    speech.save(str(output_file))
    print(f"Saved as {output_file.name}")


if __name__ == "__main__":
    main()
