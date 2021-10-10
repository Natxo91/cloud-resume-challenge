import json

import pytest


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return json.load('/getApiRequest.json')



def test_lambda_handler(apigw_event,context):

    ret = app.getfunction(apigw_event, "")
    data = json.loads(ret["body"])
    #if 1 == 0:
    #    ret = 'fatal error 404'
    #else:
    #    ret = 'OK'
    #assert ret == 'OK'
    assert ret["statusCode"] == 200
    #assert "message" in ret["body"]
    #assert data["message"] == "hello world"
    # assert "location" in data.dict_keys()
