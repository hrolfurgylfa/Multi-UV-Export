"""
Multi UV Export, a simple blender addon to export UV layouts of multiple
objects at the same time. 
Copyright (C) 2021 Hrólfur Gylfason

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# Community
import bpy


class MultiUVExportProperties(bpy.types.PropertyGroup):
    image_format: bpy.props.EnumProperty(
        items=[
            ("png", "PNG", "Export UVs as a PNG", "", 1),
            ("svg", "SVG", "Export UVs as a SVG", "", 2),
            ("eps", "EPS", "Export UVs as a EPS", "", 3),
        ],
        name="Format",
        description="Image format for the exported UVs",
        default="png",
    )
    opacity: bpy.props.FloatProperty(
        name="Opacity",
        description="Opacity of the exported UVs",
        default=1.0,
        min=0,
        max=1,
    )
    folder: bpy.props.StringProperty(
        name="Path",
        description="Path to Directory",
        default="//",
        maxlen=1024,
        subtype="DIR_PATH",
    )
