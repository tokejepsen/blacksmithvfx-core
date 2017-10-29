import os

import lucidity

from blacksmithvfx_environment import utils


def get_test_paths():
    return [
        "//disk/project_root/test_project",
        "//disk/project_root/test_project/in/elements",
        "//disk/project_root/test_project/in/footage/grade",
        "//disk/project_root/test_project/in/footage/raw",
        "//disk/project_root/test_project/in/roughCuts",
        "//disk/project_root/test_project/in/references/fromClient",
        "//disk/project_root/test_project/in/shoot/scriptNotes",
        "//disk/project_root/test_project/in/shoot/stills",
        "//disk/project_root/test_project/in/GFX",
        "//disk/project_root/test_project/in/assets",
        "//disk/project_root/test_project/in/EDL",
        "//disk/project_root/test_project/in/production/storyboards",
        "//disk/project_root/test_project/in/production/treatment",
        "//disk/project_root/test_project/in/production/script",
        "//disk/project_root/test_project/in/roto",
        "//disk/project_root/test_project/in/audio",
        "//disk/project_root/test_project/out/tracking",
        "//disk/project_root/test_project/out/mattePainting",
        "//disk/project_root/test_project/out/deliverables",
        "//disk/project_root/test_project/out/client",
        "//disk/project_root/test_project/out/cleanUp",
        "//disk/project_root/test_project/out/roto",

        "//disk/project_root/test_project/Tasks/editing",
        "//disk/project_root/test_project/Tasks/editing/Work/nuke/scripts",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/"
        "sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/autosave",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/scripts",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/images",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/data",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/sound",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/particles",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/assets",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "bifrost",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "particles",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "nCache",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/cache/"
        "alembic",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/scenes/"
        "edit",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/clips",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/movies",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/iprImages",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/depth",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furFiles",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furImages",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furShadowMap",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furEqualMap",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/renderData"
        "/fur/furAttrMap",
        "//disk/project_root/test_project/Tasks/editing/Work/flame",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/hip",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/tex",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/geo",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/sim",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/render",
        "//disk/project_root/test_project/Tasks/editing/Publish",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/"
        "workspace.mel",

        "//disk/project_root/test_project/Tasks/editing/Work/nuke/scripts/"
        "Editing_editing_v001.nk",
        "//disk/project_root/test_project/Tasks/editing/Work/maya/scenes/"
        "Editing_editing_v001.mb",
        "//disk/project_root/test_project/Tasks/editing/Work/houdini/hip/"
        "Editing_editing_v001.hip",

        "//disk/project_root/test_project/Tasks/editing/Publish/scene/"
        "editing_instanceName/v001/editing_main_v001.mb",
        "//disk/project_root/test_project/Tasks/editing/Publish/scene/"
        "editing_instanceName/v001/editing_main_v001.ma",
        "//disk/project_root/test_project/Tasks/editing/Publish/scene/"
        "editing_instanceName/v001/editing_main_v001.nk",
        "//disk/project_root/test_project/Tasks/editing/Publish/mov/"
        "editing_instanceName/v001/editing_main_v001.mov",
        "//disk/project_root/test_project/Tasks/editing/Publish/cache/"
        "editing_instanceName/v001/editing_main_v001.abc",

        "//disk/project_root/test_project/Tasks/editing/Publish/img/"
        "editing_instanceName/v001/editing_main_v001.%04d.exr",
        "//disk/project_root/test_project/Tasks/editing/Publish/img/"
        "editing_instanceName/v001/editing_main_v001.1001.exr",

        "//disk/project_root/test_project/Assets",

        "//disk/project_root/test_project/Assets/Character/rat",

        "//disk/project_root/test_project/Assets/Character/rat/lookdev",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "nuke/scripts",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/autosave",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/scripts",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/images",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/data",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/sound",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/particles",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/assets",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/cache/bifrost",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/cache/particles",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/cache/nCache",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/cache/alembic",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/scenes/edit",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/clips",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/movies",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/renderData/iprImages",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/renderData/depth",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/renderData/fur/furFiles",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/renderData/fur/furImages",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/renderData/fur/furShadowMap",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/renderData/fur/furEqualMap",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/renderData/fur/furAttrMap",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "flame",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "houdini/hip",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "houdini/tex",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "houdini/geo",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "houdini/sim",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "houdini/render",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work"
        "/maya/workspace.mel",

        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "nuke/scripts/Lookdev_lookdev_v001.nk",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "maya/scenes/Lookdev_lookdev_v001.mb",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/Work/"
        "houdini/hip/Lookdev_lookdev_v001.hip",

        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish/scene/lookdev_instanceName/v001/"
        "Character_rat_lookdev_main_v001.mb",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish/scene/lookdev_instanceName/v001/"
        "Character_rat_lookdev_main_v001.ma",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish/scene/lookdev_instanceName/v001/"
        "Character_rat_lookdev_main_v001.nk",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish/mov/lookdev_instanceName/v001/"
        "Character_rat_lookdev_main_v001.mov",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish/cache/lookdev_instanceName/v001/"
        "Character_rat_lookdev_main_v001.abc",

        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish/img/lookdev_instanceName/v001/"
        "Character_rat_lookdev_main_v001.%04d.exr",
        "//disk/project_root/test_project/Assets/Character/rat/lookdev/"
        "Publish/img/lookdev_instanceName/v001/"
        "Character_rat_lookdev_main_v001.1001.exr",

        "//disk/project_root/test_project/Shots/sh0010",
        "//disk/project_root/test_project/Shots/sh0010/Footage",

        "//disk/project_root/test_project/Shots/sh0010/animation",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/nuke/"
        "scripts",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "sound",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "clips",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "cache/bifrost",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "cache/particles",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "cache/alembic",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "cache/nCache",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "scenes/edit",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "autosave",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "particles",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "movies",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "renderData/fur/furFiles",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "renderData/fur/furImages",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "renderData/fur/furShadowMap",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "renderData/fur/furAttrMap",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "renderData/fur/furEqualMap",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "renderData/depth",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "renderData/iprImages",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "scripts",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "images",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "data",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "assets",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/flame",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/"
        "houdini/hip",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/"
        "houdini/tex",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/"
        "houdini/geo",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/"
        "houdini/render",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/"
        "houdini/sim",
        "//disk/project_root/test_project/Shots/sh0010/animation/Publish",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "workspace.mel",

        "//disk/project_root/test_project/Shots/sh0010/animation/Work/nuke/"
        "scripts/sh0010_Animation_animation_v001.nk",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/maya/"
        "scenes/sh0010_Animation_animation_v001.mb",
        "//disk/project_root/test_project/Shots/sh0010/animation/Work/houdini/"
        "hip/sh0010_Animation_animation_v001.hip",

        "//disk/project_root/test_project/Shots/sh0010/animation/Publish/"
        "scene/animation_instanceName/v001/sh0010_animation_main_v001.mb",
        "//disk/project_root/test_project/Shots/sh0010/animation/Publish/"
        "scene/animation_instanceName/v001/sh0010_animation_main_v001.ma",
        "//disk/project_root/test_project/Shots/sh0010/animation/Publish/"
        "scene/animation_instanceName/v001/sh0010_animation_main_v001.nk",
        "//disk/project_root/test_project/Shots/sh0010/animation/Publish/"
        "mov/animation_instanceName/v001/sh0010_animation_main_v001.mov",
        "//disk/project_root/test_project/Shots/sh0010/animation/Publish/"
        "cache/animation_instanceName/v001/sh0010_animation_main_v001.abc",

        "//disk/project_root/test_project/Shots/sh0010/animation/Publish/"
        "img/animation_instanceName/v001/sh0010_animation_main_v001.%04d.exr",
        "//disk/project_root/test_project/Shots/sh0010/animation/Publish/"
        "img/animation_instanceName/v001/sh0010_animation_main_v001.1001.exr",

        "//disk/project_root/test_project/Sequences/sq001",

        "//disk/project_root/test_project/Sequences/sq001/editing",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/nuke"
        "/scripts",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/autosave",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/scripts",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/images",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/data",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/sound",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/particles",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/assets",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/cache/bifrost",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/cache/particles",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/cache/nCache",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/cache/alembic",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/scenes/edit",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/clips",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/movies",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/renderData/iprImages",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/renderData/depth",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/renderData/fur/furFiles",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/renderData/fur/furImages",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/renderData/fur/furShadowMap",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/renderData/fur/furEqualMap",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/renderData/fur/furAttrMap",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/flame",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/houdini"
        "/hip",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/houdini"
        "/tex",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/houdini"
        "/geo",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/houdini"
        "/sim",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/houdini"
        "/render",
        "//disk/project_root/test_project/Sequences/sq001/editing/Publish",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/workspace.mel",

        "//disk/project_root/test_project/Sequences/sq001/editing/Work/nuke"
        "/scripts/sq001_Editing_editing_v001.nk",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/maya"
        "/scenes/sq001_Editing_editing_v001.mb",
        "//disk/project_root/test_project/Sequences/sq001/editing/Work/houdini"
        "/hip/sq001_Editing_editing_v001.hip",

        "//disk/project_root/test_project/Sequences/sq001/editing/Publish/"
        "scene/editing_instanceName/v001/sq001_editing_main_v001.mb",
        "//disk/project_root/test_project/Sequences/sq001/editing/Publish/"
        "scene/editing_instanceName/v001/sq001_editing_main_v001.ma",
        "//disk/project_root/test_project/Sequences/sq001/editing/Publish/"
        "scene/editing_instanceName/v001/sq001_editing_main_v001.nk",
        "//disk/project_root/test_project/Sequences/sq001/editing/Publish/"
        "mov/editing_instanceName/v001/sq001_editing_main_v001.mov",
        "//disk/project_root/test_project/Sequences/sq001/editing/Publish/"
        "cache/editing_instanceName/v001/sq001_editing_main_v001.abc",

        "//disk/project_root/test_project/Sequences/sq001/editing/Publish/"
        "img/editing_instanceName/v001/sq001_editing_main_v001.%04d.exr",
        "//disk/project_root/test_project/Sequences/sq001/editing/Publish/"
        "img/editing_instanceName/v001/sq001_editing_main_v001.1001.exr",

        "//disk/project_root/test_project/Sequences/sq001/sh0010",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/Footage",

        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/nuke/scripts",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/sound",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/particles",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/sourceimages/3dPaintTextures",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/cache/bifrost",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/cache/particles",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/cache/nCache",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/cache/alembic",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/scenes/edit",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/autosave",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/clips",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/movies",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/renderData/iprImages",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/renderData/depth",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/renderData/fur/furFiles",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/renderData/fur/furImages",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/renderData/fur/furShadowMap",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/renderData/fur/furEqualMap",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/renderData/fur/furAttrMap",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/scripts",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/images",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/data",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/assets",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/flame",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/houdini/hip",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/houdini/tex",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/houdini/geo",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/houdini/sim",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/houdini/render",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Publish",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing"
        "/Work/maya/workspace.mel",

        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Work/houdini/hip/sq001_sh0010_Compositing_compositing_v001.hip",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Work/maya/scenes/sq001_sh0010_Compositing_compositing_v001.mb",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Work/nuke/scripts/sq001_sh0010_Compositing_compositing_v001.nk",

        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Publish/scene/compositing_instanceName/v001/"
        "sq001_sh0010_compositing_main_v001.mb",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Publish/scene/compositing_instanceName/v001/"
        "sq001_sh0010_compositing_main_v001.ma",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Publish/scene/compositing_instanceName/v001/"
        "sq001_sh0010_compositing_main_v001.nk",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Publish/mov/compositing_instanceName/v001/"
        "sq001_sh0010_compositing_main_v001.mov",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Publish/cache/compositing_instanceName/v001/"
        "sq001_sh0010_compositing_main_v001.abc",

        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Publish/img/compositing_instanceName/v001/"
        "sq001_sh0010_compositing_main_v001.%04d.exr",
        "//disk/project_root/test_project/Sequences/sq001/sh0010/compositing/"
        "Publish/img/compositing_instanceName/v001/"
        "sq001_sh0010_compositing_main_v001.1001.exr",
    ]


