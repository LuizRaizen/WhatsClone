# -*- coding: utf-8 -*-


import os

import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex as hex_color
from kivy.utils import platform

if platform == "win":
    from kivy.config import Config

    Config.set("graphics", "resizable", False)
    Config.set("graphics", "width", 720)
    Config.set("graphics", "height", 780)
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

kivy.require('1.11.1')

WHITE_CHOCOLATE = hex_color("#ECE5DD")
TEA_GREEN = hex_color("#DCF8C6")
GREEN = hex_color("#25D366")
TEAL_GREEN = hex_color("#128C7E")
BANGLADESH_GREEN = hex_color("#075e54")
PICTON_BLUE = hex_color("34B7F1")
GRAY_CHATEAU = hex_color("#9ca1a7")
IRON = hex_color("#d7d8da")
ROLLING_STONE = hex_color("#6c777d")
EBONY_CLAY = hex_color("#232d36")
AZTEC = hex_color("#101d25")


# class MessageNotify(BoxLayout):
#
#     def __init__(self, **kwargs):
#         super(MessageNotify, self).__init__(**kwargs)
#         self.size_hint = (None, None)
#         self.size = (40, 40)
#         self.label = Label(text="13", color=(0, 0, 0, 1), bold=True)
#         self.add_widget(self.label)
#         with self.canvas:
#             Color(TEAL_GREEN)
#             RoundedRectangle(size=self.size, pos=self.pos, radius=[400, ])


