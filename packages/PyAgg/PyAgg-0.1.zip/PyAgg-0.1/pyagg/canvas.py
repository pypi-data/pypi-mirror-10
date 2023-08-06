"""
Defines the PyAgg Canvas class, where most of the PyAgg functinoality is defined. 
"""

##############################
# Startup and imports

# Import future stuff
from __future__ import division

# Import dependencies
import PIL, PIL.Image, PIL.ImageTk, PIL.ImageDraw, PIL.ImageFont

# Import builtins
import sys, os
import Tkinter as tk
import struct
import itertools
import random
import traceback
import warnings

# Import submodules
PYAGGFOLDER = os.path.split(__file__)[0]
from . import affine
from . import units
from . import bboxhelper

##############################
# Determine OS and bitsystem
OSSYSTEM = {"win32":"windows",
             "darwin":"mac",
             "linux":"linux",
             "linux2":"linux"}[sys.platform]
PYVERSION = sys.version[:3]
if sys.maxsize == 9223372036854775807: PYBITS = "64"
else: PYBITS = "32"

##############################
# Retrieve system fonts
FONTNAMES = dict()
FONTFILENAMES = dict()
try:
    sys.path.insert(0, PYAGGFOLDER)
    from fontTools.ttLib import TTFont
    SYSFONTFOLDERS = dict([("windows","C:/Windows/Fonts/"),
                           ("mac", "/Library/Fonts/"),
                           ("linux", "/usr/share/fonts/truetype/")])
    FONTFILENAMES = dict([(filename.lower(), os.path.join(dirpath, filename))
                           for dirpath,dirnames,filenames in os.walk(SYSFONTFOLDERS[OSSYSTEM])
                          for filename in filenames
                          if filename.endswith(".ttf")])
    for filename in FONTFILENAMES.keys():
        metadata = TTFont(FONTFILENAMES[filename]).get("name")
        for info in metadata.names:
            if info.nameID == 4: # font family name with optional bold/italics
                if info.string.startswith("\x00"):
                    # somehow the font string has weird byte data in first position and between each character
                    fontname = info.string[1::2]
                else:
                    fontname = info.string
                break
        FONTNAMES.update([(fontname.lower(), filename)])
except:
    msg = "\n".join(["%s" % traceback.format_exc(),
                     "-----------------",
                     "Due to an error, could not determine the font names available for your system.",
                     "Using font names when setting text font will therefore not work.",
                     "Instead you must specify the font filename or filepath for it to work.",
                     "-----------------"
                     ])
    warnings.warn(msg)
finally:
    sys.path = sys.path[1:] # remove previously added fontTools path

##############################
# create function for getting fonts
def _get_fontpath(font):
    font = font.lower()
    # first try to get human readable name from custom list
    if FONTNAMES.get(font):
        return os.path.join(SYSFONTFOLDERS[OSSYSTEM], FONTFILENAMES[FONTNAMES[font]])
    # then try to get from custom font filepath
    elif os.path.lexists(font):
        return font
    # or try to get from filename in font folder
    elif FONTFILENAMES.get(font):
        return FONTFILENAMES[font]
    # raise error if hasnt succeeded yet
    raise Exception("Could not find the font specified. Font must be either a human-readable name, a filename with extension in the default font folder, or a full path to the font file location")

##############################     
# Import correct AGG binaries
try:
    if OSSYSTEM == "windows":
        if PYBITS == "32":
            if PYVERSION == "2.6":
                try: from .precompiled.win.bit32.py26 import aggdraw
                except:
                    sys.path.insert(0, PYAGGFOLDER+"/precompiled/win/bit32/py26")
                    import aggdraw
                    sys.path = sys.path[1:] # remove previously added aggdraw path
            elif PYVERSION == "2.7":
                try: from .precompiled.win.bit32.py27 import aggdraw
                except:
                    sys.path.insert(0, PYAGGFOLDER+"/precompiled/win/bit32/py27")
                    import aggdraw
                    sys.path = sys.path[1:] # remove previously added aggdraw path
        elif PYBITS == "64":
            if PYVERSION == "2.6":
                raise ImportError("Currently no Windows precompilation for 64-bit Py26")
            elif PYVERSION == "2.7":
                try: from .precompiled.win.bit64.py27 import aggdraw
                except:
                    sys.path.insert(0, PYAGGFOLDER+"/precompiled/win/bit64/py27")
                    import aggdraw
                    sys.path = sys.path[1:] # remove previously added aggdraw path
    elif OSSYSTEM == "mac":
        if PYBITS == "32":
            raise ImportError("Currently no Mac precompilation for 32-bit Py26 or Py27")
        elif PYBITS == "64":
            if PYVERSION == "2.6":
                raise ImportError("Currently no Mac precompilation for 64-bit Py26")
            elif PYVERSION == "2.7":
                try: from .precompiled.mac.bit64.py27 import aggdraw
                except:
                    sys.path.insert(0, PYAGGFOLDER+"/precompiled/mac/bit64/py27")
                    import aggdraw
                    sys.path = sys.path[1:] # remove previously added aggdraw path
    elif OSSYSTEM == "linux":
        raise ImportError("Currently no Linux precompilation for any version or bit system")
except ImportError:
    import aggdraw # in case user has compiled a working aggdraw version on their own






##############################
# Some convenience functions

def _grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=None, *args)

def _pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)





##############################
# Main class

