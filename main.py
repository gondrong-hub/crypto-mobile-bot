from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

import bot_service


class CryptoBotApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.status = Label(
            text="Status: STOPPED\nPAPER TRADING",
            font_size="20sp"
        )

        start_btn = Button(
            text="START BOT",
            font_size="20sp"
        )
        start_btn.bind(on_press=self.start_bot)

        stop_btn = Button(
            text="STOP BOT",
            font_size="20sp"
        )
        stop_btn.bind(on_press=self.stop_bot)

        layout.add_widget(
            Label(text="Crypto Mobile Bot", font_size="28sp")
        )
        layout.add_widget(self.status)
        layout.add_widget(start_btn)
        layout.add_widget(stop_btn)

        return layout

    def start_bot(self, instance):
        if bot_service.start():
            self.status.text = "Status: RUNNING\nPAPER TRADING"

    def stop_bot(self, instance):
        bot_service.stop()
        self.status.text = "Status: STOPPED\nPAPER TRADING"


if __name__ == "__main__":
    CryptoBotApp().run()
