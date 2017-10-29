import pyblish.api


class BlacksmithFtrackExtractSceneComponent(pyblish.api.InstancePlugin):
    """ Appending output files from local extraction as components. """

    order = pyblish.api.ExtractorOrder
    label = "Scene Component"
    families = ["scene"]

    def process(self, instance):

        if "collection" not in instance.data:

            # Add ftrack family
            families = instance.data.get("families", [])
            instance.data["families"] = families + ["ftrack"]

            # Get location
            session = instance.context.data["ftrackSession"]
            location = session.pick_location()

            # Add component
            components = instance.data.get("ftrackComponentsList", [])
            components.append({
                "assettype_data": {"short": "scene"},
                "assetversion_data": {
                    "version": instance.context.data["version"]
                },
                "component_data": {
                    "name": pyblish.api.current_host(),
                },
                "component_path": instance.context.data["currentFile"],
                "component_overwrite": True,
                "component_location": location,
            })
            instance.data["ftrackComponentsList"] = components
