from manim import *


class introduction(Scene):
    # Diplay the title Math AA - The “Open Problem”
    def construct(self):
        title = Text("The “Open Problem”", should_center=True).scale(1.5)
        self.play(Write(title))
        self.play(title.animate.shift(UP * 1))
        text2 = Text("Aidan, Asher, Caine, Vincent").scale(1)
        self.play(Write(text2))
        self.play(FadeOut(text2), title.animate.shift(DOWN))
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
        s1 = Square(side_length=0.5, fill_color=BLUE,
                    fill_opacity=1.0, stroke_width=0,)
        s2 = Square(side_length=0.5, fill_color=BLUE,
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

        brace_sqaure_width = Brace(s4, direction=RIGHT)
        brace_sqaure_width_text = brace_sqaure_width.get_text("x")

        brace_width2 = BraceBetweenPoints(p1, p2, direction=UP)
        text_width2 = brace_width2.get_text("42.0cm - 2x")

        brace_height2 = BraceBetweenPoints(p3, p4, direction=RIGHT)
        text_height2 = brace_height2.get_text("59.4cm - 2x")

        volume = MathTex("V = x (42.0 - 2x)(59.4 - 2x) cm^3")
        # Add the braces and text to the scene and animate
        self.play(FadeIn(rect1))
        self.play(GrowFromCenter(brace_width), FadeIn(text_width),
                  GrowFromCenter(brace_height), FadeIn(text_height))
        self.wait(1)
        self.play(ShrinkToCenter(brace_width), FadeOut(text_width),
                  ShrinkToCenter(brace_height), FadeOut(text_height))
        self.play(FadeIn(s1), FadeIn(s2), FadeIn(s3), FadeIn(s4))
        self.play(GrowFromCenter(brace_width2), FadeIn(text_width2),
                  GrowFromCenter(brace_height2), FadeIn(text_height2), GrowFromCenter(brace_sqaure_width), FadeIn(brace_sqaure_width_text), )
        self.wait(1)
        self.play(Write(volume.next_to(rect1, DOWN, buff=0.5)))
        self.wait(1)
        self.play(ShrinkToCenter(brace_width2), FadeOut(text_width2), ShrinkToCenter(brace_height2), FadeOut(
            text_height2), FadeOut(volume), FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4), FadeOut(rect1))


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


class first_derivative_test(Scene):
    def construct(self):
        t0 = Table(
            [["+", "0", "-"],
             ["/", "—", "\\"]],
            row_labels=[MathTex("{dy \over dx}"), Text("shape")],
            col_labels=[MathTex("8.085^-"), MathTex("8.085"),
                        MathTex("8.085^+")],
            top_left_entry=MathTex("x"))
        t1 = Table(
            [["+", "0", "-"],
             ["\\", "—", "/"]],
            row_labels=[MathTex("{dy \over dx}"), Text("shape")],
            col_labels=[MathTex("25.715^-"), MathTex("25.715"),
                        MathTex("25.715^+")],
            top_left_entry=MathTex("x"))
        self.play(Write(t0))
        self.wait(2)
        self.play(ReplacementTransform(t0, t1))
        self.wait()
        self.play(FadeOut(t1))
        # Write out the conflusion
        text = Tex("When")
        math_text = MathTex("x = 8.085")
        conclusion = MathTex("V_{max} = 9027.96 cm^3")
        text_group = VGroup(text, math_text).arrange(RIGHT)
        self.play(Write(text_group))
        self.wait()
        self.play(text_group.animate.shift(UP))
        self.play(Write(conclusion))
        self.wait()
        self.play(FadeOut(conclusion), text_group.animate.shift(DOWN))
        self.play(FadeOut(text_group))


class second_derivative_test(Scene):
    def construct(self):
        equation = MathTex("\\frac{d^2y}{dx^2} = 24x - 405.2")
        equation2 = MathTex("\\frac{d^2y}{dx^2} = -211.2 < 0")

        self.play(Write(equation))
        self.wait()
        # Write when When x = 8.08,
        self.play(equation.animate.shift(UP))
        when = Tex("When x = 8.08,")
        self.play(Write(when))
        self.wait()
        self.play(FadeOut(when), equation.animate.shift(DOWN))
        self.play(Transform(equation, equation2))
        self.wait()
        # Write out the conclusion
        conclusion = MathTex("\\therefore")
        conclusion2 = Tex("when x = 8.08, V is at a maximum")

        text_group = VGroup(conclusion, conclusion2).arrange(RIGHT)

        self.play(FadeOut(equation))
        self.play(Write(text_group))


class minimum_area(Scene):
    def construct(self):
        rect1 = Rectangle(width=3, height=5, fill_color=ORANGE,
                          fill_opacity=1.0, stroke_width=0,)

        # Create 4 sqaures and align it to the corners of the rectangle
        s1 = Square(side_length=0.5, fill_color=BLUE,
                    fill_opacity=1.0, stroke_width=0,)
        s2 = Square(side_length=0.5, fill_color=BLUE,
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

        brace_sqaure_width = Brace(s4, direction=RIGHT)
        brace_sqaure_width_text = brace_sqaure_width.get_text("x")

        brace_width2 = BraceBetweenPoints(p1, p2, direction=UP)
        text_width2 = brace_width2.get_text("42.0cm - 2x")

        brace_height2 = BraceBetweenPoints(p3, p4, direction=RIGHT)
        text_height2 = brace_height2.get_text("59.4cm - 2x")

        # Area equation
        area = MathTex("A_{paper} = 59.4 * 42.0 = 2494.8")
        area_of_sqaure = MathTex("A_{square} = x^2")
        area_of_sqaure_expanded = MathTex("A_{square} = 8.085^2")
        area_of_paper_used = MathTex("A_{used} = 2494.8 - 4(8.085)^2")
        area_of_paper_used2 = MathTex("A_{used} = 2233.2cm^2")
        # Add the braces and text to the scene and animate
        self.play(FadeIn(rect1), FadeIn(s1),
                  FadeIn(s2), FadeIn(s3), FadeIn(s4))
        self.play(GrowFromCenter(brace_width2), FadeIn(text_width2),
                  GrowFromCenter(brace_height2), FadeIn(text_height2), GrowFromCenter(brace_sqaure_width), FadeIn(brace_sqaure_width_text))
        self.play(Write(area.next_to(rect1, DOWN, buff=0.5), run_time=1))
        self.wait(0.5)
        self.play(ReplacementTransform(
            area, area_of_sqaure.next_to(rect1, DOWN, buff=0.5), run_time=0.8))
        self.wait(0.5)
        self.play(ReplacementTransform(area_of_sqaure,
                  area_of_sqaure_expanded.next_to(rect1, DOWN, buff=0.5), run_time=0.8))
        self.wait(0.5)
        newGroup = VGroup(rect1, s1, s2, s3, s4, brace_width2, text_width2, brace_height2,
                          text_height2, brace_sqaure_width, brace_sqaure_width_text, area_of_sqaure_expanded)
        # move the group to top left of teh screen and scale it down by 0.5
        self.play(newGroup.animate.scale(0.5).to_corner(UL))
        redraw = area_of_sqaure_expanded.copy()
        self.play(redraw.animate.move_to(ORIGIN).scale(2))
        self.play(ReplacementTransform(
            redraw, area_of_paper_used))
        self.wait(0.5)
        self.play(ReplacementTransform(
            area_of_paper_used, area_of_paper_used2))
        self.wait()
