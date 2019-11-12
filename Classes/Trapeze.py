# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Surface import Surface

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Geometry.Trapeze.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Geometry.Trapeze.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from pyleecan.Methods.Geometry.Trapeze.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Geometry.Trapeze.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from pyleecan.Methods.Geometry.Trapeze.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from pyleecan.Methods.Geometry.Trapeze.get_patch import get_patch
except ImportError as error:
    get_patch = error

try:
    from pyleecan.Methods.Geometry.Trapeze.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from pyleecan.Methods.Geometry.Trapeze.translate import translate
except ImportError as error:
    translate = error


from pyleecan.Classes.check import InitUnKnowClassError


class Trapeze(Surface):
    """Trapeze defined by  the center of symmetry(point_ref), the label, the polar angle, the height and the big and small weight"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Trapeze.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Trapeze method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.Trapeze.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError("Can't use Trapeze method comp_length: " + str(comp_length))
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.Trapeze.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Trapeze method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.Trapeze.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use Trapeze method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.Trapeze.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use Trapeze method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.Trapeze.get_patch
    if isinstance(get_patch, ImportError):
        get_patch = property(
            fget=lambda x: raise_(
                ImportError("Can't use Trapeze method get_patch: " + str(get_patch))
            )
        )
    else:
        get_patch = get_patch
    # cf Methods.Geometry.Trapeze.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Trapeze method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.Trapeze.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Trapeze method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # save method is available in all object
    save = save

    def __init__(self, height=1, W2=1, W1=1, point_ref=0, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["height", "W2", "W1", "point_ref", "label"])
            # Overwrite default value with init_dict content
            if "height" in list(init_dict.keys()):
                height = init_dict["height"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.height = height
        self.W2 = W2
        self.W1 = W1
        # Call Surface init
        super(Trapeze, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Trapeze_str = ""
        # Get the properties inherited from Surface
        Trapeze_str += super(Trapeze, self).__str__() + linesep
        Trapeze_str += "height = " + str(self.height) + linesep
        Trapeze_str += "W2 = " + str(self.W2) + linesep
        Trapeze_str += "W1 = " + str(self.W1)
        return Trapeze_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(Trapeze, self).__eq__(other):
            return False
        if other.height != self.height:
            return False
        if other.W2 != self.W2:
            return False
        if other.W1 != self.W1:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Surface
        Trapeze_dict = super(Trapeze, self).as_dict()
        Trapeze_dict["height"] = self.height
        Trapeze_dict["W2"] = self.W2
        Trapeze_dict["W1"] = self.W1
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Trapeze_dict["__class__"] = "Trapeze"
        return Trapeze_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.height = None
        self.W2 = None
        self.W1 = None
        # Set to None the properties inherited from Surface
        super(Trapeze, self)._set_None()

    def _get_height(self):
        """getter of height"""
        return self._height

    def _set_height(self, value):
        """setter of height"""
        check_var("height", value, "float", Vmin=0)
        self._height = value

    # the height of the Trapeze
    # Type : float, min = 0
    height = property(
        fget=_get_height, fset=_set_height, doc=u"""the height of the Trapeze"""
    )

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    # the big base of Trapeze
    # Type : float, min = 0
    W2 = property(fget=_get_W2, fset=_set_W2, doc=u"""the big base of Trapeze""")

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    # the small base of the Trapeze
    # Type : float, min = 0
    W1 = property(fget=_get_W1, fset=_set_W1, doc=u"""the small base of the Trapeze""")
