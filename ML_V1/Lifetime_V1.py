import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class WordBlasterGame(GridLayout):
    def __init__(self, **kwargs):
        super(WordBlasterGame, self).__init__(**kwargs)
        self.cols = 1
        self.word = self.select_random_word()
        self.attempts = 6
        self.guessed_letters = []
        self.is_game_over = False

        self.message_label = Label(text="Welcome to Word Blaster!\nGuess the word within 6 attempts.", font_size=24)
        self.add_widget(self.message_label)

        self.word_label = Label(text=self.display_word(), font_size=36)
        self.add_widget(self.word_label)

        self.input_box = TextInput(multiline=False, font_size=24)
        self.add_widget(self.input_box)

        self.button = Button(text="Guess", font_size=24)
        self.button.bind(on_press=self.process_guess)
        self.add_widget(self.button)

    def select_random_word(self):
        word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew"]
        return random.choice(word_list)

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word.strip()

    def process_guess(self, instance):
        guess = self.input_box.text.lower().strip()
        self.input_box.text = ""

        if guess == "":
            return

        if self.is_game_over:
            self.restart_game()
            return

        if len(guess) == len(self.word):
            if guess == self.word:
                self.show_result_popup("Congratulations! You guessed the word correctly.")
            else:
                self.message_label.text = "Wrong guess!"
                self.attempts -= 1
        else:
            if guess in self.guessed_letters:
                self.message_label.text = "You already guessed that letter."
            elif guess in self.word:
                self.message_label.text = "Correct guess!"
                self.guessed_letters.append(guess)
            else:
                self.message_label.text = "Wrong guess!"
                self.attempts -= 1
                self.guessed_letters.append(guess)

        self.word_label.text = self.display_word()

        if self.attempts == 0:
            self.show_result_popup("Game over! You ran out of attempts.\nThe word was: " + self.word)

    def show_result_popup(self, message):
        popup_layout = GridLayout(cols=1)
        result_label = Label(text=message, font_size=24, halign="center")
        popup_layout.add_widget(result_label)
        play_again_button = Button(text="Play Again", font_size=24)
        play_again_button.bind(on_press=self.restart_game)
        popup_layout.add_widget(play_again_button)
        popup = Popup(title="Word Blaster", content=popup_layout, size_hint=(None, None), size=(400, 200))
        popup.open()
        self.is_game_over = True

    def restart_game(self, instance=None):
        self.word = self.select_random_word()
        self.attempts = 6
        self.guessed_letters = []
        self.word_label.text = self.display_word()
        self.message_label.text = "Welcome to Word Blaster!\nGuess the word within 6 attempts."
        self.is_game_over = False


class WordBlasterApp(App):
    def build(self):
        return WordBlasterGame()


# Start the game
if __name__ == '__main__':
    WordBlasterApp().run()
