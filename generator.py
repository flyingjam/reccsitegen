import codecs
import markdown

def main():
    input_file = codecs.open("template.html", mode="r", encoding = "utf-8")
    text = input_file.read()
    print(text)

if __name__ == "__main__":
    main()