class Canvas:
    """
    An image that knows how to draw on itself and keep track of its
    coordinate system.

    Attributes:

    - *width*:
        Pixel width of canvas image
    - *height*:
        Pixel height of canvas image
    - *ppi*:
        Pixels per inch. Used to calculate pixels needed for real world sizes. 
    - *default_unit*:
        How to interpret sizes given as just a number.
    - *coordspace_bbox*:
        Bounding box of the canvas coordinate system as a list 
        containing 4 floats [xmin, ymin, xmax, ymax].
    - *coordspace_width*:
        Width of the canvas coordinate system, as the difference
        between xmin and xmax. 
    - *coordspace_height*:
        Height of the canvas coordinate system, as the difference
        between ymin and ymax. 
    - *coordspace_units*:
        The number of coordinate space units per 1 cm screen width. 
    - *coordspace_transform*:
        A list of 6 floats representing the affine transform
        coefficients used to transform input coordinates to the drawing coordinate system. 
    """
    def __init__(self, width, height, background=None, mode="RGBA", ppi=300):
        """
        Creates a new blank canvas image. 

        Parameters:
        
        - *width*:
            Width of the canvas image. Value can be an integer for number of
            pixels. Value can also be any valid string size: in, cm, or mm. In the latter
            case uses the ppi setting (pixels per inch) to calculate the
            pixel width/height equivalent, because pixels are distance agnostic.
        - *height*:
            Height of the canvas image. Same values as width. 
        - *background* (optional):
            The color of the background image.
            Value should be an RGB or RGB tuple, or an aggdraw color name that matches the
            image mode. Defaults to None (transparent). 
        - *mode* (optional):
            any of PIL's image modes, typically 'RGBA' (default) or 'RGB'. 
        - *ppi* (optional):
            Pixels per inch. Defaults to publication quality of 300. Its only effect
            is that it calculates the correct pixels whenever you use a real world
            size such as cm, mm, in, or pt. When you use pixel units directly or %, the ppi has
            no effect. This means that if ppi matters to you, you should initiate
            the canvas width and height using real world sizes, and draw all sizes using
            real world sizes as well. Ppi should only be set at initiation time.
        """
        # unless specified, interpret width and height as pixels
        width = units.parse_dist(width, default_unit="px", ppi=ppi)
        height = units.parse_dist(height, default_unit="px", ppi=ppi)
        width,height = int(round(width)),int(round(height))
        # create image
        self.img = PIL.Image.new(mode, (width, height), background)
        # create drawer
        self.drawer = aggdraw.Draw(self.img)
        # remember info
        self.background = background
        self.ppi = ppi
        # by default, interpret all sizes in % of width
        self.default_unit = "%w"
        # by default, interpret all coordinates in pixel space
        self.pixel_space()

    @property
    def width(self):
        return self.drawer.size[0]

    @property
    def height(self):
        return self.drawer.size[1]








    # Image operations

    def resize(self, width, height, lock_ratio=False):
        """
        Resize canvas image to new width and height in pixels or other units,
        and the coordinate system will follow, so that each corner
        in the old image is equivalent to each corner in the new image.

        Parameters:

        - *width*:
            Width of the new image. Can be specified with any unit with a string representation. Otherwise defaults to pixels. 
        - *height*:
            Height of the new image. Can be specified with any unit with a string representation. Otherwise defaults to pixels. 
        - *lock_ratio* (optional):
            Whether to modify the given sizes to preserve the
            width/height ratio of the original image. Default is False. 

        Returns:
        
        - In addition to changing the original instance, this method returns
            the new instance to allow for linked method calls. 
        """
        # Resize image
        self.drawer.flush()
        width = units.parse_dist(width,
                                 ppi=self.ppi,
                                 default_unit="px",
                                 canvassize=[self.width,self.height])
        height = units.parse_dist(height,
                                 ppi=self.ppi,
                                 default_unit="px",
                                 canvassize=[self.width,self.height])
        self.img = self.img.resize((width, height), PIL.Image.ANTIALIAS)
        self.update_drawer_img()
        # Then update coordspace to match the new image dimensions
        self.custom_space(*self.coordspace_bbox, lock_ratio=lock_ratio)
        return self

    def rotate(self, degrees):
        """
        Rotate the canvas image in degree angles,
        and the coordinate system will follow.

        Parameters:

        - *degrees*: Degree angles to rotate. 0 degrees faces upwards and increases
            clockwise.
            
        Returns:
        
        - In addition to changing the original instance, this method returns
            the new instance to allow for linked method calls. 
        """
        self.drawer.flush()
        self.img = self.img.rotate(degrees, PIL.Image.BICUBIC)
        self.update_drawer_img()
        return self

