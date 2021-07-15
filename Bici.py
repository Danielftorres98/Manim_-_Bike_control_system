# Laura Manuela Castañeda Medina
# Daniel Felipe Torres Robles
# Proyecto Final Control

from big_ol_pile_of_manim_imports import *
# L1 signals

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class Anim_1_1(GraphScene):
    CONFIG = {
        "y_max" : 2,
        "y_min" : 0,
        "x_max" : 1,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 10,
        "graph_origin" : 0,
        "y_axis_label": None, 
        "x_axis_label": None,
    }
    
    def construct(self):
        Rueda_bici_trasera = RoundedRectangle(
                     color = WHITE,
                     height = 2.3,
                     width = 0.4,
                     corner_radius = 0.2
            )

        Linea1 = Line(1.5*UP,DOWN)
        Linea1.set_color(WHITE)

        Linea2 = Line(0.5*RIGHT,RIGHT)
        Linea2.set_color(WHITE)

        Circulo = Circle()
        Circulo.scale(0.25)
        Circulo.set_color(WHITE)

        Rueda_bici_trasera.scale(0.6)
        Rueda_bici_trasera.move_to(DOWN)
        Linea1.next_to(Rueda_bici_trasera, UP, buff=.01)
        Linea2.move_to(Linea1.get_center() + 0.4*DOWN)
        Circulo.next_to(Linea1, UP, buff=.01)

        Bici_trasera = VGroup(Linea1,Linea2,Circulo,Rueda_bici_trasera)
        Bici_trasera.move_to(3*RIGHT + 0.5*DOWN)

        Rueda_frontal_bici_trasera = RoundedRectangle(
                     color = WHITE,
                     height = 2.3,
                     width = 0.4,
                     corner_radius = 0.2
            )

        Rueda_frontal_bici_trasera.rotate(PI/2)
        Rueda_frontal_bici_trasera.set_fill(BLACK,opacity=1)

        Rueda_trasera_bici_trasera = RoundedRectangle(
                     color = WHITE,
                     height = 2.3,
                     width = 0.4,
                     corner_radius = 0.2
            )

        Rueda_trasera_bici_trasera.rotate(PI/2)
        Rueda_trasera_bici_trasera.set_fill(BLACK,opacity=1)

        Linea = Line(2*RIGHT,LEFT)
        Linea.set_color(WHITE)

        Rueda_frontal_bici_trasera.scale(0.6)
        Rueda_trasera_bici_trasera.scale(0.6)
        Rueda_frontal_bici_trasera.move_to(Linea.get_right())
        Rueda_trasera_bici_trasera.move_to(Linea.get_left())
        
        Bici_cenital = VGroup(Linea,Rueda_frontal_bici_trasera,Rueda_trasera_bici_trasera)
        Bici_cenital.move_to(3*LEFT)

        self.setup_axes1()
        self.setup_axes2()
        self.play(ShowCreation( Bici_trasera ),run_time = 2)
        self.play(ShowCreation( Bici_cenital ),run_time = 2)
        self.wait(2)

        
        Angulo = PI/2
        Delta_Angulo = -PI/64
        Punto_referencia_bici_trasera = Rueda_bici_trasera.get_center()+0.6*DOWN
        Contador_fotograma = 0

        while Contador_fotograma <= -( (1 / Delta_Angulo) * PI ):
            Bici_trasera.rotate( Angulo , about_point = Punto_referencia_bici_trasera )
            self.wait(0.1)
            Angulo = Delta_Angulo
            Contador_fotograma = Contador_fotograma + 1
    

        self.wait(2)

    def setup_axes1(self):
        GraphScene.setup_axes(self)
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        self.x_axis.set_color(WHITE)
        self.y_axis.set_color(WHITE)
        self.x_axis.scale(0.5)
        self.y_axis.scale(0.8)
        self.x_axis.move_to(2.7*DOWN + 3*RIGHT)
        self.y_axis.move_to(0.3*DOWN + 3*RIGHT)
        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                ]
            ],
            run_time=2
        )

    def setup_axes2(self):
        GraphScene.setup_axes(self)
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        self.x_axis.set_color(WHITE)
        self.y_axis.set_color(WHITE)
        self.x_axis.scale(0.7)
        self.y_axis.scale(0.5)
        self.x_axis.move_to(0*UP + 3*LEFT)
        self.y_axis.move_to(1.2*UP + 4.5*LEFT)
        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                ]
            ],
            run_time=2
        )
