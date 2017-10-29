class mock_entity(dict):
    """Mock entity for faking Ftrack entities
    Requires keyword argument "entity_type" on creation.
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, args)

        if "entity_type" not in kwargs.keys():
            raise ValueError('Need the keyword argument "entity_type"')

        self.__dict__ = kwargs


def get_work_file(session, task, application, version):
    """Gets the assumed path to the work file of the application."""

    extension_mapping = {
        ".hrox": "nukestudio",
        ".nk": "nuke",
        ".mb": "maya",
        ".hip": "houdini"
    }
    extension = None
    for key, value in extension_mapping.iteritems():
        if value == application:
            extension = key

    # Faking an Ftrack component for the location structure.
    entity = mock_entity(
        ("parent", task["parent"]),
        ("project", task["project"]),
        ("version", version),
        ("file_type", extension),
        ("name", task["name"]),
        ("type", task["type"]),
        entity_type="Task"
    )

    location = session.pick_location()
    return location.structure.get_resource_identifier(entity)


workfile_extensions = [".nk", ".mb", ".hip"]

single_files = {
    ".mb": "scene",
    ".ma": "scene",
    ".nk": "scene",
    ".mov": "mov",
    ".abc": "cache"
}

sequence_files = {".exr": "img"}
