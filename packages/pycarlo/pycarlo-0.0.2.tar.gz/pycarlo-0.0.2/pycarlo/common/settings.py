import os
from pathlib import Path

"""Environmental configuration"""

# Enable error logging.
MCD_VERBOSE_ERRORS = os.getenv('MCD_VERBOSE_ERRORS', False) in (True, 'true', 'True')

# MCD API endpoint.
MCD_API_ENDPOINT = os.getenv('MCD_API_ENDPOINT', 'https://api.getmontecarlo.com/graphql')

# Override MCD Default Profile when reading from the config-file in a session.
MCD_DEFAULT_PROFILE = os.getenv('MCD_DEFAULT_PROFILE')

# Override MCD API ID when creating a session.
MCD_DEFAULT_API_ID = os.getenv('MCD_DEFAULT_API_ID')

# Override MCD API Token when creating a session.
MCD_DEFAULT_API_TOKEN = os.getenv('MCD_DEFAULT_API_TOKEN')

"""Internal Use"""

# Name of the current package.
DEFAULT_PACKAGE_NAME = 'pycarlo'

# Default config keys for the MC config file. Created via the CLI.
DEFAULT_MCD_API_ID_CONFIG_KEY = 'mcd_id'
DEFAULT_MCD_API_TOKEN_CONFIG_KEY = 'mcd_token'

# Default headers for the MC API.
DEFAULT_MCD_API_ID_HEADER = f'x-{DEFAULT_MCD_API_ID_CONFIG_KEY.replace("_", "-")}'
DEFAULT_MCD_API_TOKEN_HEADER = f'x-{DEFAULT_MCD_API_TOKEN_CONFIG_KEY.replace("_", "-")}'

# Default headers to trace and help identify requests. For debugging.
DEFAULT_MCD_SESSION_ID = 'x-mcd-session-id'  # Generally the session name.
DEFAULT_MCD_TRACE_ID = 'x-mcd-trace-id'

# File name for profile configuration.
PROFILE_FILE_NAME = 'profiles.ini'

# Default profile to be used.
DEFAULT_PROFILE_NAME = 'default'

# Default path where any configuration files are written.
DEFAULT_CONFIG_PATH = os.path.join(str(Path.home()), '.mcd')
