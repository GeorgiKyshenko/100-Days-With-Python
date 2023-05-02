travel_log = {
    "Bulgaria": {
        "visited_cities": ["Burgas", "Sofia", "Varna"], "total_visits": 12
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log.get("Bulgaria").get("visited_cities")[0])
# or
print(travel_log["Bulgaria"]["visited_cities"][0])
print(travel_log["Bulgaria"]["total_visits"])
print(travel_log.get("Germany")[2])

# Ultra nesting
travel_log["Bulgaria"]["expectations"] = ["Excellent", "Not Bad"]
print(travel_log)

# Nesting a dictionary in a list
travel_log = [
    {
        "country": "Bulgaria",
        "visited_cities": ["Burgas", "Sofia", "Varna"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "visited_cities": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

print(" ".join(travel_log[0]["visited_cities"]) + "-" + str(travel_log[0].get("total_visits")))


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {"country": country_visited, "visited_cities": cities_visited, "total_visits": times_visited}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

