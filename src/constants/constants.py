DEFAULT_LISTEN_PORT = '5005'


# ----- CONFIG CONSTANTS ----- [Path for configurations]
PRIORITY_SERVER_CONFIG_PATH = '/config'
SERVER_CONFIG_PATH = '/config'
KEY_SERVER_CONFIG = 'server_configuration'
KEY_PRIORITY_SERVER_CONFIG = 'prio_server_configuration'
KEY_SERVERS = 'servers'
KEY_SENDER = 'sender'


# ----- FILE CONSTANTS ------- [File names/path]
PRIORITY_SERVER_FILE = '/high-prio-smtp-servers.yaml'
SERVER_FILE = '/smtp-servers.yaml'

# ----- ENV KEYS ------------- [Keys for the environment variables]
ENV_LISTEN_PORT = 'EMAIL_CLIENT_SERVICE_LISTEN_PORT'
ENV_CONFIG_FOLDER = 'MESSAGING_CONFIG_FOLDER'
ENV_PRI_CONFIG_FOLDER = 'MESSAGING_CONFIG_FOLDER'

# ----- VALIDATION CONSTANTS ------------- [Required fields for YAML validation]
KEY_SEPARATOR = ','
REQUIRED_YAML_KEYS = 'from, sender, replyTo, servers'
REQUIRED_SERVER_KEYS = 'host, port, connections, auth'

# ----- CONNECTION CONSTANTS ------------- [Parameters for connection retries and backoff]
IS_AUTH_REQUIRED = 'False'
MAX_RECONNECT_ATTEMPTS = '3'
INITIAL_RECONNECT_WAIT = '0.5' # In seconds

# ----- EMAIL CONSTANTS --------- [Keys for email message construction]
KEY_SUBJECT = 'Subject'
KEY_FROM = 'From'
KEY_TO = 'To'
KEY_CC = 'Cc'
KEY_BC = 'Bcc'