##    def skew(self):
##        """
##        Skew the canvas image in pixels,
##        and the coordinate system will follow.
##        """
##        pass

    def flip(self, xflip=True, yflip=False):
        """
        Flip the canvas image horizontally or vertically (center-anchored),
        and the coordinate system will follow.

        Parameters:

        - *xflip* (optional): Flips the image horizontally if set to True. Default is True. 
        - *yflip* (optional): Flips the image vertically if set to True. Default is False. 

        Returns:
        
        - In addition to changing the original instance, this method returns
            the new instance to allow for linked method calls. 
        """
        self.drawer.flush()
        img = self.img
        if xflip: img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        if yflip: img = img.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self.img = img
        self.update_drawer_img()
        return self

    def move(self, xmove, ymove):
        """
        Move/offset the canvas image in pixels or other units,
        and the coordinate system will follow.

        Parameters:

        - *xmove*: Moves/offsets the image horizontally.
            Can be specified with any unit with a string representation. Otherwise defaults to pixels. 
        - *ymove*: Moves/offsets the image vertically.
            Can be specified with any unit with a string representation. Otherwise defaults to pixels. 

        Returns:
        
        - In addition to changing the original instance, this method returns
            the new instance to allow for linked method calls.
        """
        # convert units to pixels
        xmove = units.parse_dist(xmove,
                                 ppi=self.ppi,
                                 default_unit="px",
                                 canvassize=[self.width,self.height])
        ymove = units.parse_dist(ymove,
                                 ppi=self.ppi,
                                 default_unit="px",
                                 canvassize=[self.width,self.height])
        # paste self on blank at offset pixel coords
        self.drawer.flush()
        blank = PIL.Image.new(self.img.mode, self.img.size, None)
        blank.paste(self.img, (xmove, ymove))
        self.img = blank
        # similarly move the drawing transform
        # by converting pixels to coord distances
        xmove,ymove = self.pixel2coord_dist(xmove, ymove)
        orig = affine.Affine(*self.coordspace_transform)
        moved = orig * affine.Affine.translate(xmove,ymove)
        self.drawer = aggdraw.Draw(self.img)
        self.drawer.settransform(moved.coefficients)
        # remember the new coordinate extents and affine matrix
        self.coordspace_transform = moved.coefficients
        # offset bbox
        x1,y1,x2,y2 = 0,0,self.width,self.height
        x1,y1 = self.pixel2coord(x1, y1)
        x2,y2 = self.pixel2coord(x2, y2)
        self.coordspace_bbox = [x1,y1,x2,y2]
        return self

    def paste(self, image, xy=(0,0)):
        """
        Paste the northwest corner of a PIL image
        onto a given location in the Canvas.

        Parameters:

        - *image*: PIL image to paste.
        - *xy*: An xy point tuple of the location to paste the northwest corner of the image.
            Can be specified with any unit with a string representation. Otherwise defaults to pixels.

        Returns:
        
        - In addition to changing the original instance, this method returns
            the new instance to allow for linked method calls.
        """
        # Parse xy location from any type of unit to pixels
        x,y = xy
        x = units.parse_dist(x,
                             ppi=self.ppi,
                             default_unit="px",
                             canvassize=[self.width,self.height])
        y = units.parse_dist(y,
                             ppi=self.ppi,
                             default_unit="px",
                             canvassize=[self.width,self.height])
        xy = (x,y)
        # Need more options, eg anchor point, and coordinate xy
        self.drawer.flush()
        if isinstance(image, Canvas): image = image.img
        if image.mode == "RGBA":
            self.img.paste(image, xy, image) # paste using self as transparency mask
        else: self.img.paste(image, xy)
        self.update_drawer_img()
        return self

##    def crop(self, xmin, ymin, xmax, ymax):
##        """
##        Crop the canvas image to a bounding box defined in pixel coordinates,
##        and the coordinate system will follow.
##
##        Parameters:
##        
##        - xmin: The lower bound of the x-axis after the crop.
##        - ymin: The lower bound of the y-axis after the crop.
##        - xmax: The higher bound of the x-axis after the crop.
##        - ymax: The higher bound of the y-axis after the crop.
##
##        Returns:
##        
##        - In addition to changing the original instance, this method returns
##            the new instance to allow for linked method calls.
##        """
##        ### NEW: JUST DO SAME ROUTINE AS "move" AND "resize"
##        # HALFWAY THROUGH USING COORDINATES
##        # MAYBE GO BACK TO PIXELS ONLY
##        # NOTE: Also need to update drawing transform to match the new image dimensions
##        self.drawer.flush()
##
##        # convert bbox to pixel positions
##        (xmin, ymin), (xmax, ymax) = [self.coord2pixel(xmin, ymin),
##                                      self.coord2pixel(xmax, ymax)]
##
##        # ensure pixels are listed in correct left/right top/bottom order
##        xleft, ytop, xright, ybottom = xmin, ymin, xmax, ymax
##        if xleft > xright: xleft,xright = xright,xleft
##        if ytop > ybottom: ytop,ybottom = ybottom,ytop
##
##        # constrain aspect ratio, maybe by applying a new zoom_transform and reading coordbbox
##        # ...
##
##        # do the cropping
##        pixel_bbox = map(int, [xleft, ytop, xright, ybottom])
##        self.img = self.img.crop(pixel_bbox)
##        self.update_drawer_img()
##        return self

    def update_drawer_img(self):
        """
        Updates any image changes to the drawer, and reapplies the transform to the new
        image size. Mostly used internally, but can be useful if you apply any PIL operations
        directly to the canvas image (the .img attribute). 
        """
        self.drawer = aggdraw.Draw(self.img)
        self.drawer.settransform(self.coordspace_transform)








    # Color quality

##    def brightness():
##        pass
##
##    def contrast():
##        pass
##
##    def transparency(self, alpha):
##        self.drawer.flush()
##        blank = PIL.Image.new(self.img.mode, self.img.size, None)
##        self.img = blank.paste(self.img, (0,0), alpha)
##        self.update_drawer_img()
##        return self
##
##    def color_tint():
##        # add rgb color to each pixel
##        pass










    # Layout

