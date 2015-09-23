import rdw_api
import config

number_plate = '16-tt-fv'
api = rdw_api.RdwApi(config.API_KEY)

car_information = api.request_information(number_plate)

print(car_information)
print(car_information['parkerentoegestaan'])