Dict={"Name":"Buggu","Gender":"Male","Age":"69","Address":"Scott Road","Phone":"0119988752"}
Choice=input("Which Detail you want :")
if Choice in Dict:
    print(Dict[Choice])
else:
    print("Key is not found")