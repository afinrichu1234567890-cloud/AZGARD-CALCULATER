from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):

    def build(self):

        self.expression = ""

        layout = GridLayout(cols=4)

        self.display = TextInput(
            multiline=False,
            readonly=True,
            font_size=32
        )

        layout.add_widget(self.display)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        ]

        for text in buttons:
            btn = Button(
                text=text,
                font_size=24
            )

            btn.bind(
                on_press=self.button_press
            )

            layout.add_widget(btn)

        return layout

    def button_press(self, instance):

        text = instance.text

        if text == "C":
            self.expression = ""
            self.display.text = ""

        elif text == "=":

            try:
                result = str(
                    eval(self.expression)
                )

                self.display.text = result
                self.expression = result

            except:
                self.display.text = "Error"
                self.expression = ""

        else:

            self.expression += text
            self.display.text = self.expression

CalculatorApp().run()
