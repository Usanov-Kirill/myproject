import requests

r = requests.get("https://api.adviceslip.com/advice", timeout=5) 
r.raise_for_status()        
data = r.json()    
print(data["slip"]["advice"])   

