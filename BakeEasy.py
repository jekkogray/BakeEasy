import bpy


class CreateImageButton(bpy.types.Operator):
    bl_idname = "editor.createimage"
    bl_label = "Create Image Node"

    def execute(self, context):
        active_mat = context.object.active_material.node_tree
        nodes = active_mat.nodes
        image_node = nodes.new("TextureNodeImage", image=bpy.ops.image.new(name=active_mat.name, width=1024, height=1024, color=(
            0.0, 0.0, 0.0, 1.0), alpha=False, generated_type='BLANK', float=False, use_stereo_3d=False, tiled=False))
        image_node.location = (100, 100)
        return {'FINISHED'}


class CreateUVMapsButton(bpy.types.Operator):
    bl_idname = "editor.createuvmaps"
    bl_label = "Create Smart UV And Projection UV"

    def execute(self, context):

        if (len(context.object.data.uv_layers) == 0):
            bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.0,
                                     user_area_weight=0.0, use_aspect=True, stretch_to_bounds=True)
            context.object.data.uv_layers["UVMap"].name = "SmartUV"
            
            bpy.ops.uv.project_from_view(orthographic=False, camera_bounds=True,
                                         correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)
            context.object.data.uv_layers["UVMap"].name = "ProjectUV"
            return {'FINISHED'}

        # Remove everything 
        if "SmartUV" and "ProjectUV" not in context.object.data.uv_layers:
            context.object.data.uv_textures[len(context.object.data.uv_layers)].active = True
            for i in range (0, len(context.object.data.uv_layers)):
                bpy.ops.uv_texture_remove()

            bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.0,
                                     user_area_weight=0.0, use_aspect=True, stretch_to_bounds=True)
            context.object.data.uv_layers["UVMap"].name = "SmartUV"
            bpy.ops.object.editmode_toggle()
            bpy.ops.uv.project_from_view(orthographic=False, camera_bounds=True,
                                         correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)
            context.object.data.uv_layers["UVMap"].name = "ProjectUV"


            return {'FINISHED'}
        



class BakeEasyPanel(bpy.types.Panel):
    bl_label = "Bake Easy Panel"
    bl_idname = "_PT_BakeEasyPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'baking'

    #context is defined
    def draw(self, context):
        layout = self.layout
        layout.operator("editor.createuvmaps", text="Create UV Map")
        layout.operator("editor.createimage", text="Create Image Node")


def register():
    bpy.utils.register_class(CreateUVMapsButton)
    bpy.utils.register_class(CreateImageButton)
    bpy.utils.register_class(BakeEasyPanel)


def unregister():
    bpy.utils.unregister_class(CreateUVMapsButton)
    bpy.utils.unregister_class(CreateImageButton)
    bpy.utils.unregister_class(BakeEasyPanel)


if __name__ == "__main__":
    register()
