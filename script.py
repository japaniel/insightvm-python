import os
import dotenv
import base64
import logging

import swagger_client
from swagger_client import configuration
from swagger_client.rest import ApiException
from pprint import pprint

def build_config():
    """ Build Config object from environment variables """

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

def lookup_host(api_client, host =''):
    """ 
    Look up if the host is in InsightVM
    Returns ... something

    :param api_client: Instance of swagger_client.ApiClient

    :param host: Shortname, or subset of shortname, for the host that is being searched
    """
    api_instance = swagger_client.AssetApi(api_client)

    filter = {
        'field': 'host-name',
        'operator': 'is-like',
        'value': host,
    }

    body = swagger_client.SearchCriteria(match='all',filters=[filter])

    try:
        api_response = api_instance.find_assets(body, page=os.environ['PAGE'], size=os.environ['SIZE'])
        logging.debug(api_response.resources)
    except ApiException as e:
        print("Exception when calling AssetApi->find_assets: %s\n" % e)

    return api_response.resources

def add_host(api_client, host):
    """
    Add host to InsightVM

    Return when complete
    """
    pass

def scan_host(api_client, host =""):
    """
    Run security scan on the host

    Returns scan results
    """
    pass

def main():
    config = build_config()

    api_client = swagger_client.ApiClient(config)

    resources = lookup_host(api_client, os.environ['HOST'])
    
    if len(resources) < 1:
        logging.warning("{} was not found".format(os.environ['HOST']))
        add_host(api_client, os.environ['HOST'])

    if len(resources) > 1:
        # TODO - Make this smoother
        hosts = ['one', 'two']
        logging.error('Multiple resources were found; be more specific in your search/n {}'.format(hosts))
        exit()

    logging.info('Found the host: {}'.format(os.environ['HOST']))
    
    if resources[0].assessed_for_vulnerabilities == False:
        scan_host(api_client, os.environ['HOST'])

    if resources[0].risk_score > 0.0:
        logging.error('risk score is too high: {}'.format(resources[0].risk_score))
        exit()

    print("we got this far")

    # for property, value in vars(api_instance).items():
    #     print(property, ":", value)

if __name__ == '__main__':
    main()