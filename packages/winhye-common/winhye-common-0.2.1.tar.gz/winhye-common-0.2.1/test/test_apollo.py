import os
import sys

PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)), "src")
sys.path.append(PATH)

from winhye_common.utils.apollo_client import ApolloClientInit


def test_apollo():
    apo = ApolloClientInit(
        app_id='kaifa',
        config_server_url='http://59.110.220.223:8083',
        cluster='PRO'
    )

    value = apo.get_config('ccc')
    print(value)


if __name__ == '__main__':
    test_apollo()
