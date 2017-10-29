import os
import platform

import lucidity
from blacksmithvfx_environment import utils


class Template(lucidity.Template):

    def get_parents(self, entity, parents):
        """Recursive iterate to find all parents.
        For AssetVersion where no parent is present, the asset is assumed as
        parent.
        For SequenceComponent and FileComponent where no parent is present, the
        asset version is assumed as parent.
        """

        try:
            parent = entity["parent"]
            if parent:
                parents.append(parent)
                return self.get_parents(parent, parents)
        except KeyError:
            if entity.entity_type == "AssetVersion":
                parents.append(entity["asset"])
                return self.get_parents(entity["asset"], parents)

            if entity.entity_type == "FileComponent":

                parent = entity["version"]
                # Assuming its in a container, if there are no version.
                if parent:
                    parents.append(entity["version"])
                else:
                    parent = entity["container"]
                    parents.append(entity["container"])
                return self.get_parents(parent, parents)

            if entity.entity_type == "SequenceComponent":
                parents.append(entity["version"])
                return self.get_parents(entity["version"], parents)

        return parents

    def get_entity_type_path(self, entities):
        """Get the entity type path from a list of entities
        The returned path is a list of entity types separated by a path
        separator:
            "[entity_type]/[entity_type]/[entity_type]"
            "Project/Asset/AssetVersion"

        The "short" data member (asset type code) is used for components. This
        results in paths like this:
            Project/Asset/[short]
            Project/Asset/upload

        The "file_type" data member (extension) is used for components. This
        results in paths like this:
            "Project/Asset/[short]/AssetVersion/FileComponent/[file_type]"
            "Project/Asset/upload/AssetVersion/FileComponent/.txt"
        """

        path_items = []
        for entity in entities:
            path_items.append(entity.entity_type)

            try:
                if entity["type"]:
                    path_items.append(entity["type"]["short"])
            except KeyError:
                pass

            try:
                path_items.append(entity["file_type"])
            except KeyError:
                pass

        return "/".join(path_items)

    def get_template_name(self, entity):
        """Convenience method for getting the template name
        The template name is generated from the entity's parents, and their
        entity type.
        """

        entities = list(reversed(self.get_parents(entity, [])))
        entities.append(entity)
        return self.get_entity_type_path(entities)

    def get_valid_templates(self, entity, templates):

        results = []
        template_name = self.get_template_name(entity)
        try:
            template_name = entity["metadata"]["lucidity_template_name"]
        except KeyError:
            pass

        for template in templates:
            if template.name == template_name:
                results.append(template)

        return results

    def format(self, data):

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "AssetVersion":
            version_string = str(data["version"]).zfill(3)
            data["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "FileComponent":
            if data["version"]:
                version_string = str(data["version"]["version"]).zfill(3)
                data["version"]["version"] = version_string
            else:
                version_string = str(
                    data["container"]["version"]["version"]
                ).zfill(3)
                data["container"]["version"]["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "SequenceComponent":
            version_string = str(data["version"]["version"]).zfill(3)
            data["version"]["version"] = version_string

            # "padding" data member needs to be convert from integer to string.
            padding_string = str(data["padding"]).zfill(2)
            data["padding"] = padding_string

        if data.entity_type == "Task" and "version" in data.keys():
            version_string = str(data["version"]).zfill(3)
            data["version"] = version_string

        return os.path.abspath(
            super(Template, self).format(data)
        ).replace("\\", "/")


def register():
    '''Register templates.
    Templates are named according to the entity in the hierarchy,
    they aim to solve paths for.
    For example a template named "Project" is only for paths for the project.
    Nested entity types are specified with a path separator, for example
    "Project/Shot" deals with paths for shots under the project.
    To specify dealing with certain file types, the file types extension is
    added. For example a template named "Project/.nk" deals with Nuke script
    paths under the project.
    It is assumed that asset versions are children of the asset, resulting in a
    path "Project/Asset/AssetVersion".
    '''

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    templates = []

    # Project
    mount = "{disk." + system_name + "}/{root}/{name}"
    templates.extend([
        Template("Project", mount),
        Template("Project", mount + "/in/elements"),
        Template("Project", mount + "/in/footage/grade"),
        Template("Project", mount + "/in/footage/raw"),
        Template("Project", mount + "/in/roughCuts"),
        Template("Project", mount + "/in/references/fromClient"),
        Template("Project", mount + "/in/shoot/scriptNotes"),
        Template("Project", mount + "/in/shoot/stills"),
        Template("Project", mount + "/in/GFX"),
        Template("Project", mount + "/in/assets"),
        Template("Project", mount + "/in/EDL"),
        Template("Project", mount + "/in/production/storyboards"),
        Template("Project", mount + "/in/production/treatment"),
        Template("Project", mount + "/in/production/script"),
        Template("Project", mount + "/in/roto"),
        Template("Project", mount + "/in/audio"),
        Template("Project", mount + "/out/tracking"),
        Template("Project", mount + "/out/mattePainting"),
        Template("Project", mount + "/out/deliverables"),
        Template("Project", mount + "/out/client"),
        Template("Project", mount + "/out/cleanUp"),
        Template("Project", mount + "/out/roto"),
    ])

    # Project/Task
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "Tasks/{name}"
    )
    name = "Project/Task"
    templates.extend(generate_task_templates(name, mount, ""))

    file_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Tasks/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.name}_{name}_v{version.version}{file_type}"
    )
    container_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Tasks/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.name}_{name}_v{version.version}.%{padding}d"
        "{file_type}"
    )
    container_file_mount = (
        "{container.version.task.project.disk." + system_name + "}/"
        "{container.version.task.project.root}/"
        "{container.version.task.project.name}/"
        "Tasks/"
        "{container.version.task.name}/"
        "Publish/"
        "{container.version.asset.type.short}/"
        "{container.version.asset.name}/"
        "v{container.version.version}/"
        "{container.version.task.name}_{container.name}_"
        "v{container.version.version}.{name}{file_type}"
    )
    templates.extend(
        generate_file_templates(
            "Project", file_mount, container_mount, container_file_mount
        )
    )

    # Project/Folder
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "{name}"
    )
    templates.extend([
        Template("Project/Folder", mount),
    ])

    # Project/Folder/AssetBuild
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "{parent.name}/{type.name}/{name}"
    )
    templates.extend([
        Template("Project/Folder/AssetBuild", mount),
    ])

    # Project/Folder/AssetBuild/Task
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "{parent.parent.name}/{parent.type.name}/{parent.name}/{name}"
    )
    name = "Project/Folder/AssetBuild/Task"
    templates.extend(generate_task_templates(name, mount, ""))

    file_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Assets/"
        "{version.task.parent.type.name}/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.type.name}_{version.task.parent.name}_"
        "{version.task.name}_{name}_v{version.version}{file_type}"
    )
    container_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Assets/"
        "{version.task.parent.type.name}/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.type.name}_{version.task.parent.name}_"
        "{version.task.name}_{name}_v{version.version}.%{padding}d{file_type}"
    )
    container_file_mount = (
        "{container.version.task.project.disk." + system_name + "}/"
        "{container.version.task.project.root}/"
        "{container.version.task.project.name}/"
        "Assets/"
        "{container.version.task.parent.type.name}/"
        "{container.version.task.parent.name}/"
        "{container.version.task.name}/"
        "Publish/"
        "{container.version.asset.type.short}/"
        "{container.version.asset.name}/"
        "v{container.version.version}/"
        "{container.version.task.parent.type.name}_"
        "{container.version.task.parent.name}_"
        "{container.version.task.name}_{container.name}_"
        "v{container.version.version}.{name}{file_type}"
    )
    templates.extend(
        generate_file_templates(
            "Project/Folder/AssetBuild",
            file_mount,
            container_mount,
            container_file_mount
        )
    )

    # Project/Shot
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "/Shots/{name}"
    )
    name = "Project/Shot"
    templates.append(Template(name, mount))
    templates.append(Template(name, mount + "/Footage"))

    # Project/Shot/Task
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "/Shots/{parent.name}/{name}"
    )
    name = "Project/Shot/Task"
    templates.extend(generate_task_templates(name, mount, "{parent.name}_"))

    file_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Shots/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.name}_{version.task.name}_{name}_"
        "v{version.version}{file_type}"
    )
    container_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Shots/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.name}_{version.task.name}_{name}_"
        "v{version.version}.%{padding}d{file_type}"
    )
    container_file_mount = (
        "{container.version.task.project.disk." + system_name + "}/"
        "{container.version.task.project.root}/"
        "{container.version.task.project.name}/"
        "Shots/"
        "{container.version.task.parent.name}/"
        "{container.version.task.name}/"
        "Publish/"
        "{container.version.asset.type.short}/"
        "{container.version.asset.name}/"
        "v{container.version.version}/"
        "{container.version.task.parent.name}_{container.version.task.name}_"
        "{container.name}_v{container.version.version}.{name}{file_type}"
    )
    templates.extend(
        generate_file_templates(
            "Project/Shot",
            file_mount,
            container_mount,
            container_file_mount
        )
    )

    # Project/Sequence
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "/Sequences/{name}"
    )
    name = "Project/Sequence"
    templates.append(Template(name, mount))

    # Project/Sequence/Task
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "/Sequences/{parent.name}/{name}"
    )
    name = "Project/Sequence/Task"
    templates.extend(generate_task_templates(name, mount, "{parent.name}_"))

    file_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Sequences/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.name}_{version.task.name}_{name}_"
        "v{version.version}{file_type}"
    )
    container_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Sequences/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.name}_{version.task.name}_{name}_"
        "v{version.version}.%{padding}d{file_type}"
    )
    container_file_mount = (
        "{container.version.task.project.disk." + system_name + "}/"
        "{container.version.task.project.root}/"
        "{container.version.task.project.name}/"
        "Sequences/"
        "{container.version.task.parent.name}/"
        "{container.version.task.name}/"
        "Publish/"
        "{container.version.asset.type.short}/"
        "{container.version.asset.name}/"
        "v{container.version.version}/"
        "{container.version.task.parent.name}_{container.version.task.name}_"
        "{container.name}_v{container.version.version}.{name}{file_type}"
    )
    templates.extend(
        generate_file_templates(
            "Project/Sequence",
            file_mount,
            container_mount,
            container_file_mount
        )
    )

    # Project/Sequence/Shot
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "/Sequences/{parent.name}/{name}"
    )
    name = "Project/Sequence/Shot"
    templates.append(Template(name, mount))
    templates.append(Template(name, mount + "/Footage"))

    # Project/Sequence/Shot/Task
    mount = (
        "{project.disk." + system_name + "}/{project.root}/{project.name}/"
        "/Sequences/{parent.parent.name}/{parent.name}/{name}"
    )
    name = "Project/Sequence/Shot/Task"
    templates.extend(
        generate_task_templates(
            name, mount, "{parent.parent.name}_{parent.name}_"
        )
    )

    file_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Sequences/"
        "{version.task.parent.parent.name}/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.parent.name}_{version.task.parent.name}_"
        "{version.task.name}_{name}_v{version.version}{file_type}"
    )
    container_mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}/"
        "{version.task.project.name}/"
        "Sequences/"
        "{version.task.parent.parent.name}/"
        "{version.task.parent.name}/"
        "{version.task.name}/"
        "Publish/"
        "{version.asset.type.short}/"
        "{version.asset.name}/"
        "v{version.version}/"
        "{version.task.parent.parent.name}_{version.task.parent.name}_"
        "{version.task.name}_{name}_v{version.version}.%{padding}d{file_type}"
    )
    container_file_mount = (
        "{container.version.task.project.disk." + system_name + "}/"
        "{container.version.task.project.root}/"
        "{container.version.task.project.name}/"
        "Sequences/"
        "{container.version.task.parent.parent.name}/"
        "{container.version.task.parent.name}/"
        "{container.version.task.name}/"
        "Publish/"
        "{container.version.asset.type.short}/"
        "{container.version.asset.name}/"
        "v{container.version.version}/"
        "{container.version.task.parent.parent.name}_"
        "{container.version.task.parent.name}_{container.version.task.name}_"
        "{container.name}_v{container.version.version}.{name}{file_type}"
    )
    templates.extend(
        generate_file_templates(
            "Project/Sequence/Shot",
            file_mount,
            container_mount,
            container_file_mount
        )
    )

    return templates


