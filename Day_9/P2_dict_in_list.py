# Main objective is to create a program that adds the country you visited to "travel_log", according to the video instructions;
# Link of the video is : https://www.udemy.com/course/100-days-of-code/learn/lecture/40101342#overview (Course enrolling is mandatory)


country = input()
visits = int(input())
list_of_cities = eval(input())


travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, list_of_cities):
    new_travel = {}
    new_travel["country"] = country.title()
    new_travel["visits"] = visits
    new_travel["cities"] = list_of_cities
    print(new_travel)
    travel_log.append(new_travel)
    print(travel_log)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")