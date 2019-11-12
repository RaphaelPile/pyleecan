# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Slot import Slot

from pyleecan.Classes.check import InitUnKnowClassError


class SlotMag(Slot):
    """Slot for inset and surface magnet (abstract)"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, W3=0, Zs=36, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["W3", "Zs"])
            # Overwrite default value with init_dict content
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W3 = W3
        # Call Slot init
        super(SlotMag, self).__init__(Zs=Zs)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotMag_str = ""
        # Get the properties inherited from Slot
        SlotMag_str += super(SlotMag, self).__str__() + linesep
        SlotMag_str += "W3 = " + str(self.W3)
        return SlotMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotMag, self).__eq__(other):
            return False
        if other.W3 != self.W3:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Slot
        SlotMag_dict = super(SlotMag, self).as_dict()
        SlotMag_dict["W3"] = self.W3
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotMag_dict["__class__"] = "SlotMag"
        return SlotMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W3 = None
        # Set to None the properties inherited from Slot
        super(SlotMag, self)._set_None()

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float")
        self._W3 = value

    # Angle between magnet in the slot
    # Type : float
    W3 = property(
        fget=_get_W3, fset=_set_W3, doc=u"""Angle between magnet in the slot"""
    )
