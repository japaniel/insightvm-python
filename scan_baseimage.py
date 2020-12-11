import os
import dotenv
import base64
import logging
import time
import re
import pandas

import swagger_client
from swagger_client import configuration
from swagger_client.rest import ApiException
from pprint import pprint

def build_config():
    """ Build Config object from environment variables """
    config = configuration.Configuration()
    config.password = os.getenv('PASSWORD')
    del os.environ['PASSWORD']
    config.username = os.getenv('USER')
    config.host = os.getenv('INSIGHTVM_HOST')
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

    if os.getenv('FILTERS'):
        # TODO - Make this work if we ever want to validate more than the hostname
        # which we do already because we want to know if the IP is the same as what
        # is in InsightVM as the base image will go up and down
        for f in os.environ['FILTERS']:
            pprint(f)
    
    else:
        filters = {
            'field': 'host-name',
            'operator': 'is-like',
            'value': host,
        }

    body = swagger_client.SearchCriteria(match='all',filters=[filters])

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
    # TODO - check for a running scan
    api_instance = swagger_client.ScanApi(api_client)
    id = 9 # TODO - Get rid of this magic number, which might be needed for testing...
    body = swagger_client.AdhocScan() # AdhocScan | The details for the scan. (optional)

    try:
        api_response = api_instance.start_scan(id, body=body)
        logging.debug('Response: {}'.format(api_response))
    except ApiException as e:
        logging.error("Exception when calling ScanApi->start_scan: %s\n" % e)

    scan_id = api_response.id
    stuff = poll_scan(api_client, scan_id)
    
    return stuff

def poll_scan(api_client, id =""):
    """
    Polls the scan_id every 5 seconds until scan is complete

    Returns completed data
    """
    status = ""

    logging.info('Checking status of scan {}'.format(id))
    while status != 'finished':
        api_instance = swagger_client.ScanApi(api_client)
        id = id

        try:
            api_response = api_instance.get_scan(id)
            status = api_response.status
            logging.info('Scan {} is in {} status'.format(id, status))
            time.sleep(5)
        except ApiException as e:
            print("Exception when calling ScanApi->get_scan: %s\n" % e)

    return api_response

def validate_host(resources, search_term):
    """
    Validate the resource returned is in fact the host we are looking for

    :param resource: list returned by the SearchAPI call

    :param search_term: string of host to search for

    Returns single resource
    """
    rs = []
    for r in resources:
        if search_term and not re.search(search_term, r.host_name):
            logging.info('The host {} is not in ')
            continue

        # TODO - This thing right here
        for event in r.history:
            # sort by date
            # Python lists are ordered and in our case by _date so unless we sort otherwise we are :thumbsup:
            # limit to last 2h
            event_time = pandas.Timestamp(event._date)
            current_time = pandas.Timestamp.now('UTC')
            print(current_time, event_time)

            test = current_time - event_time
            print(test.total_seconds())

            df = pandas.DataFrame(columns=['event', 'now'])
            df.event = [event_time]
            df.now = [current_time]
            diff = (df.now-df.event).astype('timedelta64[h]')
            #pprint(diff)

            # check if any are type='SCAN'
            
       
            # logging.info('Asset {} was scanned within the last 2h; passing'.format(asset))
            # exit

        rs.append(r)

    if len(rs) > 1:
        logging.debug('Multiple resources were found; be more specific in your search/n{}'.format(resources))
        exit()

    resource = rs[0]
    return resource

def main():
    ENV_FILE = dotenv.find_dotenv()
    if ENV_FILE:
        dotenv.load_dotenv(ENV_FILE, override=True)

    host = os.getenv('HOST')
    config = build_config()

    api_client = swagger_client.ApiClient(config)

    resources = lookup_host(api_client, host)

    if len(resources) < 1:
        logging.warning("{} was not found".format(host))
        logging.info("Adding {} to InsigthVM".format(host))
        add_host(api_client, host)

    if len(resources) >= 1:
        resource = validate_host(resources, host)

    logging.info('Found the host: {}'.format(host))
    # TODO - Swap True to False as the desired normal state
    if resource.assessed_for_vulnerabilities == True:
        scan_host(api_client, host)

    if resource.vulnerabilities.total > 0:
        logging.error('Total risk score is too high: {}'.format(resource.vulnerabilities.total))
        exit()

    print("We Passed!")

    # for property, value in vars(api_instance).items():
    #     print(property, ":", value)

if __name__ == '__main__':
    main()