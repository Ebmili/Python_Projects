""" 
programming_dictionary = {
  "Bug": "An error in the program", 
  "Function": "A pice of code, storage that you can resue easily over and over again",
}

print(programming_dictionary["Bug"])

#adding into a dictionary

programming_dictionary["Loop"] = "The action of doing sth over and over again"

print(programming_dictionary)

#Call empty

empty_dictionary = {}

#Edit an intem in a dictionary

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key]) """

##capitals = {
##  "France": "Paris",
##  "Germany": "Berlin",
##}


#You can add a list of cities to a value of key 

#travel_log = {
#  "France": ["Paris", "Lillie", "Dijon"],
#  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
#}

# Dictionary into a dictionary

#travel_log = {
#  "France": {"cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits": 12},
#  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
#}

#Dictionary within a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

def add_new_country():
    new_country = {}
    new_country["country"] = input("Enter the country: ")
    new_country["total_visits"] = int(input("Enter the number of visits: "))
    cities = input("Enter the cities visited (comma-separated): ").split(',')
    new_country["cities_visited"] = [city.strip() for city in cities]
    travel_log.append(new_country)

# Call function to add a new country
add_new_country()

# Print the details of the last entry in travel_log
last_entry = travel_log[-1]
print(f"I've been to {last_entry['country']} {last_entry['total_visits']} times.")
print(f"The cities visited are: {', '.join(last_entry['cities_visited'])}.")
