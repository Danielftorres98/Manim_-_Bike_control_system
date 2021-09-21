# Laura Manuela Castañeda Medina
# Daniel Felipe Torres Robles
# Proyecto Final Control

from big_ol_pile_of_manim_imports import *
from scipy import signal as sp

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class Anim_1_1(GraphScene):
    
    def construct(self):
        axis_config = {
            "y_max" : 4,
            "y_min" : -4,
            "x_max" : 4,
            "x_min" : -4,
            }
        
        Rueda1 = Circle(
                     color = BLUE,
                     radius = 1.2
            )

        Rueda2 = Circle(
                     color = BLUE,
                     radius = 1
            )

        Rueda1.set_fill(BLUE, opacity=0.3)
        Rueda2.set_fill(BLUE, opacity=0.3)
        
        Rueda1.move_to(1.5*DOWN + 2.6*LEFT)
        Rueda2.move_to(1.6*DOWN + 1.3*RIGHT)

        Linea_horizontal = Line( start=LEFT,end=0.5*RIGHT )
        Linea_horizontal.set_color( RED )

        Linea1 = Line( start=np.array([-1, 0, 0]),end=np.array([-0.7, -1.5, 0]) ) 
        Linea1.set_color( RED )

        Linea2 = Line( start=LEFT,end=1.3*DOWN + 2.3*LEFT ) 
        Linea2.set_color( RED )

        Linea3 = Line( start=1.5*DOWN + 0.7*LEFT,end=1.3*DOWN + 2.3*LEFT ) 
        Linea3.set_color( RED )

        Linea4 = Line( start=0.5*RIGHT,end=0.4*DOWN + 0.65*RIGHT ) 
        Linea4.set_color( RED )

        Linea5 = Line( start=0.4*DOWN + 0.65*RIGHT,end=1.5*DOWN + 0.7*LEFT ) 
        Linea5.set_color( RED )

        Linea6 = Line( start=0.4*UP + 0.35*RIGHT,end= 1.4*DOWN + 1.025*RIGHT )
        Linea6.set_color( RED )

        Lineas = VGroup( Linea_horizontal, Linea1, Linea2, Linea3, Linea4, Linea5, Linea6 )
        Lineas.scale(1.2)

        Bici = VGroup( Rueda1, Rueda2, Lineas)

        self.play(ShowCreation(Bici),run_time = 2)
        self.wait(2)


class Anim_1_2(ThreeDScene):
    
    def construct(self):
        axis_config = {
            "y_max" : 0,
            "y_min" : -4,
            "x_max" : 4,
            "x_min" : 0,
            "z_max" : 3,
            "z_min" : 0,
            }
        
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 80*DEGREES, theta = -40*DEGREES, distance = 6)

        Rueda1 = Circle(
                     color = BLUE,
                     radius = 1.2
            )

        Rueda2 = Circle(
                     color = BLUE,
                     radius = 1
            )

        Rueda1.set_fill(BLUE, opacity=0.3)
        Rueda2.set_fill(BLUE, opacity=0.3)
        
        Rueda1.move_to(1.5*DOWN + 2.6*LEFT)
        Rueda2.move_to(1.6*DOWN + 1.3*RIGHT)

        Linea_horizontal = Line( start=LEFT,end=0.5*RIGHT )
        Linea_horizontal.set_color( RED )

        Linea1 = Line( start=np.array([-1, 0, 0]),end=np.array([-0.7, -1.5, 0]) ) 
        Linea1.set_color( RED )

        Linea2 = Line( start=LEFT,end=1.3*DOWN + 2.3*LEFT ) 
        Linea2.set_color( RED )

        Linea3 = Line( start=1.5*DOWN + 0.7*LEFT,end=1.3*DOWN + 2.3*LEFT ) 
        Linea3.set_color( RED )

        Linea4 = Line( start=0.5*RIGHT,end=0.4*DOWN + 0.65*RIGHT ) 
        Linea4.set_color( RED )

        Linea5 = Line( start=0.4*DOWN + 0.65*RIGHT,end=1.5*DOWN + 0.7*LEFT ) 
        Linea5.set_color( RED )

        Linea6 = Line( start=0.4*UP + 0.35*RIGHT,end= 1.4*DOWN + 1.025*RIGHT )
        Linea6.set_color( RED )

        Lineas = VGroup( Linea_horizontal, Linea1, Linea2, Linea3, Linea4, Linea5, Linea6 )
        Lineas.scale(1.2)

        Bici = VGroup( Rueda1, Rueda2, Lineas)

        Bici.rotate(PI/2, axis = RIGHT)

        self.play(ShowCreation(axes),run_time = 2)
        self.play(ShowCreation(Bici),run_time = 2)
        self.wait(2)

        Angulo_phi = PI/2
        Angulo_arco_bici_trasera = PI/2
        
        Delta_Angulo = -PI/3
        Punto_referencia_bici_trasera = Bici.get_center() + 1.5*IN
        Contador_fotograma = 0

        Angulo_bici_trasera = DecimalNumber(0, num_decimal_places=2, include_sign=False)
        Angulo_bici_trasera.add_updater(lambda d: d.set_value( Angulo_arco_bici_trasera * 180 / PI) )
        Angulo_bici_trasera.next_to(Linea6, UP, buff=1)

        while Contador_fotograma <= -( (1 / Delta_Angulo) * PI ):

            Bici.rotate( Angulo_phi , axis = RIGHT, about_point = Punto_referencia_bici_trasera)
            self.wait(0.1)
            Angulo_phi = Delta_Angulo
            Contador_fotograma = Contador_fotograma + 1

            Angulo_bici_trasera.add_updater( lambda d: d.set_value( (Angulo_arco_bici_trasera * 180 / PI) + 1) )
            
            Arco_bici_trasera = Arc( arc_center = Punto_referencia_bici_trasera , radius = 3, start_angle = PI/2, angle = Angulo_arco_bici_trasera )

            Angulo_arco_bici_trasera = Angulo_arco_bici_trasera + Delta_Angulo
            
            self.play( ShowCreation( Angulo_bici_trasera ), ShowCreation( Arco_bici_trasera ), run_time = 0.1)
            self.play( FadeOut( Angulo_bici_trasera ), FadeOut( Arco_bici_trasera ), run_time = 0.1)
    
        self.wait(2)
