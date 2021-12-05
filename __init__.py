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

bl_info = {
    "name": "Multi UV Export",
    "description": "A simple addon to export UV layouts of multiple objects at the same time.",
    "author": "Hrólfur Gylfason",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "category": "UV",
    "location": "View 3D > Sidebar > Misc Tab",
    "wiki_url": "https://github.com/hrolfurgylfa/Blender-Multi-UV-Export",
    "tracker_url": "https://github.com/hrolfurgylfa/Blender-Multi-UV-Export/issues",
}

# Community
import bpy

# Custom
from .properties import MultiUVExportProperties
from .operators import MultiUVExportOperator
from .ui import MultiUVExportPanel


classes = (
    MultiUVExportProperties,
    MultiUVExportOperator,
    MultiUVExportPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.multi_uv_export = bpy.props.PointerProperty(
        type=MultiUVExportProperties
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.multi_uv_export


if __name__ == "__main__":
    register()
