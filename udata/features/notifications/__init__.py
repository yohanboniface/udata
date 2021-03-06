# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from importlib import import_module

import logging

log = logging.getLogger(__name__)


def init_app(app):
    # Load core notifications
    import udata.core.organization.notifications  # noqa
    import udata.core.discussions.notifications  # noqa
    import udata.core.issues.notifications  # noqa
    import udata.harvest.notifications  # noqa

    # Load feature notifications
    import udata.features.transfer.notifications  # noqa

    # Load all plugins views and blueprints
    for plugin in app.config['PLUGINS']:
        module = 'udata.ext.{0}.notifications'.format(plugin)
        try:
            import_module(module)
        except ImportError:
            pass
        except:
            log.exception('Error importing %s notifications', module)
