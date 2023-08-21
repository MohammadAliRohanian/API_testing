# Condition statement for select enviroment
import config

env = config.ENV
domain = config.DOMAIN_UAT

if env == "UAT":
    domain = config.DOMAIN_UAT

# Routes
USERS_ROUTE = domain + "/users"
