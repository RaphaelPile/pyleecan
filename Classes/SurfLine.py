# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Surface import Surface

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Geometry.SurfLine.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from pyleecan.Methods.Geometry.SurfLine.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from pyleecan.Methods.Geometry.SurfLine.translate import translate
except ImportError as error:
    translate = error

try:
    from pyleecan.Methods.Geometry.SurfLine.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Geometry.SurfLine.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from pyleecan.Methods.Geometry.SurfLine.get_patch import get_patch
except ImportError as error:
    get_patch = error

try:
    from pyleecan.Methods.Geometry.SurfLine.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from pyleecan.Methods.Geometry.SurfLine.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Geometry.SurfLine.plot_lines import plot_lines
except ImportError as error:
    plot_lines = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Line import Line


class SurfLine(Surface):
    """SurfLine defined by list of lines that delimit it, label and point reference."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.SurfLine.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.SurfLine.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.SurfLine.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # cf Methods.Geometry.SurfLine.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.SurfLine.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfLine method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.SurfLine.get_patch
    if isinstance(get_patch, ImportError):
        get_patch = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method get_patch: " + str(get_patch))
            )
        )
    else:
        get_patch = get_patch
    # cf Methods.Geometry.SurfLine.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.SurfLine.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfLine method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.SurfLine.plot_lines
    if isinstance(plot_lines, ImportError):
        plot_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method plot_lines: " + str(plot_lines))
            )
        )
    else:
        plot_lines = plot_lines
    # save method is available in all object
    save = save

    def __init__(self, line_list=list(), point_ref=0, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["line_list", "point_ref", "label"])
            # Overwrite default value with init_dict content
            if "line_list" in list(init_dict.keys()):
                line_list = init_dict["line_list"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        # line_list can be None or a list of Line object
        self.line_list = list()
        if type(line_list) is list:
            for obj in line_list:
                if obj is None:  # Default value
                    self.line_list.append(Line())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in [
                        "Line",
                        "Segment",
                        "Arc1",
                        "Arc2",
                        "Arc3",
                        "Arc",
                    ]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for line_list"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.line_list.append(class_obj(init_dict=obj))
                else:
                    self.line_list.append(obj)
        elif line_list is None:
            self.line_list = list()
        else:
            self.line_list = line_list
        # Call Surface init
        super(SurfLine, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SurfLine_str = ""
        # Get the properties inherited from Surface
        SurfLine_str += super(SurfLine, self).__str__() + linesep
        if len(self.line_list) == 0:
            SurfLine_str += "line_list = []"
        for ii in range(len(self.line_list)):
            SurfLine_str += (
                "line_list["
                + str(ii)
                + "] = "
                + str(self.line_list[ii].as_dict())
                + "\n"
            )
        return SurfLine_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(SurfLine, self).__eq__(other):
            return False
        if other.line_list != self.line_list:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Surface
        SurfLine_dict = super(SurfLine, self).as_dict()
        SurfLine_dict["line_list"] = list()
        for obj in self.line_list:
            SurfLine_dict["line_list"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SurfLine_dict["__class__"] = "SurfLine"
        return SurfLine_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.line_list:
            obj._set_None()
        # Set to None the properties inherited from Surface
        super(SurfLine, self)._set_None()

    def _get_line_list(self):
        """getter of line_list"""
        for obj in self._line_list:
            if obj is not None:
                obj.parent = self
        return self._line_list

    def _set_line_list(self, value):
        """setter of line_list"""
        check_var("line_list", value, "[Line]")
        self._line_list = value

        for obj in self._line_list:
            if obj is not None:
                obj.parent = self

    # List of Lines
    # Type : [Line]
    line_list = property(
        fget=_get_line_list, fset=_set_line_list, doc=u"""List of Lines """
    )
