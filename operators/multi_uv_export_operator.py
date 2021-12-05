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
import copy

# Community
import bpy

# Custom
from ..helper_functions import combine_folder_and_file


class MultiUVExportOperator(bpy.types.Operator):
    bl_idname = "multi_uv_export.run"
    bl_label = "Export Multiple UVs"

    def execute(self, context):

        # Get all the selected objects
        sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == "MESH"]

        # Save the original selection state of all objects
        before_selected_objs = copy.copy(bpy.context.selected_objects)
        before_active_obj = bpy.context.view_layer.objects.active

        # Remove everything from selection
        bpy.ops.object.select_all(action="DESELECT")

        # Loop through each object and export its UVs
        for obj in sel_objs:
            # Select the current object
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj

            # Export layout to folder
            folder = context.scene.multi_uv_export.folder
            mode = context.scene.multi_uv_export.image_format.upper()
            opacity = context.scene.multi_uv_export.opacity
            filename = combine_folder_and_file(folder, obj.name)
            bpy.ops.uv.export_layout(
                export_all=True,
                filepath=bpy.path.abspath(filename),
                mode=mode,
                opacity=opacity,
            )

            # Deselect the current object
            obj.select_set(False)

        # Restore the original selection
        for obj in before_selected_objs:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = before_active_obj

        # Warn if nothing was selected, meaning nothing was done
        if len(sel_objs) == 0:
            self.report({"WARNING"}, "Nothing selected")
        else:
            self.report({"INFO"}, "Done exporting UVs")

        return {"FINISHED"}
