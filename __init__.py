bl_info = {
    "name": "Quake Demo Importer",
    "author": "Sphere",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "File > Import > Quake demo",
    "description": "Import Quake demo",
    "category": "Import"}

import os

import numpy as np
import pyquake.blenddemo
import pyquake.blendmdl
import pyquake.blendbsp
from pyquake import pak

import bpy
import bpy.ops
import bpy.props
import bpy_extras

path = os.path.join(os.path.dirname(__file__), 'extra_fullbright')
tlight05_fullbright = np.loadtxt(os.path.join(path, 'tlight05.txt'))
tlight10_fullbright = np.loadtxt(os.path.join(path, 'tlight10.txt'))
light1_1_fullbright = np.loadtxt(os.path.join(path, 'light1_1.txt'))
light1_2_fullbright = np.loadtxt(os.path.join(path, 'light1_2.txt'))
light1_5_fullbright = np.loadtxt(os.path.join(path, 'light1_5.txt'))
light1_7_fullbright = np.loadtxt(os.path.join(path, 'light1_7.txt'))
light3_5_fullbright = np.loadtxt(os.path.join(path, 'light3_5.txt'))
light3_6_fullbright = np.loadtxt(os.path.join(path, 'light3_6.txt'))
light3_7_fullbright = np.loadtxt(os.path.join(path, 'light3_7.txt'))
light3_8_fullbright = np.loadtxt(os.path.join(path, 'light3_8.txt'))
window1_2_fullbright = np.loadtxt(os.path.join(path, 'window1_2.txt'))
window03_fullbright = np.loadtxt(os.path.join(path, 'window03.txt'))

config = {
    "do_materials": True,
    "use_lightmap": False,
    "hide_view_entity": False,
    "models": {
        "__default__": {
            "sample_as_light": False,
            "tint": [1, 1, 1, 1],
            "tint_hsv": [0.5, 1, 1],
            "force_fullbright": False,
            "strength": 1,
            "cam_strength": 1,
            "bbox": [[-1024, -1024, -1024], [1024, 1024, 1024]],
            "shade_smooth": True,
        },
        "m_g_key": {
            "strength": 100,
            "force_fullbright": True,
        },
        "w_s_key": {
            "force_fullbright": True,
        },
        "flame": {
            "sample_as_light": True,
            "strength": 5000,
        },
        "flame2": {
            "sample_as_light": True,
            "strength": 5000,
        },
        "lavaball": {
            "strength": 1000,
        },
        "missile": {
            "strength": 5000,  # rocket fire trail
            "cam_strength": 2,
        },
        "grenade": {
            "strength": 100,  # grenade glow
        },
        "player": {
            "strength": 100,  # muzzle flash
        },
    },
    "maps": {
        "__default__": {
            "fullbright_object_overlay": True,
            "textures": {
                "__default__": {
                    "strength": 50,
                    "cam_strength": 1,
                    "sample_as_light": False,
                    "emission_sampling_default": "NONE",
                    "emission_sampling_inside_pvs": "FRONT",
                    "emission_sampling_outside_pvs": "NONE",
                    "tint": [1, 1, 1, 1],
                    "tint_hsv": [0.5, 1, 1],
                    "force_fullbright": False,
                    "overlay": True,
                    "bbox": [[-1024, -1024, -1024], [1024, 1024, 1024]],
                },
                "+0basebtn": {
                    "strength": 250,
                },
                "*lava1": {
                    "strength": 100,
                },
                "*teleport": {
                    "strength": 5000,
                    "cam_strength": 5,
                    "force_fullbright": True,
                },
                "key03_02": {
                    "strength": 200,
                },
                "light1_1": {
                    "strength": 250,
                    "force_fullbright": light1_1_fullbright,
                    "tint_hsv": [0.5, 0.75, 1],
                },
                "light1_2": {
                    "strength": 1000,
                    "force_fullbright": light1_2_fullbright,
                    "tint_hsv": [0.5, 0.333, 1],
                },
                "light1_4": {
                    "strength": 250,
                    "force_fullbright": light1_7_fullbright,
                },
                "light1_5": {
                    "strength": 250,
                    "force_fullbright": light1_5_fullbright,
                },
                "light1_7": {
                    "strength": 250,
                    "force_fullbright": light1_7_fullbright,
                },
                "light1_8": {
                    "strength": 250,
                    "force_fullbright": light1_7_fullbright,
                },
                "light3_3": {
                    "strength": 250,
                    "force_fullbright": light1_7_fullbright,
                },
                "light3_5": {
                    "strength": 250,
                    "force_fullbright": light3_5_fullbright,
                },
                "light3_6": {
                    "strength": 250,
                    "force_fullbright": light3_6_fullbright,
                },
                "light3_7": {
                    "strength": 250,
                    "force_fullbright": light3_7_fullbright,
                },
                "light3_8": {
                    "strength": 250,
                    "force_fullbright": light3_8_fullbright,
                },
                "+0_med25": {
                    "strength": 100,
                },
                "+0_med25s": {
                    "strength": 100,
                },
                "med3_0": {
                    "strength": 100,
                },
                "med3_1": {
                    "strength": 100,
                },
                "+3_med100": {
                    "strength": 100,
                },
                "nail1sid": {
                    "strength": 100,
                },
                "nail1top": {
                    "strength": 100,
                },
                "metal6_3": {
                    "strength": 50,
                },
                "rune_a": {
                    "strength": 50,
                },
                "sky4": {
                    "strength": 50,
                    "tint_hsv": (0.5, 0.5, 1),
                },
                "sliplite": {
                    "strength": 100,
                },
                "slipside": {
                    "strength": 100,
                },
                "switch_1": {
                    "strength": 100,
                },
                "tlight01": {
                    "strength": 2000,
                    "tint": [1, 0.8, 1, 1],
                    "sample_as_light": True,
                },
                "tlight02": {
                    "strength": 500,
                },
                "tlight05": {
                    "strength": 1000,
                    "force_fullbright": tlight05_fullbright,
                },
                "tlight07": {
                    "strength": 1000,
                    "tint": [1, 1, 3.33, 1],
                },
                "tlight10": {
                    "strength": 500,
                    "tint": [1, 0.85, 0.7, 1],
                    "force_fullbright": tlight10_fullbright,
                },
                "tlight11": {
                    "strength": 500,
                    "tint": [1, 0.85, 0.7, 1],
                },
                "window01_1": {
                    "strength": 500,
                    "force_fullbright": True,
                },
                "window01_2": {
                    "strength": 500,
                    "force_fullbright": True,
                },
                "window01_3": {
                    "strength": 100,
                    "force_fullbright": True,
                },
                "window02_1": {
                    "strength": 100,
                    "force_fullbright": True,
                },
                "window03": {
                    "strength": 500,
                    "force_fullbright": window03_fullbright,
                    "tint_hsv": [0.5, 0.5, 1],
                },
                "window1_2": {
                    "strength": 1500,
                    "force_fullbright": window1_2_fullbright,
                    "sample_as_light": True,
                },
                "window1_3": {
                    "strength": 500,
                    "force_fullbright": window1_2_fullbright,
                },
                "wizwin1_2": {
                    "strength": 1500,
                    "force_fullbright": window1_2_fullbright,
                },
            }
        },
        "e4m7": {
            "textures": {
                "light1_2": {
                    "sample_as_light": True,
                },
            }
        },
    }
}


