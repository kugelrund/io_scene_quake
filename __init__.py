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
dem5_3_fullbright = np.loadtxt(os.path.join(path, 'dem5_3.txt'))
tlight05_fullbright = np.loadtxt(os.path.join(path, 'tlight05.txt'))
tlight10_fullbright = np.loadtxt(os.path.join(path, 'tlight10.txt'))
light1_1_fullbright = np.loadtxt(os.path.join(path, 'light1_1.txt'))
light1_2_fullbright = np.loadtxt(os.path.join(path, 'light1_2.txt'))
light1_3_fullbright = np.loadtxt(os.path.join(path, 'light1_3.txt'))
light1_5_fullbright = np.loadtxt(os.path.join(path, 'light1_5.txt'))
light1_7_fullbright = np.loadtxt(os.path.join(path, 'light1_7.txt'))
light3_5_fullbright = np.loadtxt(os.path.join(path, 'light3_5.txt'))
light3_6_fullbright = np.loadtxt(os.path.join(path, 'light3_6.txt'))
light3_7_fullbright = np.loadtxt(os.path.join(path, 'light3_7.txt'))
light3_8_fullbright = np.loadtxt(os.path.join(path, 'light3_8.txt'))
window1_2_fullbright = np.loadtxt(os.path.join(path, 'window1_2.txt'))
window03_fullbright = np.loadtxt(os.path.join(path, 'window03.txt'))
flame_fullbright = np.loadtxt(os.path.join(path, 'flame.txt'))
flame2_fullbright = np.loadtxt(os.path.join(path, 'flame2.txt'))

