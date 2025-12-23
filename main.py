from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
import random

class GuessGame(MDApp):
    def build(self):
        # Налаштування теми
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        
        self.secret = random.randint(1, 100)
        self.attempts = 0
        
        screen = MDScreen()
        
        # Головний контейнер
        layout = BoxLayout(orientation='vertical', padding="20dp", spacing="20dp")
        
        # Картка гри
        card = MDCard(
            orientation='vertical',
            padding="20dp",
            size_hint=(0.9, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=4,
            radius=[20, 20, 20, 20]
        )
        
        self.info_label = MDLabel(
            text="Вгадай число від 1 до 100",
            halign="center",
            font_style="H5",
            theme_text_color="Primary"
        )
        
        self.input_num = MDTextField(
            hint_text="Введіть ваше число",
            helper_text="Тільки цифри",
            helper_text_mode="on_error",
            input_filter='int',
            font_size="20sp",
            pos_hint={"center_x": .5},
            size_hint_x=0.8
        )
        
        self.btn_check = MDFillRoundFlatButton(
            text="ПЕРЕВІРИТИ",
            pos_hint={"center_x": .5},
            on_release=self.check_guess
        )
        
        self.result_label = MDLabel(
            text="Чекаю на твій хід...",
            halign="center",
            theme_text_color="Secondary"
        )
        
        self.btn_reset = MDFillRoundFlatButton(
            text="ГРАТИ ЗНОВУ",
            pos_hint={"center_x": .5},
            opacity=0,
            disabled=True,
            on_release=self.reset_game
        )

        card.add_widget(self.info_label)
        card.add_widget(self.input_num)
        card.add_widget(self.btn_check)
        card.add_widget(self.result_label)
        card.add_widget(self.btn_reset)
        
        layout.add_widget(card)
        screen.add_widget(layout)
        return screen

    def check_guess(self, instance):
        val = self.input_num.text.strip()
        if not val:
            self.input_num.error = True
            return
            
        guess = int(val)
        self.attempts += 1
        self.input_num.text = ""
        
        if guess < self.secret:
            self.result_label.text = f"⬆️ Більше! Спроб: {self.attempts}"
        elif guess > self.secret:
            self.result_label.text = f"⬇️ Менше! Спроб: {self.attempts}"
        else:
            self.result_label.text = f"🎉 ПЕРЕМОГА! Це було {self.secret}\nСпроб: {self.attempts}"
            self.result_label.theme_text_color = "Custom"
            self.result_label.text_color = (0, 1, 0, 1)
            self.btn_check.disabled = True
            self.btn_reset.opacity = 1
            self.btn_reset.disabled = False

    def reset_game(self, instance):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.result_label.text = "Нова гра! Вгадуй:"
        self.result_label.theme_text_color = "Secondary"
        self.btn_check.disabled = False
        self.btn_reset.opacity = 0
        self.btn_reset.disabled = True

if __name__ == '__main__':
    GuessGame().run()
