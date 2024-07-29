# Request --> Client Server

# GET Request - Booking Id
# URL- https://restful-booker.herokuapp.com/booking/302
# Auth - No
# Payload - No
# Content type or Header - No
# Query param- No
# Path Param - Yes - 302

# Response
# Body--> Verify assert
# Status code verification
# Time
# JSON Schema validation, XML Schema

import pytest
import allure
import requests


@allure.title("GET Request Restful-booker automation project")
@allure.description("TC#1, To test get booking id by a single booking id")
@allure.tag("p0", "smoke", "regression")
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/302"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200


@allure.title("GET Request Restful-booker automation project")
@allure.description("TC#1, To test get booking id by a invalid booking id")
@allure.tag("p0", "smoke", "regression")
def test_get_single_request_by_invalid_id():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404

@allure.title("GET Request Restful-booker automation project")
@allure.description("TC#1, To test get booking id by a invalid booking id")
@allure.tag("p0", "smoke", "regression")
def test_get_single_request_by_wrong_id():
    url = "https://restful-booker.herokuapp.com/booking/001"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code != 404
