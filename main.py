from manimlib import *
import numpy as n
import math


class TileCoding(Scene):
    def construct(self):
        
        axis_config={
                "unit_size":1,
                "stroke_width":3,
                "stroke_color":PINK,
               
            }
        
        axis_config_2={
                "unit_size":1,
                "stroke_width":7,
                "stroke_color":WHITE,
               
            }
        grid = NumberPlane((-10, 10), (-10, 10),axis_config=axis_config, faded_line_ratio=0 )
        grid_2 = NumberPlane((-10, 10), (-10, 10),axis_config=axis_config_2, faded_line_ratio=0 )
        grid_2.init_colors()
        grid_2.generate_target()
        grid_2.target.shift(0.5*UP+0.5*RIGHT)
        self.play(FadeIn(grid))
        self.wait(0.5)
        point = Dot(point=(2.75,2.75,0), radius=0.05)
        feature_vec_repr = Square(side_length=0.5, color=PINK, opacity=0.6)
        feature_vec_repr.set_fill(PINK, opacity=0.6)
        feature_vec_repr.shift(2.75*UP+2.75*RIGHT)
        self.play(FadeIn(grid_2, run_time=0),MoveToTarget(grid_2, run_time=2))
        self.play(FadeIn(point))
        
        self.play(FadeIn(feature_vec_repr))

class StateTransition(Scene):
    def get_y( self):
        y = math.cos(3 * (self.x_val + math.pi / 2))
        return  y
    def get_y_str(self):
        y = self.get_y()
        return "{:.2f}".format(y)
    def get_g_force(self):
        return -.0025 * math.cos(3 * self.x_val)
    def get_g_force_str(self):
        f = self.get_g_force()
        return "{:.5f}".format(f)
    def get_x_hat_from_do_move(self, F):
        self.x_hat_val =  self.x_hat_val + .001 * \
            F - .0025 * math.cos(3 * self.x_val)
        return self.get_x_hat_str()
    def get_x_hat_str(self):
        return "{:.3f}".format(self.x_hat_val)
    def get_x_val(self):
        return "{:.3f}".format(self.x_val)
    def update_and_return_x_val(self):
        self.x_val = self.x_val + self.x_hat_val
        return self.get_x_val()
    
    def construct(self):
        x = "x"
        self.x_val = 0.2
        x_hat = r'\hat{x}'
        self.x_hat_val = 0.01
        left_arrow = r"\leftarrow"
        y = ["y", "(", x, ")"]
        g_force = ["\hat{gravity}","(", x, ")"]

        x_h_formula = [x_hat, "+", "0.001","F", "+", *g_force]
        lines = Group(
            Tex(x , "=", str(self.x_val),r"\,\,\,\,\,\,",  x_hat, "=", str(self.x_hat_val) ),
            Tex(*y, "=", self.get_y_str(),r"\,\,\,\,\,\,", *g_force, "=", self.get_g_force_str()),
            Tex(r"M\!ove\,\,right:\,F=1", isolate="F"),
            Tex(r"\downarrow"),
            Tex(x_hat, left_arrow,*x_h_formula, isolate=["(",")","F"]),
            Tex(x_hat, "=",self.get_x_hat_str(),"+", str(0.001*1), self.get_g_force_str()),
            Tex(x_hat, "=", self.get_x_hat_from_do_move(1)),
            Tex(x, r"\leftarrow", x, "+", x_hat),
            Tex(x, "=", str(self.x_val), "+", self.get_x_hat_str()),
            Tex(x, "=", self.update_and_return_x_val()),
            Tex(x , "=", self.get_x_val(),r"\,\,\,\,\,\,",  x_hat, "=", self.get_x_hat_str() ),
            Tex(*y, "=", self.get_y_str(),r"\,\,\,\,\,\,", *g_force, "=", self.get_g_force_str()),
            
        )
        
    
        lines.arrange(DOWN, buff=SMALL_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
            x: BLUE,
            y[0]: BLUE_E,
            "str(self.get_g_force_str())":BLUE_B,
            g_force[0]:BLUE_B,
            x_hat: GREEN,
            "F":PINK,
            })
        #Hard coded, has to be changed if x_val is changed
        lines[5].set_color_by_tex_to_color_map({
            "0.001":PINK,
            "0.010":GREEN,
            "-0.00206":BLUE_B
        })
        lines[8].set_color_by_tex_to_color_map({
            "0.2":BLUE,
            "0.009":GREEN,
        })
        play_kw = {"run_time": 1.2}
        display_kw = {"run_time": 0.8}
        self.play(FadeIn(lines[0], **display_kw))
        
        self.wait(1)
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
            ),
            **play_kw
        )
        self.wait(1)
        self.play(FadeIn(lines[2], **display_kw),
        FadeIn(lines[3], **display_kw))
        self.wait(1)
        self.play(FadeIn(lines[4], **display_kw))
        self.wait(1)
        
        mapping = {"F":"0.001", g_force[0]:"-0.00206",
        x_hat:"0.010"}
        self.play(
            TransformMatchingTex(
                lines[4].copy(), lines[5],
            ),
            **play_kw)
        self.wait(0.5)
        self.play(
            TransformMatchingTex(
                lines[5].copy(), lines[6],
            ),
            **play_kw)
        self.wait(0.5)
        self.play(FadeIn(lines[7], **display_kw))
        self.wait(0.5)
        self.play(
            TransformMatchingTex(
                lines[7].copy(), lines[8],
            ),
            **play_kw)
        self.play(
            TransformMatchingTex(
                lines[8].copy(), lines[9],
            ),
            **play_kw)
        self.wait(0.3)
        self.play(
            TransformMatchingTex(
                lines[9].copy(), lines[10],
            ),
            TransformMatchingTex(
                lines[6].copy(), lines[10],
            ),
            **play_kw)
        self.wait(0.3)
        self.play(
            TransformMatchingTex(
                lines[10].copy(), lines[11],
            ),
            **play_kw)
        self.wait(1)
        
        
        