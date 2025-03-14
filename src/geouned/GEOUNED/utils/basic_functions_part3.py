import FreeCAD, Part


def save_auxiliary_plane(output_filename, surface, shape):
    # make bounding box
    # Create a box with dimensions (Length, Width, Height)
    box = Part.makeBox(10, 20, 30)
    x = 0
    y = 0
    z = 0

    bbox = shape.Shape.BoundBox

    box.Placement.Base = FreeCAD.Vector(x, y, z)

    Part.export([box], output_filename)
