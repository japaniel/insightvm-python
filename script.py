import os
import dotenv
import base64

import swagger_client
import swagger_client.configuration as configuration
from swagger_client.rest import ApiException
from pprint import pprint

def main():
    ENV_FILE = dotenv.find_dotenv()
    if ENV_FILE:
        dotenv.load_dotenv(ENV_FILE, override=True)

    config = configuration.Configuration()
    config.password = os.getenv('PASSWORD')
    del os.environ['PASSWORD']
    config.username = os.getenv('USER')
    config.host = os.environ['HOST']
    config.verify_ssl = False

    auth_settings = config.auth_settings()
    # for property, value in vars(config).items():
    #     print(property, ":", value)

    api_client = swagger_client.ApiClient(config)
 
    api_instance = swagger_client.SiteApi(api_client)
    page = 0
    size = 10
    sort = ['ASC']

    try:
        api_response = api_instance.get_sites(page=page, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SiteApi->get_sites: %s\n" % e)


    # api_instance = swagger_client.AssetApi(api_client)

    # for property, value in vars(api_instance).items():
        # print(property, ":", value)
    # filter = {
        # 'field': '',
        # 'value': 'baseimage',
        # 'operator': 'is-like',
        # 
    # }

    # body = swagger_client.SearchCriteria(match='all',filters=[filter])
    # page = 0
    # size = 10

    # try:
        # Asset Search
        # api_response = api_instance.find_assets(body, page=page, size=size)
        # pprint(api_response)
    # except ApiException as e:
        # print("Exception when calling AssetApi->find_assets: %s\n" % e)

if __name__ == '__main__':
    main()