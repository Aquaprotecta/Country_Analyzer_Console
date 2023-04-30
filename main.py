import requests
import os

def get(country_name):
    api_url = f'https://api.api-ninjas.com/v1/country?name={country_name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'm/kt1fTkQods5DwclGVhYg==y1SfZTmIJZLImGQG'})
    
    if response.status_code == requests.codes.ok:
        data = response.json()[0]
        country_data = {
            'Country': data['name'],
            'Population': f"{data['population']:,}",
            'GDP': f"${data['gdp']:,}",
            'Infant Mortality': data['infant_mortality'],
            'Fertility': data['fertility']
        }
        return country_data
    else:
        print("Error:", response.status_code, response.text)
        
        
country = input('Enter the country you want the information of: ')
country_data = get(country)

if country_data:
    for key, value in country_data.items():
        print(f"{key}: {value}")
        
os.system("pause")