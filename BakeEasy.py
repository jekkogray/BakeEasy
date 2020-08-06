import bpy
class CreateImageButton(bpy.types.Operator):
    bl_idname = "scene.createimage" 
    bl_label = "Create Image Node"

    def execute(self, context):
        active_mat = context.object.active_material.node_tree
        nodes =  active_mat.nodes 
        image_node = nodes.new ("TextureNodeImage", image=bpy.ops.image.new(name=active_mat.name, width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=False, generated_type='BLANK', float=False, use_stereo_3d=False, tiled=False))
        image_node.location = (100, 100)
        return {'FINISHED'}

class CreateUVMapsButton(bpy.types.Operator):
    bl_idname = "scene.createuvmaps" 
    bl_label = "Create Smart UV And Projection UV" 

    def execute(self, context): 
        if (len(context.object.data.uv_layers) == 0):
            bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.0, user_area_weight=0.0, use_aspect=True, stretch_to_bounds=True)
            context.object.data.uv_layers["UVMap"].name = "SmartUV"    
            return {'FINISHED'}

        ## Remove everything but SmartUV and ProjectUV
        context.object.data.uv_layers = [x for x in context.object.data.uv_layers if x == "SmartUV" or x == "ProjectUV"]
        if (len(context.object.data.uv_layers) == 0):
            bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.0, user_area_weight=0.0, use_aspect=True, stretch_to_bounds=True)
            context.object.data.uv_layers["UVMap"].name = "SmartUV"    
            return {'FINISHED'}
        return {'FINISHED'}

        
class BakeEasyPanel(bpy.types.Panel):
    bl_label = "Bake Easy Panel"
    bl_idname = "_PT_BakeEasyPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type ='UI'
    bl_category = 'baking'
    
    #context is defined
    def draw(self, context): 
        layout = self.layout
        layout.operator("scene.createuvmaps", text="Create UV Map")
        layout.operator("scene.createimage", text="Create Node") 
  
        
          
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
    