def assert_entity(entity):
    templates = lucidity.discover_templates()
    msg = (
        "No valid templates found for template name: \"{0}\", and entity: "
        "\"{1}\"".format(templates[0].get_template_name(entity), entity)
    )
    assert templates[0].get_valid_templates(entity, templates), msg

    get_resolved_paths(entity)


def get_resolved_paths(entity):
    templates = lucidity.discover_templates()
    valid_templates = templates[0].get_valid_templates(entity, templates)
    resolved_paths = []
    for template in valid_templates:
        try:
            resolved_paths.append(template.format(entity))
        except lucidity.error.FormatError as e:
            msg = e.message + "\nTemplate name: {0}".format(template.name)
            raise type(e)(msg)

    return resolved_paths


def test_environment():
    msg = "Could not find \"LUCIDITY_TEMPLATE_PATH\" in environment."
    assert "LUCIDITY_TEMPLATE_PATH" in os.environ.keys(), msg


def test_templates_existence():
    templates = lucidity.discover_templates()
    assert templates, "No templates discovered."


def test_proposed_paths():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    paths = get_test_paths()
    for path in template_paths:
        if path in paths:
            paths.remove(path)

    msg = "Paths not covered by templates:"
    for path in paths:
        msg += "\n{0}".format(path)
    msg += "\nTemplate paths:"
    for path in template_paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def test_unused_templates():
    templates = lucidity.discover_templates()

    used_templates = []
    for entity in get_entities():
        valid_templates = templates[0].get_valid_templates(entity, templates)
        used_templates.extend(valid_templates)

    # Cover templates not used
    unused_templates = list(set(templates) - set(used_templates))
    msg = "Templates not used:"
    for template in unused_templates:
        msg += "\n{0}".format(template)
    assert not unused_templates, msg


