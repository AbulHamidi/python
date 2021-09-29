import json
import requests
from datetime import datetime

stops = requests.get("http://data.foli.fi/siri/sm/pretty")
stops = json.loads(stops.text)

while True:
    stop_id = input("Anna pysäkin numero: ")
    try:
       stop = stops[stop_id]["stop_name"]
    except KeyError:
        continue
        print(stop_id)

    stop_data = requests.get(f"http://data.foli.fi/siri/sm/{stop_id}/pretty")
    stop_data = json.loads(stop_data.text)
    next_10 = stop_data["result"][:10]
    
    print(stop)
    for arrival in next_10:
        planned_time = arrival["aimedarrivaltime"]
        expected_time = arrival["expectedarrivaltime"]
        time_diff = expected_time - planned_time
        dt = ""
        
        if time_diff:
            dt = F"({time_diff//60:+d})"
        time = datetime.fromtimestamp(expected_time)
        route = arrival["lineref"]
        destination = arrival["destinationdisplay"]
        
        print(f"{time:%H:%M}{dt:>5}{route:>4} - {destination}")
        
        
