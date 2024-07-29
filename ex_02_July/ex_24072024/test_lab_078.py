#API CRUD OPERATION

import pytest
import allure
import requests


@allure.title("Create booking CRUD")
@allure.description("TC#1 Verify by creating a booking id")
@pytest.mark.smoke
def test_create_booking_positive():
    # To make request (URL, Headers(content ype), method, payload/data/body/Dict/JSON, Auth not required)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

    responseData = response.json()
    # Response body Verification
    # Verify (headers,json schema, status code, time)
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True
    assert checkin == "2018-01-01"
    assert checkout =="2019-01-01"


@allure.title("Create booking CRUD")
@allure.description("TC#2 Verify by creating a booking id by giving empty payload")
@pytest.mark.crud
def test_create_booking_negative():
    # To make request (URL, Headers(content ype), method, payload/data/body/Dict/JSON, Auth not required)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 500




