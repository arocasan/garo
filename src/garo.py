from segredos import segredo
import requests
import json

garo_id = segredo.GARO_ID
garo_address = segredo.GARO_ADDRESS


def chargebox_status():

    response = requests.get(f"{garo_address}/status")
    chargebox_status = response.json()
    chargebox_mode = chargebox_status["mode"]
    chargebox_power = chargebox_status["powerMode"]
    chargebox_wifi = chargebox_status["mainCharger"]["wifiCardStatus"]
    chargebox_connected = chargebox_status["connector"]
    chargebox_time = chargebox_status["chargeboxTime"]
    chargebox_internet = chargebox_status["connectedToInternet"]
    chrgebox_current = chargebox_status["currentChargingCurrent"]
    chrgebox_power = chargebox_status["currentChargingPower"]
    chargebox_acc_session_energy = chargebox_status["accSessionEnergy"]
    chargebox_acc_session_time = chargebox_status["accSessionMillis"]
    chargebox_latest_reading = chargebox_status["latestReading"]
    chargebox_temperature = chargebox_status["currentTemperature"]
    chargebox_cable_locked = chargebox_status["mainCharger"]["cableLockMode"]
    chargebox_latest_contact = chargebox_status["mainCharger"]["lastContact"]
    chargebox_meter_status = chargebox_status["mainCharger"]["meterStatus"]
    print(chargebox_mode, chargebox_temperature)

    return response


garo_status = chargebox_status()

print(garo_status)