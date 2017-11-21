"""
constants
"""

vehicle_type = "Sedan"
base = "JohnnyBase"
searching_driver = "Please wait while we look for a driver.."
default_user = "admin"
default_pword = "123456"
suggested_add = ""

"""
HTTP REQUESTS
"""
root_url = "https://devmobile.operr.com"
accept_trip_endpoint = "/v2/mobile/driver/accept_trip"
accept_trip_payload = {
            "trip_id": None,
            "driver_id": None #johnnyle9
        }
test_data_kw = {}
test_data_kw['PROFILE_PAGE'] = [{}]
