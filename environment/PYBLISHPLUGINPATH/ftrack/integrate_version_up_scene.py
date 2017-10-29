import os

import pyblish.api
from blacksmithvfx_environment import utils


class BlacksmithFtrackIntegrateVersionUpScene(pyblish.api.ContextPlugin):
    """Versions up the scene if publishing an asset

    Offset to get component from pyblish-ftrack
    """

    order = pyblish.api.IntegratorOrder + 0.1
    label = "Version Up Scene"
    families = ["img"]
    hosts = ["nuke"]
    optional = True

    def process(self, context):

        version_up = False
        for instance in context:
            if "img" not in instance.data.get("families", []):
                continue

            for data in instance.data.get("ftrackComponentsList", []):
                self.log.info(data)
                if "component" in data:
                    version_up = True

        if not version_up:
            return

        path = self.get_expected_path(
            context,
            pyblish.api.current_host(),
            context.data.get("version", 1)
        )
        self.log.debug("Versioning up scene to: {0}".format(path))

        # Create parent directory if it doesn't exist
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        if pyblish.api.current_host() == "nuke":
            import nuke
            nuke.scriptSaveAs(path)

    def get_expected_path(self, context, host, version):

        path = utils.get_work_file(
            context.data["ftrackSession"],
            context.data["ftrackTask"],
            host,
            version + 1
        )

        # Increase version until its unique on disk
        if os.path.exists(path):
            return self.get_expected_path(context, host, version + 1)
        else:
            return path
