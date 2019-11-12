# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Surface import Surface

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Geometry.Circle.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Geometry.Circle.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from pyleecan.Methods.Geometry.Circle.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Geometry.Circle.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from pyleecan.Methods.Geometry.Circle.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from pyleecan.Methods.Geometry.Circle.get_patch import get_patch
except ImportError as error:
    get_patch = error

try:
    from pyleecan.Methods.Geometry.Circle.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from pyleecan.Methods.Geometry.Circle.translate import translate
except ImportError as error:
    translate = error


from pyleecan.Classes.check import InitUnKnowClassError


class Circle(Surface):
    """Circle define by  the center of circle(point_ref), the label and the radius"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Circle.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.Circle.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method comp_length: " + str(comp_length))
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.Circle.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Circle method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.Circle.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.Circle.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.Circle.get_patch
    if isinstance(get_patch, ImportError):
        get_patch = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method get_patch: " + str(get_patch))
            )
        )
    else:
        get_patch = get_patch
    # cf Methods.Geometry.Circle.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.Circle.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # save method is available in all object
    save = save

    def __init__(
        self, radius=1, center=0, line_label="", point_ref=0, label="", init_dict=None
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict, ["radius", "center", "line_label", "point_ref", "label"]
            )
            # Overwrite default value with init_dict content
            if "radius" in list(init_dict.keys()):
                radius = init_dict["radius"]
            if "center" in list(init_dict.keys()):
                center = init_dict["center"]
            if "line_label" in list(init_dict.keys()):
                line_label = init_dict["line_label"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.radius = radius
        self.center = center
        self.line_label = line_label
        # Call Surface init
        super(Circle, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Circle_str = ""
        # Get the properties inherited from Surface
        Circle_str += super(Circle, self).__str__() + linesep
        Circle_str += "radius = " + str(self.radius) + linesep
        Circle_str += "center = " + str(self.center) + linesep
        Circle_str += 'line_label = "' + str(self.line_label) + '"'
        return Circle_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(Circle, self).__eq__(other):
            return False
        if other.radius != self.radius:
            return False
        if other.center != self.center:
            return False
        if other.line_label != self.line_label:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Surface
        Circle_dict = super(Circle, self).as_dict()
        Circle_dict["radius"] = self.radius
        Circle_dict["center"] = self.center
        Circle_dict["line_label"] = self.line_label
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Circle_dict["__class__"] = "Circle"
        return Circle_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.radius = None
        self.center = None
        self.line_label = None
        # Set to None the properties inherited from Surface
        super(Circle, self)._set_None()

    def _get_radius(self):
        """getter of radius"""
        return self._radius

    def _set_radius(self, value):
        """setter of radius"""
        check_var("radius", value, "float", Vmin=0)
        self._radius = value

    # Radius of the circle
    # Type : float, min = 0
    radius = property(
        fget=_get_radius, fset=_set_radius, doc=u"""Radius of the circle"""
    )

    def _get_center(self):
        """getter of center"""
        return self._center

    def _set_center(self, value):
        """setter of center"""
        check_var("center", value, "complex")
        self._center = value

    # center of the Circle
    # Type : complex
    center = property(
        fget=_get_center, fset=_set_center, doc=u"""center of the Circle"""
    )

    def _get_line_label(self):
        """getter of line_label"""
        return self._line_label

    def _set_line_label(self, value):
        """setter of line_label"""
        check_var("line_label", value, "str")
        self._line_label = value

    # Label to set to the lines
    # Type : str
    line_label = property(
        fget=_get_line_label, fset=_set_line_label, doc=u"""Label to set to the lines"""
    )