##    def insert_graph(self, image, bbox, xaxis, yaxis):
##        # maybe by creating and drawing on images as subplots,
##        # and then passing them in as figures that draw their
##        # own coordinate axes if specified and then paste themself.
##        # ... 
##        pass

    @property
    def coordspace_width(self):
        xleft,ytop,xright,ybottom = self.coordspace_bbox
        x2x = (xleft,xright)
        xwidth = max(x2x)-min(x2x)
        return xwidth

    @property
    def coordspace_height(self):
        xleft,ytop,xright,ybottom = self.coordspace_bbox
        y2y = (ybottom,ytop)
        yheight = max(y2y)-min(y2y)
        return yheight

    @property
    def coordspace_units(self):
        # calculate pixels per unit etc
        pixscm = 28.346457
        widthcm = self.width / float(pixscm)
        units = self.coordspace_width / float(widthcm)
        return units

    def zoom_units(self, units, center=None):
        """
        Zoom in or out based on how many units per cm to have at the new zoom level.

        Parameters:
        
        - *units*: how many coordinate units per screen cm at the new zoom level.
        - *center* (optional): xy coordinate tuple to center/offset the zoom. Defauls to middle of the bbox. 
        """
        # calculate pixels per unit etc
        unitscm = units
        cmsunit = 1 / float(unitscm)
        pixscm = 28.346457
        pixsunit = pixscm * cmsunit
        unitswidth = self.width / float(pixsunit) # use as the width of the bbox
        unitsheight = self.height / float(pixsunit) # use as the height of the bbox
        # zoom it
        newbbox = bboxhelper.resize_dimensions(self.coordspace_bbox,
                                         newwidth=unitswidth,
                                         newheight=unitsheight)
        # center it
        if center:
            newbbox = bboxhelper.center(newbbox, center)
        self.custom_space(*newbbox, lock_ratio=True)

    def zoom_factor(self, factor, center=None):
        """
        Zooms n times of previous bbox.

        Parameters:

        - *factor*: Positive values > 1 for in-zoom, negative < -1 for out-zoom.
        - *center* (optional): xy coordinate tuple to center/offset the zoom. Defauls to middle of the bbox. 
        """
        if -1 < factor < 1:
            raise Exception("Zoom error: Zoom factor must be higher than +1 or lower than -1.")
        # positive zoom means bbox must be shrunk
        if factor > 1: factor = 1 / float(factor)
        # remove minus sign for negative zoom
        elif factor <= -1: factor *= -1
        # zoom it
        newbbox = bboxhelper.resize_ratio(self.coordspace_bbox,
                           xratio=factor,
                           yratio=factor)
        # center it
        if center:
            newbbox = bboxhelper.center(newbbox, center)
        self.custom_space(*newbbox, lock_ratio=False)

    def zoom_bbox(self, xmin, ymin, xmax, ymax):
        """
        Essentially the same as using coord_space(), but takes a bbox
        in min/max format instead, converting to left/right/etc behind
        the scenes so that axis directions are preserved.

        Parameters:

        - *xmin*: The lower bound of the x-axis after the zoom.
        - *ymin*: The lower bound of the y-axis after the zoom.
        - *xmax*: The higher bound of the x-axis after the zoom.
        - *ymax*: The higher bound of the y-axis after the zoom.
        """
        xleft, ybottom, xright, ytop = xmin, ymin, xmax, ymax
        oldxleft, oldytop, oldxright, oldybottom = self.coordspace_bbox
        # ensure old and zoom axes go in same directions
        if not (xleft < xright) == (oldxleft < oldxright):
            xleft,xright = xright,xleft
        if not (ytop < ybottom) == (oldytop < oldybottom):
            ytop,ybottom = ybottom,ytop
        # zoom it
        self.custom_space(xleft, ytop, xright, ybottom, lock_ratio=True)

    def pixel_space(self):
        """
        Convenience method for setting the coordinate space to pixels,
        so the user can easily draw directly to image pixel positions.
        """
        self.drawer.settransform()
        self.coordspace_bbox = [0, 0, self.width, self.height]
        self.coordspace_transform = (1, 0, 0,
                                     0, 1, 0)

    def fraction_space(self):
        """
        Convenience method for setting the coordinate space to fractions,
        so the user can easily draw using relative fractions (0-1) of image.
        """
        self.custom_space(*[0,0,1,1])

    def percent_space(self):
        """
        Convenience method for setting the coordinate space to percentages,
        so the user can easily draw coordinates as percentage (0-100) of image.
        """
        self.custom_space(*[0,0,100,100])

    def geographic_space(self):
        """
        Convenience method for setting the coordinate space to geographic,
        so the user can easily draw coordinates as lat/long of world,
        from -180 to 180 x coordinates, and -90 to 90 y coordinates.
        Also locks the aspect ratio to fit the entire coordinate space
        inside the image without geographic distortion.
        """
        self.custom_space(*[-180,90,180,-90], lock_ratio=True)

    def custom_space(self, xleft, ytop, xright, ybottom,
                         lock_ratio=False):
        """
        Defines which areas of the screen represent which areas in the
        given drawing coordinates. Default is to draw directly with
        screen pixel coordinates. 

        Parameters:
        
        - *xleft*: The x-coordinate to be mapped to the left side of the screen.
        - *ytop*: The y-coordinate to be mapped to the top side of the screen.
        - *xright*: The x-coordinate to be mapped to the right side of the screen.
        - *ybottom*: The y-coordinate to be mapped to the bottom side of the screen.
        - *lock_ratio* (optional): Set to True if wanting to constrain the coordinate space to have the same width/height ratio as the image, in order to avoid distortion. Default is False. 

        """

        # basic info
        bbox = xleft,ytop,xright,ybottom
        x2x = (xleft,xright)
        y2y = (ybottom,ytop)
        xwidth = max(x2x)-min(x2x)
        yheight = max(y2y)-min(y2y)
        oldxwidth,oldyheight = xwidth,yheight

        # constrain the coordinate view ratio to the screen ratio, shrinking the coordinate space to ensure that it is fully contained inside the image
        centered = affine.Affine.identity()
        if lock_ratio:
            # make coords same proportions as screen
            screenxratio = self.width / float(self.height)
            yheight = yheight
            xwidth = yheight * screenxratio
            # ensure that altered coords do not shrink the original coords
            diffratio = 1.0
            if xwidth < oldxwidth: diffratio = oldxwidth / float(xwidth)
            elif yheight < oldyheight: diffratio = oldyheight / float(yheight)
            xwidth *= diffratio
            yheight *= diffratio
            # move the center of focus to middle of coordinate space if view ratio has been constrained
            xoff = (xwidth - oldxwidth) / 2.0
            yoff = (yheight - oldyheight) / 2.0
            centered *= affine.Affine.translate(xoff, yoff)
            
        # Note: The sequence of matrix multiplication is important and sensitive.
        # ...see eg http://negativeprobability.blogspot.no/2011/11/affine-transformations-and-their.html

        # scale ie resize world to screen coords
        scalex = self.width / float(xwidth)
        scaley = self.height / float(yheight)
        scaled = affine.Affine.scale(scalex,scaley)
        if xleft < xright: xoff = -min(x2x)
        else: xoff = min(x2x)
        if ytop < ybottom: yoff = -min(y2y)
        else: yoff = min(y2y)
        scaled *= affine.Affine.translate(xoff,yoff) # to force anchor upperleft world coords to upper left screen coords

        # flip world coords if axes run in different direction than screen axes
        xflip = xright < xleft
        yflip = ybottom < ytop
        if xflip: xflipoff = xwidth
        else: xflipoff = 0
        if yflip: yflipoff = yheight
        else: yflipoff = 0
        flipped = affine.Affine.translate(xflipoff,yflipoff) # to make the flipping stay in same place
        flipped *= affine.Affine.flip(xflip,yflip)

        # calculate the final coefficients and set as the drawtransform
        transcoeffs = (scaled * flipped * centered).coefficients
        self.drawer.settransform(transcoeffs)

        # finally remember the new coordinate extents and affine matrix
        self.coordspace_bbox = bboxhelper.resize_ratio(bbox,
                                           xratio=xwidth / float(oldxwidth),
                                           yratio=yheight / float(oldyheight) )
        self.coordspace_transform = transcoeffs

    def set_default_unit(unit):
        """
        Sets the default unit for drawing sizes etc.

        Parameters:

        - *unit*:
            Can be real world units (cm, mm, in, pt), percent of width or height
            (%w or %h), or percent of minimum or maximum side (%min or %max). 
            Default is percent of width. 
        """
        self.default_unit = unit












    # Drawing

    def draw_circle(self, xy=None, bbox=None, flatratio=1, **options):
        """
        Draw a circle, normal or flattened. Either specified with xy and flatratio,
        or with a bbox. 

        Parameters:

        - *xy* (optional): Xy center coordinate to place the circle. 
        - *bbox* (optional): Bounding box of the flattened circle instead of xy coordinate. 
        - *flatratio* (optional): The ratio of the circle height to width. A normal circle is given with 1.0 (default) and a half-flat circle with 0.5. 
        - *options* (optional): Keyword args dictionary of draw styling options. 
        """
        #TEMPORARY DISABLING TRANSFORM TO AVOID DEFORMED CIRCLE
        options = self._check_options(options)
        args = []
        
        if options["outlinecolor"]:
            pen = aggdraw.Pen(options["outlinecolor"], options["outlinewidth"])
            args.append(pen)
        if options["fillcolor"]:
            brush = aggdraw.Brush(options["fillcolor"])
            args.append(brush)
            
        if xy:
            x,y = xy
            x,y = self.coord2pixel(x,y)
            fillsize = options["fillsize"]
            width = options["fillwidth"]
            height = options["fillheight"]
