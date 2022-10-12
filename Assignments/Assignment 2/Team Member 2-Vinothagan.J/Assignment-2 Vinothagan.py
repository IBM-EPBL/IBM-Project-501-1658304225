import random as SS

T=SS.randint(18,40);
H=SS.randint(20,100);

if(T>30):
    print("Hazard:High Temperature","Temperature =",T,"°C");
else:
    print("No Hazard Detected","Temperature =",T,"°C");
    
if(H>90):
    print("Hazard Detected:High Humidity","Humidity =",H,"%");
else:
    print("No Hazard Detected:Normal Humidity","Humidity =",H,"%");
