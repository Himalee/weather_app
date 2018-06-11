import requests
from flask import Flask, render_template, request

app = Flask("MyApp")
# app.config.from_json('config.json')

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("main.html") # renders the main page


@app.route("/weather", methods=['GET', 'POST'])
def weather():
    # secret_key = app.config["SECRET_KEY"]
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    city = request.form['location']
    payload = {
        "q": city,
        "units": "metric",
        "appid": "ENTER API KEY HERE"
    }
    response = requests.get(endpoint, params=payload)
    print response.url
    weather = {}
    if response.json().has_key("weather"):
        weather["main"] = response.json()["weather"][0]["main"]
        weather["temp"] = response.json()["main"]["temp"]
        weather["description"] = response.json()["weather"][0]["description"]
        weather["name"] = response.json()["name"]
    else:
        return render_template("main.html", error="Can't find the location")

    if weather["main"] == "Rain":
        rain_wear = "Wear a raincoat and an umbrella!"
        return render_template("weather.html", css_class="rain", city_weather=weather, city_wear=rain_wear)

    if weather["main"] == "Thunderstorm":
        thunderstorm_wear = "Make sure you take your raincoat is water and wind proof!"
        return render_template("weather.html", css_class="thunderstorm", city_weather=weather, city_wear=thunderstorm_wear)

    if weather["main"] == "Snow":
        snow_wear = "You will need a pair of boots with a wooly hat, scarf and a pair sgloves!"
        return render_template("weather.html", css_class="snow", city_weather=weather, city_wear=snow_wear)

    if weather["main"] == "Drizzle":
        drizzle_wear = "Today will be humid. Wearing breathable natural materials such as cotton will help you cope"
        return render_template("weather.html", css_class="drizzle", city_weather=weather, city_wear=drizzle_wear)

    if weather["main"] == "Clear":
        clear_wear = "It's nice weather - enjoy it while it lasts! Wear something summery and soak up some vitamin D."
        return render_template("weather.html", css_class="clear", city_weather=weather, city_wear=clear_wear)

    if weather["main"] == "Clouds":
        clouds_wear = "Take a pair of sunglasses just in case the sun comes out!"
        return render_template("weather.html", css_class="clouds", city_weather=weather, city_wear=clouds_wear)

    if weather["main"] == "Extreme":
        extreme_wear = "The weather is acting up... you might want to consider staying at home."
        return render_template("weather.html", css_class="extreme", city_weather=weather, city_wear=extreme_wear)

    if weather["main"] == "Additional":
        additional_wear = "It could get pretty windy today, bring something to keep you warm!"
        return render_template("weather.html", css_class="additional", city_weather=weather, city_wear=additional_wear)

    if weather["main"] == "Atmosphere":
        atmosphere_wear = "It could get pretty foggy today. Less visability means having to pay more attention in traffic."
        return render_template("weather.html", css_class="atmosphere", city_weather=weather, city_wear=atmosphere_wear)

    if weather ["main"] == "Haze":
        haze_wear = "It's hazy today. By taking public transport you will contribute to a cleaner world!"
        return render_template("weather.html", css_class="haze", city_weather=weather, city_wear=haze_wear)
    else:
        return render_template("weather.html", css_class="default", city_weather=weather)


app.run(debug=True)