##            width, height = width / self.width * self.coordspace_width, \
##                            height / self.height * self.coordspace_height
            if flatratio: height *= flatratio
            halfwidth, halfheight = width / 2.0, height / 2.0
            bbox = [x-halfwidth, y-halfheight, x+halfwidth, y+halfheight]
        
        elif bbox: pass
        
        else: raise Exception("Either xy or bbox has to be specified")
        
        self.drawer.settransform()
        self.drawer.ellipse(bbox, *args)
        self.drawer.settransform(self.coordspace_transform)

    def draw_triangle(self, xy=None, bbox=None, flatratio=1.0, **options):
        """
        Draw a triangle, equiangled or otherwise. Either specified with xy and flatratio,
        or with a bbox. 

        Parameters:

        - *xy* (optional): Xy center coordinate to place the triangle. 
        - *bbox* (optional): Bounding box of the flattened triangle instead of xy coordinate. 
        - *flatratio* (optional): The ratio of the triangle height to width. A normal triangle is given with 1.0 (default) and a half-flat triangle with 0.5. 
        - *options* (optional): Keyword args dictionary of draw styling options. 
        """
        options = self._check_options(options)
        args = []
        
        if options["outlinecolor"]:
            pen = aggdraw.Pen(options["outlinecolor"], options["outlinewidth"])
            args.append(pen)
        if options["fillcolor"]:
            brush = aggdraw.Brush(options["fillcolor"])
            args.append(brush)
            
        if xy:
            x,y = xy
            fillsize = options["fillsize"]
            width = options["fillwidth"]
            height = options["fillheight"]
            if flatratio: height *= flatratio
        
        elif bbox:
            xmin,ymin,xmax,ymax = bbox
            width, height = xmax - xmin, ymax - ymin
            x, y = xmin + width / 2.0, ymin + height / 2.0
        
        else: raise Exception("Either xy or bbox has to be specified")

        width, height = width / self.width * self.coordspace_width, \
                        height / self.height * self.coordspace_height
        halfwidth, halfheight = width / 2.0, height / 2.0
        coords = [x-halfwidth,y-halfheight, x+halfwidth,y-halfheight, x,y+halfheight]
        self.drawer.polygon(coords, *args)

    def draw_pie(self, xy, startangle, endangle, **options):
        """
        Draw a piece of pie.

        Parameters:

        - *xy*: Xy center coordinate to place the pie origin. 
        - *startangle*: Degree angle to start the pie.
        - *endangle*: Degree angle to end the pie.
        - *options* (optional): Keyword args dictionary of draw styling options. 
        """
        #TEMPORARY DISABLING TRANSFORM TO AVOID DEFORMED PIE
        options = self._check_options(options)
        x,y = xy
        x,y = self.coord2pixel(x,y)
        fillsize = options["fillsize"]
        bbox = [x-fillsize, y-fillsize, x+fillsize, y+fillsize]
        args = []
        if options["outlinecolor"]:
            pen = aggdraw.Pen(options["outlinecolor"], options["outlinewidth"])
            args.append(pen)
        if options["fillcolor"]:
            brush = aggdraw.Brush(options["fillcolor"])
            args.append(brush)
        self.drawer.settransform()
        self.drawer.pieslice(bbox, startangle, endangle, *args)
        self.drawer.settransform(self.coordspace_transform)

    def draw_box(self, xy=None, bbox=None, flatratio=1.0, **options):
        """
        Draw a square, equisized or rectangular. Either specified with xy and flatratio,
        or with a bbox. 

        Parameters:

        - *xy* (optional): Xy center coordinate to place the square. 
        - *bbox* (optional): Bounding box of the flattened rectangle instead of xy coordinate. 
        - *flatratio* (optional): The ratio of the rectangle height to width. A normal square is given with 1.0 (default) and a half-flat rectangle with 0.5. 
        - *options* (optional): Keyword args dictionary of draw styling options. 
        """
        options = self._check_options(options)
        args = []
        
        if options["outlinecolor"]:
            pen = aggdraw.Pen(options["outlinecolor"], options["outlinewidth"])
            args.append(pen)
        if options["fillcolor"]:
            brush = aggdraw.Brush(options["fillcolor"])
            args.append(brush)
            
        if xy:
            x,y = xy
            width = options["fillwidth"]
            height = options["fillheight"]
            if flatratio: height *= flatratio
            width, height = width / self.width * self.coordspace_width, \
                            height / self.height * self.coordspace_height
            halfwidth, halfheight = width / 2.0, height / 2.0
            bbox = [x-halfwidth, y-halfheight, x+halfwidth, y+halfheight]
        
        elif bbox: pass
        
        else: raise Exception("Either xy or bbox has to be specified")
        
        self.drawer.rectangle(bbox, *args)

    def draw_line(self, coords, smooth=False, **options):
        """
        Connect a series of coordinate points with one or more lines.
        Outline does not work with this method.

        Parameters:

        - *coords*: A list of coordinates for the linesequence.
        - *smooth* (optional): If True, smooths the lines by drawing quadratic bezier curves between midpoints of each line segment. Default is False.
        - *options* (optional): Keyword args dictionary of draw styling options. 
        """
        # NOTE: Outline does not work because uses paths instead of normal line method.
        # TODO: Add volume param, containing a list of linewidths same length as line
        # or as a function that calculates the width at each node
        # Result is a flow line with varying thickness at each node
        # Have to calculate left/right xy at each node, and use symbol curveto()
        # Easy and really cool...DO IT!
        options = self._check_options(options)
        
        if not hasattr(coords[0], "__iter__"):
            coords = _grouper(coords, 2)
        else: coords = (point for point in coords)
        
        # get drawing tools from options
        args = []
        if options["fillcolor"]:
            pen = aggdraw.Pen(options["fillcolor"], options["fillsize"])
            args.append(pen)

        if smooth:

            # Note: Creation of the aggdraw.Symbol object here can be
            # very slow for long lines; Path is much faster but due
            # to a bug it does not correctly render curves, hence the use
            # of Symbol
            
            pathstring = ""
            
            # begin
            coords = _pairwise(coords)
            (startx,starty),(endx,endy) = next(coords)
            pathstring += " M%s,%s" %(startx, starty)
            
            # draw straight line to first line midpoint
            midx,midy = (endx + startx) / 2.0, (endy + starty) / 2.0
            pathstring += " L%s,%s" %(midx, midy)
            oldmidx,oldmidy = midx,midy
            
            # for each line
            for line in coords:
                # curve from midpoint of first to midpoint of second
                (startx,starty),(endx,endy) = line
                midx,midy = (endx + startx) / 2.0, (endy + starty) / 2.0
                pathstring += " Q%s,%s,%s,%s" %(startx, starty, midx, midy)
                oldmidx,oldmidy = midx,midy
                
            # draw straight line to endpoint of last line
            pathstring += " L%s,%s" %(endx, endy)

            # make into symbol object
            symbol = aggdraw.Symbol(pathstring)

            # draw the constructed symbol
            self.drawer.symbol((0,0), symbol, *args)

        else:

            path = aggdraw.Path()
            
            # begin
            startx,starty = next(coords)
            path.moveto(startx, starty)
            
            # connect to each successive point
            for nextx,nexty in coords:
                path.lineto(nextx, nexty)

            # draw the constructed path
            self.drawer.path((0,0), path, *args)

    def draw_polygon(self, coords, holes=[], **options):
        """
        Draw polygon and holes with color fill.
        Holes must be counterclockwise.

        Parameters:
        
        - *coords*: A list of coordinates for the polygon exterior.
        - *holes* (optional): A list of one or more polygon hole coordinates, one for each hole. Defaults to no holes.
        - *options* (optional): Keyword args dictionary of draw styling options. 
        """
        options = self._check_options(options)
        
        path = aggdraw.Path()
        
        if not hasattr(coords[0], "__iter__"):
            coords = _grouper(coords, 2)
        else: coords = (point for point in coords)

        def traverse_ring(coords):
            # begin
            startx,starty = next(coords)
            path.moveto(startx, starty)
            
            # connect to each successive point
            for nextx,nexty in coords:
                path.lineto(nextx, nexty)
            path.close()

        # first exterior
        traverse_ring(coords)

        # then holes
        for hole in holes:
            # !!! need to test for ring direction !!!
            if not hasattr(hole[0], "__iter__"):
                hole = _grouper(hole, 2)
            else: hole = (point for point in hole)
            traverse_ring(hole)

        # options        
        args = []
        if options["fillcolor"]:
            fillbrush = aggdraw.Brush(options["fillcolor"])
            args.append(fillbrush)
        if options["outlinecolor"]:
            outlinepen = aggdraw.Pen(options["outlinecolor"], options["outlinewidth"])
            args.append(outlinepen)
            
        self.drawer.path((0,0), path, *args)

    def draw_text(self, xy, text, **options):
        """
        Draws basic text.

        Parameters:

        - *xy*: The xy location to write the text.
        - *text*: The text string to write.
        - *options*: Keyword args dictionary of text styling options.
            This includes textfont, textsize, textcolor, and textanchor.
            Textfont can be the name, filename, or filepath of a font. 
            Textanchor can be any compass direction n,ne,e,se,s,sw,w,nw, or center.
        """
        x,y = xy
        options = self._check_text_options(options)

        # process text options
        fontlocation = _get_fontpath(options["textfont"])
        PIL_drawer = PIL.ImageDraw.Draw(self.img)

        # PIL doesnt support transforms, so must get the pixel coords of the coordinate
        x,y = self.coord2pixel(x,y)
        
        # get font dimensions
        font = PIL.ImageFont.truetype(fontlocation, size=options["textsize"]) #, opacity=options["textopacity"])
        fontwidth, fontheight = font.getsize(text)
        # anchor
        textanchor = options["textanchor"].lower()
        if textanchor == "center":
            x = int(x - fontwidth/2.0)
            y = int(y - fontheight/2.0)
        else:
            x = int(x - fontwidth/2.0)
            y = int(y - fontheight/2.0)
            if "n" in textanchor:
                y = int(y + fontheight/2.0)
            elif "s" in textanchor:
                y = int(y - fontheight/2.0)
            if "e" in textanchor:
                x = int(x - fontwidth/2.0)
            elif "w" in textanchor:
                x = int(x + fontwidth/2.0)

        # then draw text
        self.drawer.flush()
        # for text wrapping inside bbox, see: http://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
        # ...
        PIL_drawer.text((x,y), text, fill=options["textcolor"], font=font)
        
        # update changes to the aggdrawer, and remember to reapply transform
        self.drawer = aggdraw.Draw(self.img)
        self.drawer.settransform(self.coordspace_transform)

    def draw_geojson(self, geojobj, **options):
        """
        Draws a shape based on the GeoJSON format. 

        Parameters: 

        - *geojobj*: Takes a GeoJSON dictionary or object that has the \_\_geo_interface__ attribute. 
        - *options*: Keyword args dictionary of draw styling options.
        """
        if isinstance(geojobj, dict): geojson = geojobj
        else: geojson = geojobj.__geo_interface__
        geotype = geojson["type"]
        coords = geojson["coordinates"]
        if geotype == "Point":
            self.draw_circle(xy=coords, **options)
        elif geotype == "MultiPoint":
            for point in coords:
                self.draw_circle(xy=point, **options)
        elif geotype == "LineString":
            self.draw_line(coords=coords, **options)
        elif geotype == "MultiLineString":
            for line in coords:
                self.draw_line(coords=line, **options)
        elif geotype == "Polygon":
            exterior = coords[0]
            interiors = []
            if len(coords) > 1:
                interiors.extend(coords[1:])
            self.draw_polygon(exterior, holes=interiors, **options)
        elif geotype == "MultiPolygon":
            for poly in coords:
                exterior = poly[0]
                interiors = []
                if len(poly) > 1:
                    interiors.extend(poly[1:])
                self.draw_polygon(exterior, holes=interiors, **options)

