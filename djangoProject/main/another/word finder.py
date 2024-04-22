import re
from fuzzywuzzy import process
from nltk.stem.snowball import RussianStemmer

text = "Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень, добавить два камня или увеличить количество камней в куче в два раза. При этом не разрешается делать ход, после которого количество камней в куче будет делиться на 3. Например, если в начале игры в куче 4 камня, Петя может первым ходом получить кучу из 5 или из 8 камней. Добавить два камня Петя не может, так как в этом случае в куче станет 6 камней, а 6 делится на 3.Игра завершается, когда количество камней в куче становится не менее 103. Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 103 или больше камней"
words = open('data-parsed.txt', encoding='utf-8')
print(words.read())
def find_words(text: str, words: list[str]) -> dict:
  stemmer = RussianStemmer()
  stem_words = [stemmer.stem(w) for w in words]
  text = text.lower()

  indexes = {}
  for word in set(text.split(' ')):
    word_indexes = [w.start() for w in re.finditer(word, text)]
    check_word = stemmer.stem('word')

    similarity = process.extractOne(check_word, stem_words)
    if similarity[1] >= 50:
      indexes[words[stem_words.index(similarity[0])]] = word_indexes

  return indexes

print(find_words(text, words))