import json

countries = [{"name":"Russia"},{"code":"rs","name":"Serbia"}]

with open("data_file.json","r") as read_file:
  #  json.dump(countries,write_file)
   data = json.load(read_file)
   print(data[0])