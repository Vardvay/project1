import requests
from bs4 import BeautifulSoup

amount_pages: dict[str: int] = {'а': 2, 'б': 1, 'в': 1}

class GufoParser():
    def __init__(self, link: str) -> None:
        self._link = link

        self._words = []

        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}
        
        response = requests.get(self._link, headers = self._headers)
        self._bs = BeautifulSoup(response.text, 'html.parser')

    def generate_letter_basis(self) -> dict[str: int]:
        table = self._bs.find('table', class_ = 'table table-responsive')
        links = table.find_all('a')
        result = {
            'а': 0
        }

        for letter in links:
            result[letter.text.lower()] = 0

        return result

    def get_data(self, pages: dict[str: int]) -> list[str]:
        self._pages_for_letters = pages
        self._words = []
        for letter in self._pages_for_letters:
            for current_page in range(1, self._pages_for_letters[letter] + 1):
                response = requests.get(f'{self._link}?page={current_page}&letter={letter}', headers = self._headers)
                bs1 = BeautifulSoup(response.text, 'html.parser')
                word_columns = bs1.find_all('ul', class_ = "list-unstyled app-word-list")
                for column in word_columns:
                    lis = column.find_all('li')
                    for word in lis:
                        self._words.append(word.text.lower())

        print("Done Successfully")
        return self._words
    
    def get_data_to_file(self, file_path: str, pages: dict[str: int]) -> None:
        with open(file = file_path, mode = 'w+') as file:
            file.write('[\n')
            words = self.get_data(pages)
            for word in words:
                file.write(f'{word},\n')
            file.write(']')

    @property
    def link(self) -> str:
        return self._link
    
    @link.setter
    def link(self, link: str) -> None:
        self._link = link

gf = GufoParser('https://gufo.me/dict/medical_dict')
gf.get_data_to_file(file_path = './data', pages = amount_pages)