def test_excess_templates():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    # Cover excess templates
    paths = []
    for path in template_paths:
        if path not in get_test_paths():
            paths.append(path)

    msg = "Excess template paths:"
    for path in paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def generate_work_file_tasks(parent, project, name, type_name):
    entities = []

    for ext in utils.workfile_extensions:
        task = utils.mock_entity(
            ("parent", parent),
            ("project", project),
            ("version", 1),
            ("file_type", ext),
            ("name", name),
            ("type", {"name": type_name}),
            entity_type="Task"
        )
        entities.append(task)

    return entities


def generate_file_components(task):
    entities = []
    for ext, short in utils.single_files.iteritems():
        assettype = utils.mock_entity(
            ("short", short),
            entity_type="Type"
        )
        asset = utils.mock_entity(
            ("parent", task["parent"]),
            ("type", assettype),
            ("name", "{0}_instanceName".format(task["name"])),
            entity_type="Asset"
        )
        assetversion = utils.mock_entity(
            ("asset", asset),
            ("task", task),
            ("version", 1),
            entity_type="AssetVersion"
        )
        entity = utils.mock_entity(
            ("version", assetversion),
            ("file_type", ext),
            ("name", "main"),
            entity_type="FileComponent"
        )
        entities.append(entity)

    return entities


