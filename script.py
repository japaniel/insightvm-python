import os
import dotenv
import base64

import swagger_client
from swagger_client import configuration
from swagger_client.rest import ApiException
from pprint import pprint

def build_config():
    """ Load what we can from environment variables """

    ENV_FILE = dotenv.find_dotenv()
    if ENV_FILE:
        dotenv.load_dotenv(ENV_FILE, override=True)

    config = configuration.Configuration()
    config.password = os.getenv('PASSWORD')
    del os.environ['PASSWORD']
    config.username = os.getenv('USER')
    config.host = os.environ['INSIGHTVM_HOST']
    config.verify_ssl = False

    return config

def lookup_host(api_client):
    """  """
    api_instance = swagger_client.AssetApi(api_client)

    filter = {
        'field': 'host-name',
        'operator': 'is-like',
        'value': os.environ['HOST'],
    }

    body = swagger_client.SearchCriteria(match='all',filters=[filter])

    try:
        api_response = api_instance.find_assets(body, page=os.environ['PAGE'], size=os.environ['SIZE'])
        pprint(api_response.resources)
    except ApiException as e:
        print("Exception when calling AssetApi->find_assets: %s\n" % e)

    


def main():
    config = build_config()

    api_client = swagger_client.ApiClient(config)

    lookup_host(api_client)

    # for property, value in vars(api_instance).items():
    #     print(property, ":", value)


    if len(api_response.resources) < 1:
        # TODO - Do something smarter
        print("no resources")
        exit()
    else:
        # Continue
        print('Continue')

if __name__ == '__main__':
    main()