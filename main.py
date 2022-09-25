from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='Check.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        #return 'File exist'

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            
        text = ''.join(pages)

        with open('text.txt', 'w') as file:
            file.write(text)

        text = text.replace('\n', '')

        with open('text1.txt', 'w') as file:
            file.write(text)
            
    else:
        return 'File not exist, please check the file path'


def main():
    print(pdf_to_mp3(file_path='pdf_files\Check.pdf'))


if __name__ == '__main__':
    main()