def generate_sequence_components(task):
    entities = []

    for ext, short in utils.sequence_files.iteritems():
        assettype = utils.mock_entity(
            ("short", short),
            entity_type="Type"
        )
        asset = utils.mock_entity(
            ("parent", task["parent"]),
            ("type", assettype),
            ("name", "{0}_instanceName".format(task["name"])),
            entity_type="Asset"
        )
        assetversion = utils.mock_entity(
            ("asset", asset),
            ("task", task),
            ("version", 1),
            entity_type="AssetVersion"
        )
        entity = utils.mock_entity(
            ("version", assetversion),
            ("name", "main"),
            ("file_type", ext),
            ("padding", 4),
            entity_type="SequenceComponent"
        )
        entities.append(entity)

    return entities


def generate_container_members(containers):
    entities = []
    for container in containers:
        entity = utils.mock_entity(
            ("version", None),
            ("container", container),
            ("file_type", container["file_type"]),
            ("name", "1001"),
            entity_type="FileComponent"
        )
        entities.append(entity)

    return entities


def get_project():
    return utils.mock_entity(
        ("disk", {"windows": "//disk", "unix": "//disk"}),
        ("root", "project_root"),
        ("name", "test_project"),
        entity_type="Project"
    )


def test_project():
    assert_entity(get_project())


def get_project_task():
    project = get_project()
    return utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "editing"),
        entity_type="Task"
    )


def test_project_task():
    assert_entity(get_project_task())


def get_project_task_workfiles():
    project = get_project()
    return generate_work_file_tasks(project, project, "editing", "Editing")


def test_project_task_workfiles():
    for entity in get_project_task_workfiles():
        assert_entity(entity)


def get_project_task_file_components():
    task = get_project_task()
    return generate_file_components(task)


def test_project_task_file_components():
    for entity in get_project_task_file_components():
        assert_entity(entity)


