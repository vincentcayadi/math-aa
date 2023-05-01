from manim import *


class introduction(Scene):
    # Diplay the title Math AA - The “Open Problem”
    def construct(self):
        title = Text("The “Open Problem”", should_center=True).scale(1.5)
        self.play(Write(title))
        self.play(title.animate.shift(UP * 1))
        text2 = Text("Aidan, Asher, Caine, Vincent").scale(1)
        self.play(Write(text2))
        self.play(FadeOut(text2))
        self.play(title.animate.shift(DOWN * 1))
        self.play(FadeOut(title))


class maximum_volume(Scene):
    # Display the title Maximum Volume and have a underline
    def construct(self):
        title = Text("Finding Max Volume", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=2))


class volume_of_box(Scene):
    def construct(self):
        rect1 = Rectangle(width=3, height=5, fill_color=ORANGE,
                          fill_opacity=1.0, stroke_width=0,)

        # Create 4 sqaures and align it to the corners of the rectangle
        s2 = Square(side_length=0.5, fill_color=BLUE,
                    fill_opacity=1.0, stroke_width=0,)
        s1 = Square(side_length=0.5, fill_color=BLUE,
                    fill_opacity=1.0, stroke_width=0,)
        s3 = Square(side_length=0.5, fill_color=BLUE,
                    fill_opacity=1.0, stroke_width=0,)
        s4 = Square(side_length=0.5, fill_color=BLUE,
                    fill_opacity=1.0, stroke_width=0,)

        s1.align_to(rect1, LEFT + UP)
        s2.align_to(rect1, LEFT + DOWN)
        s3.align_to(rect1, RIGHT + UP)
        s4.align_to(rect1, RIGHT + DOWN)

        # Brace the width and height of the rectangle
        brace_width = Brace(rect1, direction=UP)
        brace_height = Brace(rect1, direction=RIGHT)
        # Add text to the braces
        text_height = brace_height.get_text("59.4cm")
        text_width = brace_width.get_text("42.0cm")

        p1 = [1, 2.5, 0]
        p2 = [-1, 2.5, 0]

        p3 = [1.5, -2, 0]
        p4 = [1.5, 2, 0]
        brace_width2 = BraceBetweenPoints(p1, p2, direction=UP)
        text_width2 = brace_width2.get_text("42.0cm - 2x")

        brace_height2 = BraceBetweenPoints(p3, p4, direction=RIGHT)
        text_height2 = brace_height2.get_text("59.4cm - 2x")

        volume = MathTex("V = x (42.0 - 2x)(59.4 - 2x) cm^3")
        # Add the braces and text to the scene and animate
        self.play(FadeIn(rect1))
        self.play(GrowFromCenter(brace_width), FadeIn(text_width))
        self.play(GrowFromCenter(brace_height), FadeIn(text_height))
        self.wait(1)
        self.play(ShrinkToCenter(brace_width), FadeOut(text_width))
        self.play(ShrinkToCenter(brace_height), FadeOut(text_height))
        self.play(FadeIn(s1), FadeIn(s2), FadeIn(s3), FadeIn(s4))
        self.wait(1)
        self.play(GrowFromCenter(brace_width2), FadeIn(text_width2))
        self.play(GrowFromCenter(brace_height2), FadeIn(text_height2))
        self.wait(1)
        self.play(Write(volume.next_to(rect1, DOWN, buff=0.5)))
        self.wait(1)


class differentiation(Scene):
    def construct(self):
        eq1 = MathTex("V = x (42.0 - 2x)(59.4 - 2x)")
        eq2 = MathTex("V = 4x^3 - 202.6x^2 + 2494.8x")
        differentiationed = MathTex("V' = 12x^2 - 405.2x + 2494.8")
        e = MathTex("12x^2 - 405.2x + 2494.8 = 0")
        result = Tex("x = 8.0846 or 25.715")
        conclusion = MathTex("\\therefore V = 9027.96 cm^3")
        self.play(Write(eq1))
        self.wait(1)
        self.play(Transform(eq1, eq2))
        self.wait(1)
        self.play(Transform(eq1, differentiationed))
        self.wait(1)
        self.play(Transform(eq1, e))
        self.wait(1)
        self.play(Transform(eq1, result))
        self.wait(1)
        self.play(Transform(eq1, conclusion))
        self.wait(1)
