# Condition statement for select enviroment domain
import config

env = config.ENV

if env == "UAT":
    domain = config.DOMAIN_UAT
# elif env == "STAGE"
#     domain = config.DOMAIN_STAGE
# elif env == "PROD"
#     domain = config.DOMAIN_PROD

# Routes
USERS_ROUTE = domain + "/users"
