from typing import Tuple,List

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines


class Canvas:
    """A class for drawing on a scene."""

    def __init__(self,ax):
        self.__ax = ax

    def draw_arc(self,xy,width,height,angle=0.0,theta1=0.0,theta2=360.0):
        """
        Draws an elliptical arc, i.e. a segment of an ellipse.

        Parameters
        ----------
        xy : (float,float)
            The center of the ellipse.
        width : float
            The length of the horizontal axis.
        height : float
            The length of the vertical axis.
        angle : float
            Rotation of the ellipse in degrees (counterclockwise).
        theta1, theta2 : float, default: 0, 360
            Starting and ending angles of the arc in degrees. These values
            are relative to *angle*, e.g. if *angle* is 45 and *theta1* is 90
            the absolute starting *angle* is `135`.
            Default theta1 = 0, theta2 = 360, i.e. a complete ellipse.
            The arc is drawn in the counterclockwise direction.
            Angles greater than or equal to 360, or smaller than 0, are
            represented by an equivalent angle in the range [0, 360), by
            taking the input value mod 360.
        """
        self.__ax.add_artist(patches.Arc(xy,width,height,angle,theta1,theta2,color='midnightblue', linewidth=1, linestyle='-'))

    def draw_line(self,p1,p2):
        """
        Draws a segment connecting p1 and p2.

        Parameters
        ----------
        p1 : (float,float)
            One end of the segment.
        p1 : (float,float)
            Other end of the segment.
        """
        self.__ax.add_artist(lines.Line2D([p1[0],p2[0]],[p1[1],p2[1]],color='midnightblue', linewidth=1, linestyle='-'))


class Drawable:
    """Base class for objects that can draw themselves using *Canvas*."""

    def bounding_box(self) -> Tuple[Tuple[float,float],Tuple[float,float]]:
        """Returns a pair of points that correspond to the opposing corners of a rectangle area in which this object will draw itself."""
        raise NotImplementedError()
    
  
    def draw(self,canvas:Canvas):
        """Draws this object using *canvas*."""
        raise NotImplementedError()
    

class Visualiser:
    """Displays a scene with drawable objects in a dedicated window."""

    def __init__(self, drawables:List[Drawable] = []):
        # drawables registry
        self.__drawables = drawables.copy()
        # figure
        self.__fig, self.__ax = plt.subplots()
        self.__fig.canvas.manager.set_window_title('Visualiser')
        # listen to close event
        self.__fig.is_open = False
        def __on_close(event):
            event.canvas.figure.is_open = False
        self.__fig.canvas.mpl_connect('close_event', __on_close )
        # make sure our window is on the screen and drawn
        self.__update_scene()
        plt.show(block=False)
        plt.pause(.1)

    def is_open(self) -> bool:
        """
        Whether the visualiser is open or not.
        """
        return self.__fig.is_open

    def add(self,drawable:Drawable,refresh:bool=True):
        """
        Adds *drawable* to this visualiser.

        Parameters
        ----------
        drawable : Drawable
             The drawable object to add to the scene
        refresh : bool, default: True
             Whether to refresh the visualiser (see method *refresh*)
        """
        self.__drawables.append(drawable)
        if refresh:
            self.refresh()

    def remove(self,drawable:Drawable,refresh:bool=True):
        """
        Removes *drawable* to this visualiser.

        Parameters
        ----------
        drawable : Drawable
             The drawable object to remove from the scene
        refresh : bool, default: True
             Whether to refresh the visualiser (see method *refresh*)
        """
        try:
            self.__drawables.remove(drawable)
            if refresh:
                self.refresh()
        except ValueError:
            pass

    def __update_scene(self):
        self.__ax.clear()
        # axes
        x_min = y_min = -1
        x_max = y_max =  1
        for d in self.__drawables:
            (p1_x,p1_y),(p2_x,p2_y) = d.bounding_box()
            x_min = min(x_min,p1_x,p2_x)
            y_min = min(y_min,p1_y,p2_y)
            x_max = max(x_max,p1_x,p2_x)
            y_max = max(y_max,p1_y,p2_y)
        self.__ax.set_xlim([x_min,x_max])
        self.__ax.set_ylim([y_min,y_max])
        self.__ax.set_aspect('equal')
        self.__ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        for drawable in self.__drawables:
            canvas = Canvas(self.__ax)
            drawable.draw(canvas)

    def refresh(self,pause:float=0.01):
        """
        Updates the figure displayed by the visualiser and then run the GUI event loop for *pause* seconds.
        """
        self.__update_scene()
        plt.pause(pause)

    def pause(self,interval:float):
        """
        Pauses to run the GUI event loop for *interval* seconds (does not updates the figure if there are changes pending, use *refresh* instead).
        """
        plt.pause(interval)

    def wait_close(self):
        """
        Suspends the current execution until the visualiser window is manually closed by the user.
        """
        plt.show()

    def close(self):
        """
        Close the visualiser.
        """
        plt.close(self.__fig)
