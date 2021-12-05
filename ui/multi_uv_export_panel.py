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

# Standard
import os
import re

# Community
import bpy

# Custom
from ..helper_functions import combine_folder_and_file


class MultiUVExportPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""

    bl_idname = "OBJECT_PT_MULTI_UV_EXPORT"
    bl_label = "Export Multiple UVs"
    bl_category = "Misc"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def _files_to_overwrite(self, objects, folder, file_extention):
        results = []

        for obj in bpy.context.selected_objects:
            if obj.type != "MESH":
                continue

            full_relative_path = (
                combine_folder_and_file(folder, obj.name) + "." + file_extention
            )
            full_abs_path = bpy.path.abspath(full_relative_path)
            if os.path.exists(full_abs_path):
                filename = re.split(r"[/\\]", full_abs_path)[-1]
                results.append(filename)

        return results

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scn = context.scene

        # Options
        col = layout.column()
        col.prop(scn.multi_uv_export, "folder")
        col.prop(scn.multi_uv_export, "image_format")
        col.prop(scn.multi_uv_export, "opacity")

        # Check what files will be overwritten if run and show a warning
        overwritten_files = self._files_to_overwrite(
            objects=list(bpy.context.selected_objects),
            folder=context.scene.multi_uv_export.folder,
            file_extention=context.scene.multi_uv_export.image_format.lower(),
        )
        if len(overwritten_files) > 0:
            col.label(text="You will overwrite the following files:", icon="ERROR")
            for file in overwritten_files[0:5]:
                col.label(text=file)
            if len(overwritten_files) > 5:
                col.label(text="And more!")

        # Run button
        col.operator("multi_uv_export.run")
