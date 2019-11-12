# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.Machine.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Machine.Machine.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Machine.Machine.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from pyleecan.Methods.Machine.Machine.comp_width_airgap_mag import (
        comp_width_airgap_mag,
    )
except ImportError as error:
    comp_width_airgap_mag = error

try:
    from pyleecan.Methods.Machine.Machine.comp_width_airgap_mec import (
        comp_width_airgap_mec,
    )
except ImportError as error:
    comp_width_airgap_mec = error

try:
    from pyleecan.Methods.Machine.Machine.get_lamination import get_lamination
except ImportError as error:
    get_lamination = error

try:
    from pyleecan.Methods.Machine.Machine.comp_Rgap_mec import comp_Rgap_mec
except ImportError as error:
    comp_Rgap_mec = error

try:
    from pyleecan.Methods.Machine.Machine.plot import plot
except ImportError as error:
    plot = error

try:
    from pyleecan.Methods.Machine.Machine.comp_output_geo import comp_output_geo
except ImportError as error:
    comp_output_geo = error

try:
    from pyleecan.Methods.Machine.Machine.comp_length_airgap_active import (
        comp_length_airgap_active,
    )
except ImportError as error:
    comp_length_airgap_active = error

try:
    from pyleecan.Methods.Machine.Machine.get_polar_eq import get_polar_eq
except ImportError as error:
    get_polar_eq = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft


class Machine(FrozenClass):
    """Abstract class for machines"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Machine.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.Machine.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.Machine.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method comp_masses: " + str(comp_masses))
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.Machine.comp_width_airgap_mag
    if isinstance(comp_width_airgap_mag, ImportError):
        comp_width_airgap_mag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_width_airgap_mag: "
                    + str(comp_width_airgap_mag)
                )
            )
        )
    else:
        comp_width_airgap_mag = comp_width_airgap_mag
    # cf Methods.Machine.Machine.comp_width_airgap_mec
    if isinstance(comp_width_airgap_mec, ImportError):
        comp_width_airgap_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_width_airgap_mec: "
                    + str(comp_width_airgap_mec)
                )
            )
        )
    else:
        comp_width_airgap_mec = comp_width_airgap_mec
    # cf Methods.Machine.Machine.get_lamination
    if isinstance(get_lamination, ImportError):
        get_lamination = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_lamination: " + str(get_lamination)
                )
            )
        )
    else:
        get_lamination = get_lamination
    # cf Methods.Machine.Machine.comp_Rgap_mec
    if isinstance(comp_Rgap_mec, ImportError):
        comp_Rgap_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_Rgap_mec: " + str(comp_Rgap_mec)
                )
            )
        )
    else:
        comp_Rgap_mec = comp_Rgap_mec
    # cf Methods.Machine.Machine.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.Machine.comp_output_geo
    if isinstance(comp_output_geo, ImportError):
        comp_output_geo = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_output_geo: " + str(comp_output_geo)
                )
            )
        )
    else:
        comp_output_geo = comp_output_geo
    # cf Methods.Machine.Machine.comp_length_airgap_active
    if isinstance(comp_length_airgap_active, ImportError):
        comp_length_airgap_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_length_airgap_active: "
                    + str(comp_length_airgap_active)
                )
            )
        )
    else:
        comp_length_airgap_active = comp_length_airgap_active
    # cf Methods.Machine.Machine.get_polar_eq
    if isinstance(get_polar_eq, ImportError):
        get_polar_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_polar_eq: " + str(get_polar_eq)
                )
            )
        )
    else:
        get_polar_eq = get_polar_eq
    # save method is available in all object
    save = save

    def __init__(
        self,
        rotor=-1,
        stator=-1,
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if rotor == -1:
            rotor = Lamination()
        if stator == -1:
            stator = Lamination()
        if frame == -1:
            frame = Frame()
        if shaft == -1:
            shaft = Shaft()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict, ["rotor", "stator", "frame", "shaft", "name", "desc"]
            )
            # Overwrite default value with init_dict content
            if "rotor" in list(init_dict.keys()):
                rotor = init_dict["rotor"]
            if "stator" in list(init_dict.keys()):
                stator = init_dict["stator"]
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
        # Initialisation by argument
        self.parent = None
        # rotor can be None, a Lamination object or a dict
        if isinstance(rotor, dict):
            # Check that the type is correct (including daughter)
            class_name = rotor.get("__class__")
            if class_name not in [
                "Lamination",
                "LamHole",
                "LamSlot",
                "LamSlotWind",
                "LamSlotMag",
                "LamSquirrelCage",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for rotor"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.rotor = class_obj(init_dict=rotor)
        else:
            self.rotor = rotor
        # stator can be None, a Lamination object or a dict
        if isinstance(stator, dict):
            # Check that the type is correct (including daughter)
            class_name = stator.get("__class__")
            if class_name not in [
                "Lamination",
                "LamHole",
                "LamSlot",
                "LamSlotWind",
                "LamSlotMag",
                "LamSquirrelCage",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for stator"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.stator = class_obj(init_dict=stator)
        else:
            self.stator = stator
        # frame can be None, a Frame object or a dict
        if isinstance(frame, dict):
            self.frame = Frame(init_dict=frame)
        else:
            self.frame = frame
        # shaft can be None, a Shaft object or a dict
        if isinstance(shaft, dict):
            self.shaft = Shaft(init_dict=shaft)
        else:
            self.shaft = shaft
        self.name = name
        self.desc = desc

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Machine_str = ""
        if self.parent is None:
            Machine_str += "parent = None " + linesep
        else:
            Machine_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Machine_str += "rotor = " + str(self.rotor.as_dict()) + linesep + linesep
        Machine_str += "stator = " + str(self.stator.as_dict()) + linesep + linesep
        Machine_str += "frame = " + str(self.frame.as_dict()) + linesep + linesep
        Machine_str += "shaft = " + str(self.shaft.as_dict()) + linesep + linesep
        Machine_str += 'name = "' + str(self.name) + '"' + linesep
        Machine_str += 'desc = "' + str(self.desc) + '"'
        return Machine_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.rotor != self.rotor:
            return False
        if other.stator != self.stator:
            return False
        if other.frame != self.frame:
            return False
        if other.shaft != self.shaft:
            return False
        if other.name != self.name:
            return False
        if other.desc != self.desc:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Machine_dict = dict()
        if self.rotor is None:
            Machine_dict["rotor"] = None
        else:
            Machine_dict["rotor"] = self.rotor.as_dict()
        if self.stator is None:
            Machine_dict["stator"] = None
        else:
            Machine_dict["stator"] = self.stator.as_dict()
        if self.frame is None:
            Machine_dict["frame"] = None
        else:
            Machine_dict["frame"] = self.frame.as_dict()
        if self.shaft is None:
            Machine_dict["shaft"] = None
        else:
            Machine_dict["shaft"] = self.shaft.as_dict()
        Machine_dict["name"] = self.name
        Machine_dict["desc"] = self.desc
        # The class name is added to the dict fordeserialisation purpose
        Machine_dict["__class__"] = "Machine"
        return Machine_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.rotor is not None:
            self.rotor._set_None()
        if self.stator is not None:
            self.stator._set_None()
        if self.frame is not None:
            self.frame._set_None()
        if self.shaft is not None:
            self.shaft._set_None()
        self.name = None
        self.desc = None

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
        check_var("rotor", value, "Lamination")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    # Machine's Rotor
    # Type : Lamination
    rotor = property(fget=_get_rotor, fset=_set_rotor, doc=u"""Machine's Rotor""")

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
        check_var("stator", value, "Lamination")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    # Machine's Stator
    # Type : Lamination
    stator = property(fget=_get_stator, fset=_set_stator, doc=u"""Machine's Stator""")

    def _get_frame(self):
        """getter of frame"""
        return self._frame

    def _set_frame(self, value):
        """setter of frame"""
        check_var("frame", value, "Frame")
        self._frame = value

        if self._frame is not None:
            self._frame.parent = self

    # Machine's Frame
    # Type : Frame
    frame = property(fget=_get_frame, fset=_set_frame, doc=u"""Machine's Frame""")

    def _get_shaft(self):
        """getter of shaft"""
        return self._shaft

    def _set_shaft(self, value):
        """setter of shaft"""
        check_var("shaft", value, "Shaft")
        self._shaft = value

        if self._shaft is not None:
            self._shaft.parent = self

    # Machine's Shaft
    # Type : Shaft
    shaft = property(fget=_get_shaft, fset=_set_shaft, doc=u"""Machine's Shaft""")

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Name of the machine
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Name of the machine""")

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    # Machine description
    # Type : str
    desc = property(fget=_get_desc, fset=_set_desc, doc=u"""Machine description""")
