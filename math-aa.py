from manim import *

class introduction(Scene):
    # Diplay the title Math AA - The “Open Problem”
    def construct(self):
        title = Text("The “Open Problem”", should_center=True).scale(1.5)
        self.play(Write(title))
        text2 = Text("Aidan, Asher, Caine, Vincent").scale(1)
        self.play(FadeIn(text2.shift(DOWN*1)))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(text2))

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
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


class defining_variables(Scene):
    # Display the title Maximum Volume and have a underline
    def construct(self):
        title = Text("Defining Variables", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


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
        self.wait(2)
        self.play(ShrinkToCenter(brace_width), FadeOut(text_width),
                  ShrinkToCenter(brace_height), FadeOut(text_height))
        self.play(FadeIn(s1), FadeIn(s2), FadeIn(s3), FadeIn(s4))
        self.play(GrowFromCenter(brace_width2), FadeIn(text_width2),
                  GrowFromCenter(brace_height2), FadeIn(text_height2), GrowFromCenter(brace_sqaure_width), FadeIn(brace_sqaure_width_text))
        self.wait(2)
        self.play(Write(volume.next_to(rect1, DOWN, buff=0.5)))
        self.wait(3)
        self.play(ShrinkToCenter(brace_width2), FadeOut(text_width2), ShrinkToCenter(brace_height2), FadeOut(
            text_height2), ShrinkToCenter(brace_sqaure_width), FadeOut(brace_sqaure_width_text), FadeOut(volume), FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4), FadeOut(rect1))


class differentiation(Scene):
    # Display the title Maximum Volume and have a underline
    def construct(self):
        title = MathTex("\\frac{dy}{dx}")
        underline = Line(
            start=title.get_left() + DOWN * 0.6,
            end=title.get_right() + DOWN * 0.6,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


class differentiation_test(Scene):
    def construct(self):
        eq1 = MathTex("V = x (42.0 - 2x)(59.4 - 2x)")
        eq2 = MathTex("V = 4x^3 - 202.6x^2 + 2494.8x")
        differentiationed = MathTex("V' = 12x^2 - 405.2x + 2494.8")
        e = MathTex("12x^2 - 405.2x + 2494.8 = 0")
        result = Tex("x = 8.0846 or 25.715 (n.a)")
        conclusion = MathTex("\\therefore V = 9027.96 cm^3")
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(eq1, eq2))
        self.wait(2)
        self.play(Transform(eq1, differentiationed))
        self.wait(2)
        self.play(Transform(eq1, e))
        self.wait(2)
        self.play(Transform(eq1, result))
        self.wait(3.5)
        self.play(Transform(eq1, conclusion))
        self.wait(3)
        self.play(FadeOut(eq1))


