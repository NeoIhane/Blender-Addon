bl_info = {
    "name": "ToZero",
    "category": "Objects",
}

import bpy


class ObjectToZero(bpy.types.Operator):
    """Object To Zero"""
    bl_idname = "object.to_zero"
    bl_label = "ToZero"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        print("To The Zero")
        
        scene = context.scene
        obj = scene.objects.active
        
        obj.location.x=0;
        obj.location.y=0;
        obj.location.z=0;
        
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(ObjectToZero.bl_idname)

def register():
    bpy.utils.register_class(ObjectToZero)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(ObjectToZero)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
