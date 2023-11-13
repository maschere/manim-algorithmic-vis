from manim import *
import os
import random

vals = [0.1,0.7,0.2,0.3,1.0]
class MainAnim(Scene):
    def construct(self):
        TEXT_SPEED = 0.045
        self.play(Write(Text("IF Conditionals", font="Fira Code Retina")))
        self.wait(1.5)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        scode = """import random

a = random.random()
if a < 0.5:
    print("heads")
else:
    print("tails")"""

        line0=MarkupText("""<span foreground="#C586C0">import</span> <span foreground="#DCDCAA">random</span>""", font="Fira Code Retina")
        line1=MarkupText("""<span foreground="#9CDCFE">a</span> = <span foreground="#DCDCAA">random</span>.<span foreground="#DCDCAA">random</span>()""", font="Fira Code Retina")
        line2=MarkupText("""<span foreground="#C586C0">if</span> <span foreground="#9CDCFE">a</span> &lt; <span foreground="#B5CEA8">0.5</span>:""", font="Fira Code Retina")
        line3=MarkupText("""<span foreground="#000000">a</span>   <span foreground="#DCDCAA">print</span>(<span foreground="#CE9178">"heads"</span>)""", font="Fira Code Retina")
        line4=MarkupText("""<span foreground="#C586C0">else</span>:""", font="Fira Code Retina")
        line5=MarkupText("""<span foreground="#000000">a</span>   <span foreground="#DCDCAA">print</span>(<span foreground="#CE9178">"tails"</span>)""", font="Fira Code Retina")
        all_lines = VGroup(line0,line1,line2,line3,line4,line5).arrange(DOWN, center=True, aligned_edge=LEFT)

        #self.play(AddTextLetterByLetter(all_lines, time_per_char=TEXT_SPEED))
        #self.play(*[AddTextLetterByLetter(l) for l in all_lines])
        for l in all_lines:
            self.play(AddTextLetterByLetter(l, time_per_char=TEXT_SPEED))
        self.wait(1)
        
        sub = Text("These 5 lines of code simulate a coin flip.", font="Fira Code Retina", font_size=20)
        sub.move_to(config.bottom + 0.5*UP)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(5)
        self.remove(sub)
        sub = Text("Let's check out how.", font="Fira Code Retina", font_size=20)
        sub.move_to(config.bottom + 0.5*UP)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(2)
        self.remove(sub)
        
        self.play(all_lines.animate.set_opacity(0.4).scale(0.7).shift(DOWN))
        box = SurroundingRectangle(line1, corner_radius=0.2)
        self.play(Create(box),line1.animate.set_opacity(1),line0.animate.set_opacity(0))
        self.play(box.animate.shift(3.7*UP),line1.animate.shift(3.7*UP))

        sub = Text("We draw a continuous, uniform random number between 0 and 1", font="Fira Code Retina", font_size=20)
        sub.move_to(config.top + 1.2*DOWN)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(4)
        self.remove(sub)
        self.play(FadeOut(box))
        self.wait(1)
        
        # code = Code(code=scode, tab_width=4,language="Python",font="Fira Code Retina",insert_line_no=False, style="monokai")
        # for l in code.code:
        #     self.play(AddTextLetterByLetter(l, time_per_char=TEXT_SPEED))
        #self.play(AddTextLetterByLetter(code, time_per_char=TEXT_SPEED))
        val = vals.pop(0)
        square = Square(2).shift(1.9*UP) # create a square
        self.play(Create(square))  # show the circle on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        
        text = Text(f'{val}', color=RED, font="Fira Code Retina").move_to(square.get_center())

        self.play(Transform(box, SurroundingRectangle(line2, corner_radius=0.2)),line2.animate.set_opacity(1))
        self.play(box.animate.move_to(square.get_bottom()+0.2*DOWN),line2.animate.move_to(square.get_bottom()+0.2*DOWN))
        self.wait(1)
        sub = Text("Branch the code execution", font="Fira Code Retina", font_size=20)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(3)
        self.remove(sub)


        arr1 = Arrow(start=square.get_left(), end=square.get_left() + 3*DOWN, stroke_width=8).shift(0.2*LEFT)
        arr2 = Arrow(start=square.get_right(), end=square.get_right() + 3*DOWN,  stroke_width=8).shift(0.2*RIGHT)
        arr = arr1 if val < 0.5 else arr2

        self.play(FadeOut(box),Create(arr1),Create(arr2))

        self.play(Transform(box, SurroundingRectangle(line3.chars[1:], corner_radius=0.2)),line3.animate.set_opacity(1))
        self.play(box.animate.move_to(arr1.get_end()+1.5*DOWN+LEFT),line3.chars[1:].animate.move_to(arr1.get_end()+1.5*DOWN+LEFT))
        self.wait(2)

        self.play(FadeOut(line4),Transform(box, SurroundingRectangle(line5.chars[1:], corner_radius=0.2)),line5.animate.set_opacity(1))
        self.play(box.animate.move_to(arr2.get_end()+1.5*DOWN+RIGHT),line5.chars[1:].animate.move_to(arr2.get_end()+1.5*DOWN+RIGHT))
        self.wait(1)
        
        self.play(Write(text),FadeOut(box))
        self.wait(2)
  
        text2 = Text(f'{"heads" if val < 0.5 else "tails"}', color=RED, font="Fira Code Retina").move_to(arr.get_end()+0.6*DOWN)
        #l2 = VMobject()
        #self.add(l2)
        #l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(text.animate.move_to(arr.get_start()))
        self.play(MoveAlongPath(text, arr), rate_func=linear)
        self.play(text.animate.move_to(arr.get_end()+0.5*DOWN))
        self.wait(1)
        self.play(ReplacementTransform(text,text2))
        self.wait(2)

        for i in range(4):
            self.play(FadeOut(text2))
            val = vals.pop(0)
            arr = arr1 if val < 0.5 else arr2
            text = Text(f'{val}', color=RED, font="Fira Code Retina").move_to(square.get_center())
            self.play(FadeIn(text))
            text2 = Text(f'{"heads" if val < 0.5 else "tails"}', color=RED, font="Fira Code Retina").move_to(arr.get_end()+0.6*DOWN)
            self.play(text.animate.move_to(arr.get_start()))
            self.play(MoveAlongPath(text, arr), rate_func=linear)
            self.play(text.animate.move_to(arr.get_end()+0.5*DOWN))
            self.play(ReplacementTransform(text,text2))

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        self.play(Write(Text("Happy Coding", font="Fira Code Retina")))
        self.wait(1)

            

if __name__ == "__main__":
    #os.system(f"manim -pql {__file__} MainAnim")
    os.system(f"manim -qh {__file__} MainAnim")