class first_derivative(Scene):
    # Display the title Maximum Volume and have a underline
    def construct(self):
        title = Text("First Derivative", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


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
        self.wait(4)
        self.play(ReplacementTransform(t0, t1))
        self.wait(4)
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
        self.wait(2)
        self.play(FadeOut(conclusion), FadeOut(text_group))


class second_derivative(Scene):
    # Display the title Maximum Volume and have a underline
    def construct(self):
        title = Text("Second Derivative", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


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
        self.wait(2)
        self.play(FadeOut(text_group))


class graphical(Scene):
    # Display the title Maximum Volume and have a underline
    def construct(self):
        title = Text("Graphical", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


class minimum_area(Scene):
    def construct(self):
        title = Text("Finding Minimum Area", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


class finding_minimum_area(Scene):
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
        self.wait()
        self.play(ReplacementTransform(
            area, area_of_sqaure.next_to(rect1, DOWN, buff=0.5), run_time=0.8))
        self.wait()
        self.play(ReplacementTransform(area_of_sqaure,
                  area_of_sqaure_expanded.next_to(rect1, DOWN, buff=0.5), run_time=0.8))
        self.wait()
        newGroup = VGroup(rect1, s1, s2, s3, s4, brace_width2, text_width2, brace_height2,
                          text_height2, brace_sqaure_width, brace_sqaure_width_text, area_of_sqaure_expanded)
        # move the group to top left of teh screen and scale it down by 0.5
        self.play(newGroup.animate.scale(0.5).to_corner(UL))
        redraw = area_of_sqaure_expanded.copy()
        self.play(redraw.animate.move_to(ORIGIN).scale(2))
        self.play(ReplacementTransform(
            redraw, area_of_paper_used))
        self.wait()
        self.play(ReplacementTransform(
            area_of_paper_used, area_of_paper_used2))
        self.wait()
        self.play(FadeOut(newGroup), FadeOut(area_of_paper_used2))


class optimum_area(Scene):
    def construct(self):
        title = Text("Finding Optimum Area", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


class differentiate_volume_with_area(Scene):
    # Display the title Maximum Volume and have a underline
    def construct(self):
        title = MathTex("\\frac{dv}{dA}")
        underline = Line(
            start=title.get_left() + DOWN * 0.6,
            end=title.get_right() + DOWN * 0.6,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


class differentiate_volume_with_area_test(Scene):
    def construct(self):
        eqn1 = MathTex("\\frac{dV}{dx}= 12x^2 - 405.6x + 2494.8")
        eqn2 = MathTex("A = (42.0)(59.4) - 4x^2")
        eqn3 = MathTex("A = 2494.8 - 4x^2")
        eqn4 = MathTex("\\therefore \\frac{dA}{dx} = -8x")
        eqn5 = MathTex("\\frac{dv}{dA} = -\\frac{12x^2 - 405.6x + 2494.8}{8x}")
        when = MathTex("When \\, \\frac{dv}{dA} = 0")
        eqn6 = MathTex("x = 8.08")

        self.play(Write(eqn1))
        self.wait(2)
        self.play(eqn1.animate.scale(0.5).to_corner(UL))
        self.play(Write(eqn2))
        self.wait(2)
        self.play(ReplacementTransform(eqn2, eqn3))
        self.wait(2)
        self.play(ReplacementTransform(eqn3, eqn4))
        self.wait(2)
        self.play(FadeOut(eqn4))
        self.play(eqn1.animate.scale(2).move_to(ORIGIN))
        self.play(ReplacementTransform(eqn1, eqn5))
        self.wait(2)
        self.play(eqn5.animate.shift(UP * 1.5), Write(when, run_time=1))
        self.wait(2)
        self.play(FadeOut(when), eqn5.animate.shift(DOWN * 1.5))
        self.play(ReplacementTransform(eqn5, eqn6))
        self.wait(2)
        self.play(FadeOut(eqn6))


class maximum_difference(Scene):
    def construct(self):
        title = Text("Maximum Difference Between V and A", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))


class maximum_difference_test(Scene):
    def construct(self):
        # Define the expression for s and its derivative
        inital = Tex("Let s be the difference between volume and area")
        s = MathTex("s = v - a")
        s2 = MathTex("s = (4x^3 - 202.6x^2 + 2494.8x) - (2494.8 - 4x^2)")
        eq1 = MathTex("\\frac{ds}{dx} = 12x^2 - 405.6x + 2494.8")
        eq2 = MathTex("When \\, \\frac{ds}{dx} = 0")
        eq3 = MathTex("12x^2 - 397.2x + 2494.8 = 0")
        eq4 = Tex("x = 8.425 or 24.67")
        eq5 = MathTex("\\frac{d^2s}{dx^2} =  24x - 397.2")
        when = MathTex("When \\, x = 8.425")
        when1 = MathTex("When \\, x = 24.67")
        eq7 = MathTex("\\frac{d^2s}{dx^2} = -195 < 0")
        eq72 = MathTex("\\frac{d^2s}{dx^2} = -194.88 > 0")

        eq8 = Tex("x = 8.425 is the maximum")
        eq82 = Tex("x = 24.67 is the minimum")
        conclusion = Tex("When x = 8.425 cm")
        conclusion2 = MathTex("V_{max} = 9016 cm^3")
        text_group = VGroup(conclusion, conclusion2).arrange(DOWN)

        self.play(Write(inital))
        self.wait(2)
        self.play(ReplacementTransform(inital,s))
        self.wait(2)
        self.play(ReplacementTransform(s, s2))
        self.wait(2)
        self.play(ReplacementTransform(s2, eq1))
        self.wait(2)
        self.play(eq1.animate.shift(UP * 1.5), Write(eq2, run_time=1))
        self.wait(2)
        self.play(FadeOut(eq2), eq1.animate.shift(DOWN * 1.5))
        self.play(ReplacementTransform(eq1, eq3))
        self.wait(2)
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(2)
        self.play(eq4.animate.shift(UP * 1.5))
        self.wait(1)
        self.play(Write(eq5))
        self.wait(2)
        self.play(ReplacementTransform(eq4,when.shift(UP * 1.5)),ReplacementTransform(eq5, eq7))
        self.wait(2)
        self.play(Write(eq8.shift(DOWN * 1.5)))
        self.wait(2)
        self.play(FadeOut(eq8),ReplacementTransform(when, when1.shift(UP * 1.5)), ReplacementTransform(eq7, eq72))
        self.wait(2)
        self.play(Write(eq82.shift(DOWN * 1.5)))
        self.wait(2)
        self.play(FadeOut(eq82), FadeOut(when1), FadeOut(eq72))
        self.wait(2)
        self.play(Write(text_group))
        self.wait(2)

class minimum_difference_two(Scene):
    def construct(self):
        title = Text("Minimum Difference between A and V", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))

class minimum_difference_two_test(Scene):
    def construct(self):
        inital = Tex("Let H be the difference between A and V")
        s = MathTex("H = A - V")
        s2 = MathTex("H =  2494.8 - 4x^2 - 4x^3 + 202.6x^2 - 2494.8x ")
        s3 = MathTex("H =  -4x^3 + 198.6x^2 - 2494.8x + 2494.8")
        eq1 = MathTex("\\frac{dH}{dx} = -12x^2 + 397.2x - 2494.8")
        when = MathTex("When \\, \\frac{dH}{dx} = 0")
        eq2 = MathTex("-12x^2 + 397.2x - 2494.8 = 0")
        eq3 = Tex("x = 8.425 or 24.67")
        eq4 = MathTex("\\frac{d^2H}{dx^2} = -24x + 397.2")
        when1 = MathTex("When \\, x = 8.425")
        when2 = MathTex("When \\, x = 24.67")
        eq5 = MathTex("\\frac{d^2H}{dx^2} = -195 < 0")
        eq6 = MathTex("\\frac{d^2H}{dx^2} = -194.88 > 0")
        eq7 = Tex("x = 8.425 is the maximum")
        eq8 = Tex("x = 24.67 is the minimum")
        conclusion = Tex("When x = 8.425 cm")
        conclusion2 = MathTex("H_{max} = 9016 cm^2")
        text_group = VGroup(conclusion, conclusion2).arrange(DOWN)

        self.play(Write(inital))
        self.wait(2)
        self.play(ReplacementTransform(inital,s))
        self.wait(2)
        self.play(ReplacementTransform(s, s2))
        self.wait(2)
        self.play(ReplacementTransform(s2, s3))
        self.wait(2)
        self.play(ReplacementTransform(s3, eq1))
        self.wait(2)
        self.play(eq1.animate.shift(UP * 1.5), Write(when, run_time=1))
        self.wait(2)
        self.play(FadeOut(when), eq1.animate.shift(DOWN * 1.5))
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2)
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(2)
        self.play(eq3.animate.shift(UP * 1.5))
        self.wait(1)
        self.play(Write(eq4))
        self.wait(2)
        self.play(ReplacementTransform(eq3,when1.shift(UP * 1.5)),ReplacementTransform(eq4, eq5))
        self.wait(2)
        self.play(Write(eq7.shift(DOWN * 1.5)))
        self.wait(2)
        self.play(FadeOut(eq7),ReplacementTransform(when1, when2.shift(UP * 1.5)), ReplacementTransform(eq5, eq6))
        self.wait(2)
        self.play(Write(eq8.shift(DOWN * 1.5)))
        self.wait(2)
        self.play(FadeOut(eq8), FadeOut(when2), FadeOut(eq6))
        self.wait(2)
        self.play(Write(text_group))
        self.wait(2)
        self.play(FadeOut(text_group))


class proposed_dimensions_yeet(Scene):
    def construct(self):
        title = Text("Proposed Dimensions", should_center=True).scale(1)
        underline = Line(
            start=title.get_left() + DOWN * 0.5,
            end=title.get_right() + DOWN * 0.5,
            stroke_width=4,
        )
        self.play(Write(title))
        self.play(Write(underline, run_time=3))
        self.wait()
        self.play(FadeOut(title), FadeOut(underline))

class proposed_dimensions(ThreeDScene):
    def construct(self):
        # Create a 3D Rectangle and brace its height width and length
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        brace = Brace(prismSmall, UP)
        self.play(Create(prismSmall), Create(brace))
        