class CustomButton(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.touched = None

    def on_press(self):
        with self.canvas.before:
            Color(1, 1, 1, .1)
            self.touched = RoundedRectangle(size=(self.size[0] + 30, self.size[1] + 30),
                                            pos=(self.pos[0] - 15, self.pos[1] - 15), radius=[400, ])

    def on_release(self):
        pop = Builder.load_string(alert_popup)
        pop.open()
        self.canvas.before.clear()


class StatusWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(StatusWidget, self).__init__(**kwargs)
        self.mode = "user"
        self.view = None

    def on_button(self):
        self.view = Builder.load_string(contact_view_popup)
        self.view.open()


class ContactWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(ContactWidget, self).__init__(**kwargs)
        self.view = None

    def on_button(self):
        self.view = Builder.load_string(contact_view_popup)
        self.view.open()


class GuideButton(ToggleButtonBehavior, Label):

    def __init__(self, **kwargs):
        super(GuideButton, self).__init__(**kwargs)

    def on_press(self):
        if not self.state == "down":
            self.state = "down"

    def on_release(self):
        self.canvas.before.clear()

    def on_state(self, widget, value):
        print(widget, value)
        if self.state == "down":
            self.color = TEAL_GREEN
            self.canvas.before.add(Color(1, 1, 1, .08))
            self.bg = Rectangle(size=self.size, pos=self.pos)
            self.canvas.before.add(self.bg)

            self.canvas.after.add(Color(rgba=TEAL_GREEN))
            self.flag = Rectangle(size=(self.width, 5), pos=self.pos)
            self.canvas.after.add(self.flag)
            self.bind(size=self.update, pos=self.update)
        else:
            self.color = GRAY_CHATEAU
            self.canvas.after.clear()

    def update(self, widget, value):
        self.canvas.after.clear()
        self.canvas.before.clear()
        with self.canvas.after:
            self.flag.size = self.width, 5
            self.flag.pos = self.pos
        with self.canvas.before:
            self.bg.size = self.size
            self.bg.pos = self.pos


class CircularButton(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        super(CircularButton, self).__init__(**kwargs)
        self.source = "images/circular_button.png"
        self.size_hint = (None, None)
        self.size = (120, 120)

    def on_press(self):
        with self.canvas.after:
            Color(1, 1, 1, .2)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[400, ])

    def on_release(self):
        self.canvas.after.clear()


class GuideMenu(BoxLayout):

    def __init__(self, **kwargs):
        super(GuideMenu, self).__init__(**kwargs)

    def on_guide(self, guide):
        self.parent.guide_active(guide)


class CallsGuide(ScrollView):
    pass


class StatusGuide(ScrollView):
    pass


class ConversationsGuide(ScrollView):
    pass


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = "vertical"

    @staticmethod
    def on_button():
        pop = Builder.load_string(alert_popup)
        pop.open()

    def guide_active(self, guide):
        pass


class Main(App):

    def build(self):
        return Builder.load_string(code)


conv_guide = """     
ConversationsGuide:
    id: conv_guide
"""
status_guide = """     
StatusGuide:
    id: status_guide
"""
calls_guide = """    
CallsGuide:
    id: calls_guide
"""

alert_popup = """
        
Popup:
    title: "Componente desabilitado!"
    title_size: "16sp"
    auto_dismiss: False
    size_hint: None, None
    size: 450, 400
    BoxLayout:
        orientation: "vertical"
        padding: 10, 20
        spacing: 20
        Image:
            source: "images/alert_popup.png"
            size: 200, 200
        Button:
            text: "Ok"
            size_hint: .8, .6
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: root.dismiss()

"""

contact_view_popup = """

ModalView:
    id: contact_view_popup
    size_hint: None, None
    size: 523, 607
    pos_hint: {"center_x": .5, "center_y": .632}
    border: 0, 0, 0, 0
    background: "images/user_photo.png"
    background_color: 0, 0, 0, .5
    BoxLayout:
        orientation: "vertical"
        Label:
            canvas.before:
                Color:
                    rgba: 0, 0, 0, .19
                Rectangle:
                    size: self.size
                    pos: self.pos
            text: "Luiz Ricardo"
            size_hint_y: .15
            text_size: 500, 40
            halign: "left"
            valign: "middle"
            pos_hint: {"center_x": .5, "center_y": .926}
            font_size: "20sp"
            padding_x: 20
        Widget:
        BoxLayout:
            canvas.before:
                Color:
                    rgba: AZTEC
                Rectangle:
                    size: self.size
                    pos: self.pos
            size_hint_y: .22
            CustomButton:
                source: "images/messages_icon.png"
                color: TEAL_GREEN
            CustomButton:
                source: "images/phone_icon.png"
                color: TEAL_GREEN
            CustomButton:
                source: "images/video_icon.png"
                color: TEAL_GREEN
            CustomButton:
                source: "images/info_icon.png"
                color: TEAL_GREEN

"""

code = """

#:include .kv/fonts.kv
#:include .kv/colors.kv
#:include .kv/widgets.kv

#:import ScrollEffect kivy.effects.scroll.ScrollEffect

RootWidget:               
    BoxLayout:
        id: layout
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: AZTEC
            Rectangle:
                size: self.size
                pos: self.pos
        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: 217
            canvas.before:
                Color:
                    rgba: EBONY_CLAY
                Rectangle:
                    size: self.size
                    pos: self.pos
        Carousel:
            direction: "right"
            min_move: .1
            anim_move_duration: .2
            anim_cancel_duration: .1
            anim_type: "out_quint"
            ignore_perpendicular_swipes: True
            ConversationsGuide:
                id: conv_guide
                anim_cancel_duration: .1
                ignore_perpendicular_swipes: True
                effect_cls: ScrollEffect
            StatusGuide:
            CallsGuide:
    
    Label:
        text: "WhatsClone"
        font_size: "20sp"
        font_name: FREE_SANS_BOLD
        text_size: self.size
        color: GRAY_CHATEAU
        halign: "center"
        valign: "middle"
        bold: True
        pos_hint: {"center_x": .2, "center_y": .96}
    GuideMenu:
        size_hint: .86, .08
        pos_hint: {"center_x": .56, "center_y": .88}
    CustomButton:
        source: "images/lupe.png"
        color: GRAY_CHATEAU
        size_hint: None, None
        size: 45, 45
        pos_hint: {"center_x": .8, "center_y": .955}
    CustomButton:
        source: "images/more.png"
        color: GRAY_CHATEAU
        size_hint: None, None
        size: 45, 45
        pos_hint: {"center_x": .935, "center_y": .955}
    CustomButton:
        source: "images/cam.png"
        color: GRAY_CHATEAU
        size_hint: None, None
        size: 45, 50
        pos_hint: {"center_x": .065, "center_y": .882}
    CircularButton:
        id: contacts_button
        source: "images/contacts.png"
        pos_hint: {"center_x": .85, "center_y": .07}
        on_release: root.on_button()
                
"""

app = Main()

if __name__ == "__main__":
    app.run()