config = {
    "do_materials": True,
    "use_lightmap": False,
    "hide_view_entity": True,
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
            "cam_strength": 10,
            "strength": 1000,
            "force_fullbright": flame_fullbright,
            "flicker": 2.0,
            "tint": [1, 0.655, 0.355, 1.0],
            "flame_triset0": {
                "point_light": True,
            },
            "flame_triset1": {
                "point_light": True,
            },
            "flame_triset2": {
                "point_light": True,
            },
            "flame_triset3": {
                "point_light": True,
            },
            "flame_triset4": {
                "point_light": True,
            },
            "flame_triset6": {
                "point_light": True,
            },
        },
        "flame2": {
            "cam_strength": 10,
            "strength": 3000,
            "force_fullbright": flame2_fullbright,
            "point_light": True,
            "flicker": 2.0,
            "tint": [1, 0.655, 0.355, 1.0],
        },
        "lavaball": {
            "cam_strength": 5,
            "strength": 1000,
            "point_light": True,
            "tint": [1, 0.213, 0.037],
            "flicker": 1.0,
        },
        "missile": {
            "cam_strength": 10,
            "strength": 10,
            "missile_triset0": {
                "point_light": True,
                "flicker": 1.0,
                "tint": [1, 0.5, 0.25],
                "strength": 3000,  # rocket fire trail
            },
        },
        "laser": {
            "cam_strength": 3,
            "strength": 3,
            "point_light": True,
            "flicker": 1.0,
            "tint": [1, 0.2, 0.0],
            "strength": 1000,
        },
        "k_spike": {
            "cam_strength": 4,
            "strength": 4,
            "point_light": True,
            "flicker": 1.0,
            "tint": [1, 0.3, 0.0],
            "strength": 500,
        },
        "grenade": {
            "strength": 100,  # grenade glow
        },
        "v_shot": {
            "cam_strength": 5,
            "strength": 5,
            "v_shot_triset0": {
                "anim_interpolation": 'CONSTANT',  # muzzle flash
                "point_light": True,
                "point_light_hide_in_pose": [0, 2, 3, 4, 5, 6, 7],
                "tint": [1, 0.5, 0.25],
                "strength": 500,
            },
        },
        "v_shot2": {
            "cam_strength": 5,
            "strength": 5,
            "v_shot2_triset4": {
                "anim_interpolation": 'CONSTANT',  # muzzle flash
                "point_light": True,
                "point_light_hide_in_pose": [0, 2, 3, 4, 5, 6, 7],
                "tint": [1, 0.5, 0.25],
                "strength": 500,
            },
        },
        "v_nail": {
            "cam_strength": 5,
            "strength": 5,
            "v_nail_triset0": {
                "anim_interpolation": 'CONSTANT',  # muzzle flash
                "point_light": True,
                "point_light_hide_in_pose": [0, 3, 4, 5, 6, 7],
                "tint": [1, 0.5, 0.25],
                "strength": 500,
            },
        },
        "v_nail2": {
            "cam_strength": 5,
            "strength": 5,
            "v_nail_triset5": {
                "anim_interpolation": 'CONSTANT',  # muzzle flash
                "point_light": True,
                "point_light_hide_in_pose": [0],
                "tint": [1, 0.5, 0.25],
                "strength": 500,
            },
        },
        "v_rock": {
            "cam_strength": 5,
            "strength": 5,
            "v_rock_triset1": {
                "anim_interpolation": 'CONSTANT',  # muzzle flash
                "point_light": True,
                "point_light_hide_in_pose": [0, 2, 3, 4, 5, 6, 7],
                "tint": [1, 0.5, 0.25],
                "strength": 500,
            },
        },
        "v_rock2": {
            "cam_strength": 5,
            "strength": 5,
            "v_rock2_triset0": {
                "anim_interpolation": 'CONSTANT',  # muzzle flash
                "point_light": True,
                "point_light_hide_in_pose": [0, 2, 3, 4, 5, 6, 7],
                "tint": [1, 0.5, 0.25],
                "strength": 500,
            },
        },
        #"player": {
        #    "strength": 100,  # muzzle flash
        #},
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
                "*water0": {
                    "opacity": 0.5,
                },
                "*04water1": {
                    "opacity": 0.5,
                },
                "*04awater1": {
                    "opacity": 0.5,
                },
                "*04mwat1": {
                    "opacity": 0.5,
                },
                "*04mwat2": {
                    "opacity": 0.5,
                },
                "*slime": {
                    "opacity": 0.75,
                },
                "*lava1": {
                    "strength": 30,
                },
                "*teleport": {
                    "strength": 3000,
                    "cam_strength": 5,
                    "force_fullbright": True,
                    "sample_as_light": True,
                },
                "key03_1": {
                    "strength": 200,
                    "sample_as_light": True,
                },
                "key03_02": {
                    "strength": 200,
                    "sample_as_light": True,
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
                "light1_3": {
                    "strength": 100,
                    "force_fullbright": light1_3_fullbright,
                    "tint_hsv": [0.5, 0.85, 1],
                },
                "light1_4": {
                    "strength": 250,
                    "force_fullbright": light1_7_fullbright,
                    "sample_as_light": True,
                },
                "light1_5": {
                    "strength": 250,
                    "force_fullbright": light1_5_fullbright,
                    "sample_as_light": True,
                },
                "light1_7": {
                    "strength": 250,
                    "force_fullbright": light1_7_fullbright,
                },
                "light1_8": {
                    "cam_strength": 1.5,
                    "strength": 300,
                    "tint_hsv": [0.5, 0.9, 1],
                    "force_fullbright": light1_7_fullbright,
                },
                "light3_3": {
                    "strength": 250,
                    "force_fullbright": light1_7_fullbright,
                },
                "light3_5": {
                    "cam_strength": 5,
                    "strength": 250,
                    "force_fullbright": light3_5_fullbright,
                    "sample_as_light": True,
                },
                "light3_6": {
                    "cam_strength": 5,
                    "strength": 250,
                    "force_fullbright": light3_6_fullbright,
                    "sample_as_light": True,
                },
                "light3_7": {
                    "cam_strength": 5,
                    "strength": 250,
                    "force_fullbright": light3_7_fullbright,
                    "sample_as_light": True,
                },
                "light3_8": {
                    "strength": 250,
                    "force_fullbright": light3_8_fullbright,
                    "sample_as_light": True,
                },
                "dem5_3": {
                    "strength": 500,
                    "force_fullbright": dem5_3_fullbright,
                    "sample_as_light": True,
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
                "sky1": {
                    "strength": 100,
                    "tint_hsv": (0.5, 0.6666666, 1),
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
                    "strength": 1500,
                    "tint": [1, 0.8, 1, 1],
                    "sample_as_light": True,
                },
                "tlight02": {
                    "strength": 150,
                    "sample_as_light": True,
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
                    "strength": 1000,
                    "force_fullbright": window03_fullbright,
                    "tint_hsv": [0.5, 0.5, 1],
                    "sample_as_light": True,
                },
                "window1_2": {
                    "strength": 1000,
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
        "e1m6": {
            "textures": {
                "*lava1": {
                    "sample_as_light": True,
                },
            }
        },
        "e1m8": {
            "textures": {
                "*lava1": {
                    "sample_as_light": True,
                },
            }
        },
        "e2m1": {
            "textures": {
                "tlight07": {
                    "strength": 500,
                    "sample_as_light": True,
                },
                "sky4": {
                    "strength": 0,
                    "cam_strength": 0,
                },
            }
        },
        "e2m2": {
            "textures": {
                "window01_2": {
                    "sample_as_light": True,
                },
                "window01_3": {
                    "sample_as_light": True,
                },
                "wizwin1_2": {
                    "sample_as_light": True,
                },
            }
        },
        "e3m3": {
            "textures": {
                "*lava1": {
                    "strength": 50,
                },
                "metal6_3": {
                    "sample_as_light": True,
                },
                "sky4": {
                    "strength": 100,
                },
            }
        },
        "e3m4": {
            "textures": {
                "light1_8": {
                    "sample_as_light": True,
                },
                "light3_3": {
                    "sample_as_light": True,
                },
                "light3_8": {
                    "strength": 500,
                },
            }
        },
        "e3m5": {
            "textures": {
                "light1_8": {
                    "sample_as_light": True,
                },
            }
        },
        "e4m2": {
            "textures": {
                "window03": {
                    "strength": 300,
                    "force_fullbright": window03_fullbright,
                    "sample_as_light": True,
                },
            }
        },
        "e4m3": {
            "textures": {
                "*lava1": {
                    "strength": 10,
                },
            }
        },
        "e4m4": {
            "textures": {
                "light1_1": {
                    "sample_as_light": True,
                },
            }
        },
        "e4m6": {
            "textures": {
                "light1_3": {
                    "sample_as_light": True,
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
        with open(self.filepath, 'rb') as demo_file:
            pyquake.blenddemo.add_demo(demo_file, fs, config, self.fps, fov=130)
        render_fps = 60
        assert (self.fps / render_fps).is_integer()
        context.scene.sync_mode = 'FRAME_DROP'
        context.scene.render.engine = 'CYCLES'
        context.scene.cycles.device = 'GPU'
        context.scene.cycles.use_animated_seed = True
        context.scene.frame_step = int(self.fps / render_fps)
        context.scene.render.fps = self.fps
        context.scene.render.resolution_x = 2560
        context.scene.render.resolution_y = 1080
        context.scene.render.use_motion_blur = True
        context.scene.render.motion_blur_shutter *= self.fps / render_fps
        context.scene.render.use_persistent_data = True
        context.scene.world.cycles.homogeneous_volume = True

        context.scene.render.use_overwrite = False
        context.scene.render.image_settings.color_mode = 'RGB'
        context.scene.render.image_settings.color_depth = '16'

        world_material = context.scene.world.node_tree
        world_material.links.clear()
        world_material.nodes.clear()
        node_output = world_material.nodes.new('ShaderNodeOutputWorld')
        node_volume = world_material.nodes.new('ShaderNodeVolumePrincipled')
        node_volume.inputs['Density'].default_value = 0.02
        world_material.links.new(node_volume.outputs[0], node_output.inputs['Volume'])

        return {'FINISHED'}


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
