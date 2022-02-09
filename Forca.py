import random


class Forca:
    def __init__(self):
        self.screen()
        while True:
            theme = input("\nType theme number: ")
            if not theme.isnumeric():
                print("Please, type a theme number")
                continue

            theme = int(theme)
            if theme > 4:
                print("Please, insert a valid number")
                continue

            theme = self.chose_theme(theme)
            word = self.words(theme)
            word_attempt = []

            for i in word:
                if i == ' ':
                    word_attempt.append(i)
                else:
                    word_attempt.append('_')

            attempts = 4

            while theme:
                print(f'\nThe word has {len(word)} letters - {word_attempt.count("_") } LEFT')
                print(f"{attempts} attempts remaining")
                print(f'{word_attempt}')
                letter = input("\nType a Letter: ")

                if len(letter) > 1:
                    print("Don't cheat!!")
                    continue
                hit = False
                for i, l in enumerate(word):
                    if letter.lower() == l.lower():
                        word_attempt[i] = l.upper()
                        hit = True

                if not hit:
                    attempts -= 1

                if word.lower() == ''.join(word_attempt).lower():
                    print("****CONGRATULATIONS****")
                    print(f"the word was: {word.upper()}")
                    input("Press Any Button to return Main Menu")
                    self.screen()
                    break

                elif attempts == 0:
                    print("****YOU LOSE****")
                    print(f"The word was: {word.upper()}")
                    input("---------Press Any Button to Return Main Menu---------")
                    self.screen()
                    break

            else:
                print("************BYE***********")
                break

    def screen(self):
        print("\n**********F-O-R-C-A**********")
        print('')
        print("SELECT THE THEME:")
        print('            1- Movies')
        print('            2- Animal')
        print('            3- Fruits')
        print('            4- Brazilian Cities')
        print('            0- Quit')

    def chose_theme(self, theme):
        if theme == 1:
            theme = 'Movies'

        elif theme == 2:
            theme = 'Animals'

        elif theme == 3:
            theme = 'Fruits'

        elif theme == 4:
            theme = 'Brazilian Cities'

        return theme

    def score(self):
        pass

    def words(self, theme):
        word = ''
        if theme == 'Movies':
            list_movies = ['Matrix', 'Spiderman', 'Superman', 'Deadpool', 'Batman']
            word = random.choice(list_movies)

        elif theme == 'Animals':
            list_animals = ['Tiger', 'Monkey', 'Elephant', 'Camel', 'Whale']
            word = random.choice(list_animals)

        elif theme == 'Fruits':
            list_fruits = ['Strawberry', 'Grape', 'Orange', 'Watermelon', 'Apple']
            word = random.choice(list_fruits)

        elif theme == 'Brazilian Cities':
            list_brazilian_city = ['Sao Paulo', 'Rio de Janeiro', "Brasilia", "Curitiba", "Porto Alegre"]
            word = random.choice(list_brazilian_city)

        return word

    def check_word(self, word, letter):
        pass


if __name__ == '__main__':
    Forca()