class ImportQuakeDemo(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    bl_idname = "import_scene.quakedem"
    bl_label = "Import Quake demo"
    bl_description = "Opens a Quake demo"
    bl_options = {'UNDO'}

    filename_ext = ".dem"
    filter_glob: bpy.props.StringProperty(default="*.dem", options={'HIDDEN'})
    filepath: bpy.props.StringProperty(name="File path")
    fps: bpy.props.IntProperty(name="FPS",
                               description="Framerate to use for import.",
                               default=360)

    def error(self, msg):
        self.report({'ERROR'}, msg)

    def execute(self, context):
        preferences = context.preferences.addons[__name__].preferences
        fs = pak.Filesystem(preferences.pak_directory)
        if "dem" in self.filepath:
            with open(self.filepath, 'rb') as demo_file:
                pyquake.blenddemo.add_demo(demo_file, fs, config, self.fps)
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Selected file does not contain 'wow'!")
            return {'CANCELLED'}


class ImportQuakePreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    pak_directory: bpy.props.StringProperty(
        name=".pak directory",
        description="Path to directory containing Quake's pak0.pak file",
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "pak_directory")


def menu_import(self, context):
    self.layout.operator(ImportQuakeDemo.bl_idname, text="Quake demo")


def register():
    bpy.utils.register_class(ImportQuakeDemo)
    bpy.utils.register_class(ImportQuakePreferences)
    bpy.types.TOPBAR_MT_file_import.append(menu_import)


def unregister():
    bpy.utils.unregister_class(ImportQuakeDemo)
    bpy.utils.unregister_class(ImportQuakePreferences)
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)


if __name__ == "__main__":
    unregister()
    register()