##    def draw_svg(self, svg):
##        pass










    # Interactive

    def pixel2coord(self, x, y):
        """
        Transforms a pixel location on the image to its position in the canvas coordinate system.

        Parameters:

        - *x*: X image pixel coordinate.
        - *y*: Y image pixel coordinate. 
        """
        # NEED TO CHANGE TO USE INVERSE TRANSFORM COEFFS
        # partly taken from Sean Gillies "affine.py"
        a,b,c,d,e,f = self.coordspace_transform
        det = a*e - b*d
        idet = 1 / float(det)
        ra = e * idet
        rb = -b * idet
        rd = -d * idet
        re = a * idet
        newx = (x*ra + y*rb + (-c*ra - f*rb) )
        newy = (x*rd + y*re + (-c*rd - f*re) )
        return newx,newy

    def pixel2coord_dist(self, x, y):
        # SHOULD BE REMOVED, SINCE WE HAVE INSTEAD measure_dist()...
        # partly taken from Sean Gillies "affine.py"
        a,b,c,d,e,f = self.coordspace_transform
        det = a*e - b*d
        idet = 1 / float(det)
        ra = e * idet
        rb = -b * idet
        rd = -d * idet
        re = a * idet
        newx = (x*ra) # only considers xoffset
        newy = (y*re) # only considers yoffset
        return newx,newy

    def coord2pixel(self, x, y):
        """
        Transforms a data coordinate to its canvas image pixel position.

        Parameters:

        - *x*: X data coordinate.
        - *y*: Y data coordinate.
        """
        a,b,c,d,e,f = self.coordspace_transform
        newx,newy = (x*a + y*b + c, x*d + y*e + f)
        return int(newx),int(newy)

    def measure_dist(self, fromxy, toxy):
        """
        Returns euclidean distance between two xy point tuples, assuming they are linear cartesian coordinates.

        Parameters:

        - *fromxy*: Data coordinate point to measure from.
        - *toxy*: Data coordinate point to measure to. 
        """
        fromx,fromy = fromxy
        tox,toy = toxy
        # dist = math.sqrt( (fromx-tox)**2 + (fromy-toy)**2 )
        xdiff,ydiff = (fromx-tox),(fromy-toy)
        dist = math.hypot(xdiff,ydiff) 
        return dist











    # Viewing and Saving

    def clear(self):
        """
        Clears any drawing done on the canvas, and resets it to its
        original mode, size, and background. 
        """
        self.img = PIL.Image.new(self.img.mode, self.img.size, self.background)
        self.drawer = aggdraw.Draw(self.img)
        
    def get_image(self):
        """
        Retrieves the canvas image along with any drawing updates.

        Returns:

        - A PIL image. 
        """
        self.drawer.flush()
        return self.img
    
    def get_tkimage(self):
        """
        Retrieves a Tkinter compatible image along with any drawing updates.

        Returns:

        - A Tkinter PhotoImage image.
        """
        self.drawer.flush()
        return PIL.ImageTk.PhotoImage(self.img)

    def view(self):
        """
        Creates a Tkinter application that packs the canvas image in order to view
        what the canvas image looks like. 
        """
        window = tk.Tk()
        label = tk.Label(window)
        label.pack()
        img = self.get_tkimage()
        label["image"] = label.img = img
        window.mainloop()

    def save(self, filepath):
        """
        Saves the canvas image to a file.

        Parameters:

        - *filepath*: The filepath to save the image, including the file type extension.
            Can be saved to any image type supported by PIL. 
        """
        self.drawer.flush()
        self.img.save(filepath)












    # Internal only

    def _check_options(self, customoptions):
        # types
        customoptions = customoptions.copy()
        
        # fillsize
        # NOTE: if circle is specified with an area, get radius by:
        #    math.sqrt(area_squared/math.pi)
        if customoptions.get("fillsize"):
            customoptions["fillsize"] = units.parse_dist(customoptions["fillsize"],
                                                         ppi=self.ppi,
                                                         default_unit=self.default_unit,
                                                         canvassize=[self.width,self.height])
        else:
            customoptions["fillsize"] = units.parse_diststring("0.7%w", ppi=self.ppi, canvassize=[self.width,self.height])
        if not customoptions.get("fillwidth"):
            customoptions["fillwidth"] = customoptions["fillsize"] * 2
        if not customoptions.get("fillheight"):
            customoptions["fillheight"] = customoptions["fillsize"] * 2
            
        # outlinewidth
        if customoptions.get("outlinewidth"):
            customoptions["outlinewidth"] = units.parse_dist(customoptions["outlinewidth"],
                                                         ppi=self.ppi,
                                                         default_unit=self.default_unit,
                                                         canvassize=[self.width,self.height])
        else: customoptions["outlinewidth"] = units.parse_diststring("0.07%w", ppi=self.ppi, canvassize=[self.width,self.height])
        
        # colors
        if customoptions.get("fillcolor", "not specified") == "not specified":
            customoptions["fillcolor"] = [random.randrange(0,255) for _ in xrange(3)]
        if customoptions.get("outlinecolor", "not specified") == "not specified":
            customoptions["outlinecolor"] = (0,0,0)
            
        # finish  
        return customoptions

    def _check_text_options(self, customoptions):
        customoptions = customoptions.copy()
        #text and font
        if not customoptions.get("textfont"):
            customoptions["textfont"] = "Arial"
            
        # RIGHT NOW, TEXTSIZE IS PERCENT OF IMAGE SIZE, BUT MAYBE USE NORMAL SIZE INSTEAD
        # see: http://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image

        if not customoptions.get("textsize"):
            #customoptions["textsize"] = int(round(self.width*0.0055)) #equivalent to textsize 7
            customoptions["textsize"] = 8
        else:
            customoptions["textsize"] = int(round(customoptions["textsize"]))
            #input is percent textheight of MAPWIDTH
            #percentheight = customoptions["textsize"]
            #so first get pixel height
            #pixelheight = self.width*percentheight
            #to get textsize
            #textsize = int(round(pixelheight*0.86))
            #customoptions["textsize"] = textsize
        if not customoptions.get("textcolor"):
            customoptions["textcolor"] = (0,0,0)