def get_project_task_sequence_components():
    task = get_project_task()
    return generate_sequence_components(task)


def test_project_task_sequence_components():
    for entity in get_project_task_sequence_components():
        assert_entity(entity)


def get_project_task_sequence_files():
    return generate_container_members(
        get_project_task_sequence_components()
    )


def test_project_task_sequence_files():
    for entity in get_project_task_sequence_files():
        assert_entity(entity)


def get_project_folder():
    project = get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "Assets"),
        entity_type="Folder"
    )


def test_project_folder():
    assert_entity(get_project_folder())


def get_project_folder_assetbuild():
    project = get_project()
    parent = get_project_folder()
    assetbuildtype = utils.mock_entity(
        ("name", "Character"),
        entity_type="Type"
    )
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "rat"),
        ("type", assetbuildtype),
        entity_type="AssetBuild"
    )


def test_project_folder_assetbuild():
    assert_entity(get_project_folder_assetbuild())


def get_project_folder_assetbuild_task():
    project = get_project()
    assetbuild = get_project_folder_assetbuild()

    return utils.mock_entity(
        ("project", project),
        ("parent", assetbuild),
        ("name", "lookdev"),
        entity_type="Task"
    )


def test_project_folder_assetbuild_task():
    assert_entity(get_project_folder_assetbuild_task())


def get_project_folder_assetbuild_task_workfiles():
    project = get_project()
    parent = get_project_folder_assetbuild()
    return generate_work_file_tasks(parent, project, "lookdev", "Lookdev")


def test_project_folder_assetbuild_task_workfiles():
    for entity in get_project_folder_assetbuild_task_workfiles():
        assert_entity(entity)


def get_project_folder_assetbuild_task_file_components():
    task = get_project_folder_assetbuild_task()
    return generate_file_components(task)


def test_project_folder_assetbuild_task_file_components():
    for entity in get_project_folder_assetbuild_task_file_components():
        assert_entity(entity)


def get_project_folder_assetbuild_task_sequence_components():
    task = get_project_folder_assetbuild_task()
    return generate_sequence_components(task)


def test_project_folder_assetbuild_task_sequence_components():
    for entity in get_project_folder_assetbuild_task_sequence_components():
        assert_entity(entity)


def get_project_folder_assetbuild_task_sequence_files():
    return generate_container_members(
        get_project_folder_assetbuild_task_sequence_components()
    )


def test_project_folder_assetbuild_task_sequence_files():
    e = get_project_folder_assetbuild_task_sequence_files()
    for entity in e:
        assert_entity(entity)


def get_project_shot():
    project = get_project()

    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "sh0010"),
        entity_type="Shot"
    )


def test_project_shot():
    assert_entity(get_project_shot())


def get_project_shot_task():
    project = get_project()
    parent = get_project_shot()

    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "animation"),
        entity_type="Task"
    )


def test_project_shot_task():
    assert_entity(get_project_shot_task())


def get_project_shot_task_workfiles():
    project = get_project()
    parent = get_project_shot()
    return generate_work_file_tasks(parent, project, "animation", "Animation")


def test_project_shot_task_workfiles():
    for entity in get_project_shot_task_workfiles():
        assert_entity(entity)


def get_project_shot_task_file_components():
    task = get_project_shot_task()
    return generate_file_components(task)


def test_project_shot_task_file_components():
    for entity in get_project_shot_task_file_components():
        assert_entity(entity)


def get_project_shot_task_sequence_components():
    task = get_project_shot_task()
    return generate_sequence_components(task)


def test_project_shot_task_sequence_components():
    for entity in get_project_shot_task_sequence_components():
        assert_entity(entity)


def get_project_shot_task_sequence_files():
    return generate_container_members(
        get_project_shot_task_sequence_components()
    )


def test_project_shot_task_sequence_files():
    for entity in get_project_shot_task_sequence_files():
        assert_entity(entity)


def get_project_sequence():
    project = get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "sq001"),
        entity_type="Sequence"
    )


def test_project_sequence():
    assert_entity(get_project_sequence())


def get_project_sequence_task():
    project = get_project()
    parent = get_project_sequence()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "editing"),
        entity_type="Task"
    )


def test_project_sequence_task():
    assert_entity(get_project_sequence_task())


