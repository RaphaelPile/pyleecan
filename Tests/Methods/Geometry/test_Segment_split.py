# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.Segment import Segment

from pyleecan.Methods.Geometry.Segment import PointSegmentError, NbPointSegmentDError
from numpy import pi, array, exp


# For AlmostEqual
DELTA = 1e-6

split_list = list()
# 1) Intersection is a point of the cutting line
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 0.5,  # First point of cutting line
        "Z2": 1j,  # Seconf point of cutting line
        "Zi": [0.5],  # Expected intersection points
        "Zb_top": 0,  # Expected begin for cutting with is_top
        "Ze_top": 0.5,  # Expected end for cutting with is_top
        "Zb_bot": 0.5,  # Expected begin for cutting with not is_top
        "Ze_bot": 1,  # Expected end for cutting with not is_top
    }
)
# 2) Same case as previous one with reverse Z1 and Z2
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 1j,  # First point of cutting line
        "Z2": 0.5,  # Seconf point of cutting line
        "Zi": [0.5],  # Expected intersection points
        "Zb_top": 0.5,  # Expected begin for cutting with is_top
        "Ze_top": 1,  # Expected end for cutting with is_top
        "Zb_bot": 0,  # Expected begin for cutting with not is_top
        "Ze_bot": 0.5,  # Expected end for cutting with not is_top
    }
)
# 3) No intersection
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 1j,  # First point of cutting line
        "Z2": 1j + 1,  # Seconf point of cutting line
        "Zi": [],  # Expected intersection points
        "Zb_top": None,  # Expected begin for cutting with is_top
        "Ze_top": None,  # Expected end for cutting with is_top
        "Zb_bot": 0,  # Expected begin for cutting with not is_top
        "Ze_bot": 1,  # Expected end for cutting with not is_top
    }
)
# 4) Same case as previous one with reverse Z1 and Z2
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 1j + 1,  # First point of cutting line
        "Z2": 1j,  # Seconf point of cutting line
        "Zi": [],  # Expected intersection points
        "Zb_top": 0,  # Expected begin for cutting with is_top
        "Ze_top": 1,  # Expected end for cutting with is_top
        "Zb_bot": None,  # Expected begin for cutting with not is_top
        "Ze_bot": None,  # Expected end for cutting with not is_top
    }
)
# 5) Cutting point is begin
split_list.append(
    {
        "begin": -1,  # Begin of the segment
        "end": 1j,  # End of the segment
        "Z1": -1 - 1j,  # First point of cutting line
        "Z2": -1 + 1j,  # Seconf point of cutting line
        "Zi": [-1],  # Expected intersection points
        "Zb_top": None,  # Expected begin for cutting with is_top
        "Ze_top": None,  # Expected end for cutting with is_top
        "Zb_bot": -1,  # Expected begin for cutting with not is_top
        "Ze_bot": 1j,  # Expected end for cutting with not is_top
    }
)
# 6) Cutting point is end
split_list.append(
    {
        "begin": -1,  # Begin of the segment
        "end": 1j,  # End of the segment
        "Z1": -1j,  # First point of cutting line
        "Z2": +1j,  # Seconf point of cutting line
        "Zi": [1j],  # Expected intersection points
        "Zb_top": -1,  # Expected begin for cutting with is_top
        "Ze_top": 1j,  # Expected end for cutting with is_top
        "Zb_bot": None,  # Expected begin for cutting with not is_top
        "Ze_bot": None,  # Expected end for cutting with not is_top
    }
)
# 7) Segment is part of the cutting line
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1 + 1j,  # End of the segment
        "Z1": -1 - 1j,  # First point of cutting line
        "Z2": -2 - 2j,  # Seconf point of cutting line
        "Zi": [0, 1 + 1j],  # Expected intersection points
        "Zb_top": 0,  # Expected begin for cutting with is_top
        "Ze_top": 1 + 1j,  # Expected end for cutting with is_top
        "Zb_bot": 0,  # Expected begin for cutting with not is_top
        "Ze_bot": 1 + 1j,  # Expected end for cutting with not is_top
    }
)


class Test_Segment_Split(object):
    """unittest for Segment split methods"""

    @pytest.mark.parametrize("test_dict", split_list)
    def test_intersect(self, test_dict):
        """Check that the intersection is computed correctly"""
        seg = Segment(test_dict["begin"], test_dict["end"])

        # Check intersection
        result = seg.intersect_line(test_dict["Z1"], test_dict["Z2"])
        assert len(result) == len(test_dict["Zi"])
        msg = (
            "Wrong intersection: returned "
            + str(result)
            + ", expected: "
            + str(test_dict["Zi"])
        )
        for ii in range(len(result)):
            assert round(abs(abs(result[ii] - test_dict["Zi"][ii]) - 0), 7) == 0, msg

        # Check split_line
        seg_top, seg_bot = seg.split_line(test_dict["Z1"], test_dict["Z2"])
        assert type(seg_top) == list
        assert type(seg_bot) == list
        # Check top return
        if len(seg_top) > 0:
            assert len(seg_top) == 1
            msg = (
                "Wrong begin for top: returned "
                + str(seg_top[0].begin)
                + ", expected: "
                + str(test_dict["Zb_top"])
            )
            assert (
                round(abs(abs(seg_top[0].begin - test_dict["Zb_top"]) - 0), 7) == 0
            ), msg
            msg = (
                "Wrong end for top: returned "
                + str(seg_top[0].end)
                + ", expected: "
                + str(test_dict["Ze_top"])
            )
            assert (
                round(abs(abs(seg_top[0].end - test_dict["Ze_top"]) - 0), 7) == 0
            ), msg
        else:  # No intersection
            assert test_dict["Zb_top"] is None

        # Check bot return
        if len(seg_bot) > 0:
            assert len(seg_bot) == 1
            msg = (
                "Wrong begin for Bot: returned "
                + str(seg_bot[0].begin)
                + ", expected: "
                + str(test_dict["Zb_bot"])
            )
            assert (
                round(abs(abs(seg_bot[0].begin - test_dict["Zb_bot"]) - 0), 7) == 0
            ), msg
            msg = (
                "Wrong end for Bot: returned "
                + str(seg_bot[0].end)
                + ", expected: "
                + str(test_dict["Ze_bot"])
            )
            assert (
                round(abs(abs(seg_bot[0].end - test_dict["Ze_bot"]) - 0), 7) == 0
            ), msg
        else:  # No intersection
            assert test_dict["Zb_bot"] is None


if __name__ == "__main__":
    a = Test_Segment_Split()
    for ii, test_dict in enumerate(split_list):
        print(ii)
        a.test_intersect(test_dict)
    # a.test_intersect(split_list[5])
    print("Done")
