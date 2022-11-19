import requests
import paho.mqtt.client as mqtt
import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound
prevMedicine = ''
currMedicine = ''
while True:
    req=requests.get("http://169.51.206.114:32641/remainder")
    value=req.json()
    try:
        prevMedicine = value['command']
        ORG= "jchm38"
        DEVICE_TYPE ="MR"
        DEVICE_ID ="2019504037"
        TOKEN ="()!xRUci*BCpeso-rk"
        server = ORG + ".messaging.internetofthings.ibmcloud.com";
        pubTopic1 = "iot-2/evt/medicine/fmt/string"
        pubTopic2 = "iot-2/evt/pH/fmt/json"
        pubTopic3 = "iot-2/evt/turb/fmt/json"
        #pubTopic3 = "iot-2/evt/wf/fmt/json"

        authMethod = "use-token-auth";
        token = TOKEN;
        clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;
        if currMedicine != prevMedicine:
                mqttc = mqtt.Client(client_id=clientId)
                mqttc.username_pw_set(authMethod, token)
                mqttc.connect(server, 1883, 60)
                mqttc.publish(pubTopic1,json.dumps(value))
                print("Published Successfully!")
                authenticator = IAMAuthenticator('jHG72RxBZzpJDs4vkDt6DySXoaJu9hylmn0hjE_p-F0g')
                text_to_speech = TextToSpeechV1(
                    authenticator=authenticator
                )

                text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/74dc1eed-1e64-4f57-ba4a-2031a8f39d85')
                with open('try.mp3', 'wb') as audio_file:
                    audio_file.write(text_to_speech.synthesize('Please Take'+'    '+value['command']+'   '+'tablet now', voice='en-US_MichaelExpressive', accept='audio/wav').get_result().content)

                print("playing")
                #playsound('try.mp3')

                currMedicine = prevMedicine 
    except Exception as error:
        print(error.args[0])
        print("Error!")
mqttc.loop_forever()

    


