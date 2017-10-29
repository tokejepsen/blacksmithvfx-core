import pyblish.api


class BlacksmithFtrackExtractComponentLocation(pyblish.api.InstancePlugin):
    """Temporary plugin to fix adding component location

    This plugins will become redundant once updating to latest version of
    pyblish-bumpybox.
    """

    order = pyblish.api.ExtractorOrder + 0.4
    label = "Location"
    families = ["local", "output"]

    def process(self, instance):

        # Setup location
        session = instance.context.data["ftrackSession"]
        location = session.pick_location()

        for data in instance.data.get("ftrackComponentsList", []):
            data["component_location"] = location
