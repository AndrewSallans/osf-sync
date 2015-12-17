"""Utilities related to error logging"""

from osfoffline import settings
from osfoffline.utils.authentication import get_current_user


def add_user_to_sentry_logs():
    """Add the current user's OSF ID to all sentry error events"""
    user = get_current_user()

    # Set user id across all threads globally
    data = settings.raven_client.extra.setdefault('data', {})
    context = {'osf_user_id': user.id}
    data.update(context)

    # Alternate mechanism based on thread locals
    #settings.raven_client.extra_context(context)


def remove_user_from_sentry_logs():
    """Remove the ID of the current user from all sentry error events"""
    extra_data = settings.raven_client.extra.get('data', {})

    for k in ('osf_user_id',):
        extra_data.pop(k, None)

    # Alternate mechanism based on thread-locals
    #settings.raven_client.context.clear()