def get_project_sequence_task_workfiles():
    project = get_project()
    parent = get_project_sequence()
    return generate_work_file_tasks(parent, project, "editing", "Editing")


def test_project_sequence_task_workfiles():
    for entity in get_project_sequence_task_workfiles():
        assert_entity(entity)


def get_project_sequence_task_file_components():
    task = get_project_sequence_task()
    return generate_file_components(task)


def test_project_sequence_task_file_components():
    for entity in get_project_sequence_task_file_components():
        assert_entity(entity)


def get_project_sequence_task_sequence_components():
    task = get_project_sequence_task()
    return generate_sequence_components(task)


def test_project_sequence_task_sequence_components():
    for entity in get_project_sequence_task_sequence_components():
        assert_entity(entity)


def get_project_sequence_task_sequence_files():
    return generate_container_members(
        get_project_sequence_task_sequence_components()
    )


def test_project_sequence_task_sequence_files():
    for entity in get_project_sequence_task_sequence_files():
        assert_entity(entity)


def get_project_sequence_shot():
    project = get_project()
    parent = get_project_sequence()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "sh0010"),
        entity_type="Shot"
    )


def test_project_sequence_shot():
    assert_entity(get_project_sequence_shot())


def get_project_sequence_shot_task():
    project = get_project()
    parent = get_project_sequence_shot()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "compositing"),
        entity_type="Task"
    )


def test_project_sequence_shot_task():
    assert_entity(get_project_sequence_shot_task())


def get_project_sequence_shot_task_workfiles():
    project = get_project()
    parent = get_project_sequence_shot()
    return generate_work_file_tasks(
        parent, project, "compositing", "Compositing"
    )


def test_project_sequence_shot_task_workfiles():
    for entity in get_project_sequence_shot_task_workfiles():
        assert_entity(entity)


def get_project_sequence_shot_task_file_components():
    task = get_project_sequence_shot_task()
    return generate_file_components(task)


def test_project_sequence_shot_task_file_components():
    for entity in get_project_sequence_shot_task_file_components():
        assert_entity(entity)


def get_project_sequence_shot_task_sequence_components():
    task = get_project_sequence_shot_task()
    return generate_sequence_components(task)


def test_project_sequence_shot_task_sequence_components():
    for entity in get_project_sequence_shot_task_sequence_components():
        assert_entity(entity)


def get_project_sequence_shot_task_sequence_files():
    return generate_container_members(
        get_project_sequence_shot_task_sequence_components()
    )


def test_project_sequence_shot_task_sequence_files():
    for entity in get_project_sequence_shot_task_sequence_files():
        assert_entity(entity)


def get_entities():
    entities = []

    entities.append(get_project())

    entities.append(get_project_task())
    entities.extend(get_project_task_workfiles())
    entities.extend(get_project_task_file_components())
    entities.extend(get_project_task_sequence_components())
    entities.extend(get_project_task_sequence_files())

    entities.append(get_project_folder())
    entities.append(get_project_folder_assetbuild())
    entities.append(get_project_folder_assetbuild_task())
    entities.extend(get_project_folder_assetbuild_task_workfiles())
    entities.extend(get_project_folder_assetbuild_task_file_components())
    entities.extend(get_project_folder_assetbuild_task_sequence_components())
    entities.extend(
        get_project_folder_assetbuild_task_sequence_files()
    )

    entities.append(get_project_shot())
    entities.append(get_project_shot_task())
    entities.extend(get_project_shot_task_workfiles())
    entities.extend(get_project_shot_task_file_components())
    entities.extend(get_project_shot_task_sequence_components())
    entities.extend(get_project_shot_task_sequence_files())

    entities.append(get_project_sequence())
    entities.append(get_project_sequence_task())
    entities.extend(get_project_sequence_task_workfiles())
    entities.extend(get_project_sequence_task_file_components())
    entities.extend(get_project_sequence_task_sequence_components())
    entities.extend(
        get_project_sequence_task_sequence_files()
    )

    entities.append(get_project_sequence_shot())
    entities.append(get_project_sequence_shot_task())
    entities.extend(get_project_sequence_shot_task_workfiles())
    entities.extend(get_project_sequence_shot_task_file_components())
    entities.extend(get_project_sequence_shot_task_sequence_components())
    entities.extend(
        get_project_sequence_shot_task_sequence_files()
    )

    return entities
