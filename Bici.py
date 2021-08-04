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

        for x in range(-7, 8):
            for y in range(-5, 6):
                dot = Dot( point = (x, y, 0) )
                self.add(dot)

        Rueda_bici_trasera = RoundedRectangle(
                     color = BLUE,
                     height = 2.3,
                     width = 0.4,
                     corner_radius = 0.2
            )

        Rueda_bici_trasera.set_fill(BLUE, opacity=0.3)

        Linea_vertical_bici_trasera = Line( 1.5*UP,DOWN )
        Linea_vertical_bici_trasera.set_color( RED )

        Linea_horizontal_bici_trasera = Line( 0.5*RIGHT, RIGHT ) 
        Linea_horizontal_bici_trasera.set_color( RED )

        Silla_bici_trasera = RoundedRectangle(
                     color = GREY,
                     height = 2.3,
                     width = 0.4,
                     corner_radius = 0.2
        )

        Silla_bici_trasera.rotate(PI/2)
        Silla_bici_trasera.scale(0.25)
        Silla_bici_trasera.set_fill(GREY, opacity=0.3)


        Rueda_bici_trasera.scale(0.6)
        Rueda_bici_trasera.move_to(DOWN)
        Linea_vertical_bici_trasera.next_to( Rueda_bici_trasera, UP, buff=.01 )
        Linea_horizontal_bici_trasera.move_to( Linea_vertical_bici_trasera.get_center() + 0.4*DOWN )
        Silla_bici_trasera.next_to( Linea_vertical_bici_trasera, UP, buff=.01 )

        Bici_trasera = VGroup( Linea_vertical_bici_trasera, Linea_horizontal_bici_trasera, Silla_bici_trasera, Rueda_bici_trasera )
        Bici_trasera.move_to( 0.5*DOWN )



        self.setup_axes1()
        self.play( ShowCreation( Bici_trasera ), run_time = 0.1 )
        self.wait(2)
        

        Angulo_phi = PI/2
        Angulo_arco_bici_trasera = PI/2
        
        Delta_Angulo = -PI/180
        Punto_referencia_bici_trasera = Rueda_bici_trasera.get_center()+0.6*DOWN
        Contador_fotograma = 0

        Angulo_bici_trasera = DecimalNumber(0, num_decimal_places=2, include_sign=False)
        Angulo_bici_trasera.add_updater(lambda d: d.set_value( Angulo_arco_bici_trasera * 180 / PI) )
        Angulo_bici_trasera.next_to(Silla_bici_trasera, UP, buff=1)

        while Contador_fotograma <= -( (1 / Delta_Angulo) * PI ):

            Bici_trasera.rotate( Angulo_phi , about_point = Punto_referencia_bici_trasera )
            self.wait(0.1)
            Angulo_phi = Delta_Angulo
            Contador_fotograma = Contador_fotograma + 1

            Angulo_bici_trasera.add_updater( lambda d: d.set_value( Angulo_arco_bici_trasera * 180 / PI ) )
            
            Arco_bici_trasera = Arc( arc_center = Punto_referencia_bici_trasera , radius = 3, start_angle = PI/2, angle = Angulo_arco_bici_trasera )

            Angulo_arco_bici_trasera = Angulo_arco_bici_trasera + Delta_Angulo
            
            self.play( ShowCreation( Angulo_bici_trasera ), ShowCreation( Arco_bici_trasera ), run_time = 0.1)
            self.play( FadeOut( Angulo_bici_trasera ), FadeOut( Arco_bici_trasera ), run_time = 0.1)
    
        self.wait(2)

    def setup_axes1(self):
        GraphScene.setup_axes(self)
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        self.x_axis.set_color(WHITE)
        self.y_axis.set_color(WHITE)
        self.x_axis.scale(0.5)
        self.y_axis.scale(0.8)
        self.x_axis.move_to(2.7*DOWN)
        self.y_axis.move_to(0.3*DOWN)
        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                ]
            ],
            run_time=0.1
        )