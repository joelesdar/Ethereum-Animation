from shutil import move
from manim import *

class QuoteDecentralized(Scene):
    def construct(self):
        text = Text('"La revolución será descentralizada"', font_size=48, slant=ITALIC, color=WHITE)
        ethereum = SVGMobject(file_name="ethereum.svg", fill_color='#636890').scale(1.2)
        self.play(DrawBorderThenFill(ethereum, rate_func=linear))
        self.wait(1)
        self.play(ethereum.animate.move_to(UP*2).scale(.8))
        self.wait(1)
        self.play(Write(text), run_time=3)
        self.wait(2)

# class TextColorExample(Scene):
#     def construct(self):
#         text1 = Text('Hello world', color=BLUE).scale(3)
#         text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
#         self.add(text1, text2)
# #c99d66