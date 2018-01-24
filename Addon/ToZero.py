bl_info = {
    "name": "ToZero",
    "category": "T",
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

def register():
    bpy.utils.register_class(ObjectToZero)


def unregister():
    bpy.utils.unregister_class(ObjectToZero)


if __name__ == "__main__":
    register()
