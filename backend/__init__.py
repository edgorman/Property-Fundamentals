import email
from pkg_resources import get_distribution

__name__ = get_distribution("backend").project_name
__version__ = get_distribution("backend").version
__description__ = email.message_from_string(get_distribution("backend").get_metadata('PKG-INFO'))['Summary']