def generate_file_templates(name_prefix,
                            file_mount,
                            container_mount,
                            container_file_mount):

    templates = []

    # FileComponent
    name = name_prefix + "/Asset/{0}/AssetVersion/FileComponent/{1}"
    for ext, short in utils.single_files.iteritems():
        templates.append(Template(name.format(short, ext), file_mount))

    # SequenceComponent
    name = name_prefix + "/Asset/{0}/AssetVersion/SequenceComponent/{1}"
    for ext, short in utils.sequence_files.iteritems():
        templates.append(Template(name.format(short, ext), container_mount))

    # SequenceComponent/FileComponent
    name = (
        name_prefix + "/Asset/{0}/AssetVersion/SequenceComponent/{1}/"
        "FileComponent/{1}"
    )
    for ext, short in utils.sequence_files.iteritems():
        templates.append(
            Template(name.format(short, ext), container_file_mount)
        )

    return templates


def generate_task_templates(name, mount, parents_pattern):

    templates = []

    # Directories
    task_directories = [
        "/Work/maya/sourceimages/3dPaintTextures",
        "/Work/nuke/scripts",
        "/Work/maya/autosave",
        "/Work/maya/scripts",
        "/Work/maya/images",
        "/Work/maya/data",
        "/Work/maya/sound",
        "/Work/maya/particles",
        "/Work/maya/assets",
        "/Work/maya/cache/bifrost",
        "/Work/maya/cache/particles",
        "/Work/maya/cache/nCache",
        "/Work/maya/cache/alembic",
        "/Work/maya/scenes/edit",
        "/Work/maya/clips",
        "/Work/maya/movies",
        "/Work/maya/renderData/iprImages",
        "/Work/maya/renderData/depth",
        "/Work/maya/renderData/fur/furFiles",
        "/Work/maya/renderData/fur/furImages",
        "/Work/maya/renderData/fur/furShadowMap",
        "/Work/maya/renderData/fur/furEqualMap",
        "/Work/maya/renderData/fur/furAttrMap",
        "/Work/flame",
        "/Work/houdini/hip",
        "/Work/houdini/tex",
        "/Work/houdini/geo",
        "/Work/houdini/sim",
        "/Work/houdini/render",
        "/Publish",
    ]

    templates.append(Template(name, mount))
    for directory in task_directories:
        templates.append(Template(name, mount + directory))

    template = Template(name, mount + "/Work/maya/workspace.mel")
    template.source = os.path.join(os.path.dirname(__file__), "workspace.mel")
    templates.append(template)

    # Work files
    templates.extend([
        Template(
            name + "/.hip",
            mount + "/Work/houdini/hip/" + parents_pattern +
            "{type.name}_{name}_v{version}{file_type}"
        ),
        Template(
            name + "/.mb",
            mount + "/Work/maya/scenes/" + parents_pattern +
            "{type.name}_{name}_v{version}{file_type}"
        ),
        Template(
            name + "/.nk",
            mount + "/Work/nuke/scripts/" + parents_pattern +
            "{type.name}_{name}_v{version}{file_type}"
        ),
    ])

    return templates