##        if not customoptions.get("textopacity"):
##            customoptions["textopacity"] = 255
##        if not customoptions.get("texteffect"):
##            customoptions["texteffect"] = None
        if not customoptions.get("textanchor"):
            customoptions["textanchor"] = "center"
        #text background box
##        if not customoptions.get("textboxfillcolor"):
##            customoptions["textboxfillcolor"] = None
##        else:
##            if customoptions.get("textboxoutlinecolor","not specified") == "not specified":
##                customoptions["textboxoutlinecolor"] = (0,0,0)
##        if not customoptions.get("textboxfillsize"):
##            customoptions["textboxfillsize"] = 1.1 #proportion size of text bounding box
##        if not customoptions.get("textboxoutlinecolor"):
##            customoptions["textboxoutlinecolor"] = None
##        if not customoptions.get("textboxoutlinewidth"):
##            customoptions["textboxoutlinewidth"] = 1.0 #percent of fill, not of map
##        if not customoptions.get("textboxopacity"):
##            customoptions["textboxopacity"] = 0 #both fill and outline
        return customoptions





##############################
# User functions

def from_image(img):
    """
    Loads a Canvas instance preloaded with the size and pixels of an
    existing PIL image, from memory.

    Parameters:

    - *img*: A PIL image instance.

    Returns:

    - A Canvas instance. 
    """
    canvas = Canvas(100, 100)
    canvas.img = img
    if not canvas.img.mode in ("RGB","RGBA"):
        canvas.img = canvas.img.convert("RGBA")
    canvas.drawer = aggdraw.Draw(canvas.img)
    canvas.pixel_space()
    return canvas

def load(filepath):
    """
    Loads a Canvas instance preloaded with the size and pixels of an
    existing image from a file.

    Parameters:

    - *filepath*: The filepath of the image file to load.

    Returns:

    - A Canvas instance.
    """
    canvas = Canvas(100, 100)
    canvas.img = PIL.Image.open(filepath)
    if not canvas.img.mode in ("RGB","RGBA"):
        canvas.img = canvas.img.convert("RGBA")
    canvas.drawer = aggdraw.Draw(canvas.img)
    canvas.pixel_space()
    return canvas





