import ftrack_api
import lucidity


class Structure(ftrack_api.structure.base.Structure):

    def get_resource_identifier(self, entity, context=None):

        templates = lucidity.discover_templates()

        if not templates:
            raise ValueError("No lucidity templates found.")

        valid_templates = templates[0].get_valid_templates(entity, templates)
        if valid_templates:
            return valid_templates[0].format(entity)

        msg = (
            'Could not find any templates for {0} with template name "{1}".'
        )
        raise ValueError(
            msg.format(entity, templates[0].get_template_name(entity))
        )


def configure_locations(event):
    '''Configure locations for session.'''
    session = event['data']['session']

    location = session.query(
        "Location where name is \"project.disk.root\""
    ).one()
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = Structure()
    location.priority = 50


def register(session):
    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an old or incompatible API and
    # return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        return

    session.event_hub.subscribe(
        "topic=ftrack.api.session.configure-location",
        configure_locations
    )
