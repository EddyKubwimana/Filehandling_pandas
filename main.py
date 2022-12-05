

import pandas as pd


# read a csv file using pandas module

file = pd.read_csv("CountryData.csv")

# create various list by slicing the the csv file

country_name = file["Country Name"]
population = file["Population"]
literacy = file["Literacy"]

mobile_subs = file["Mobile"]
internet_users = file["Internet"]

elect_production = file["Elect. Production"]
elect_consumption = file["Elect. Consumption"]

# creating the country dictionnary

country_dict = {}
for i in range(len(country_name)):
    country_dict[country_name[i]] = i

print("which country do you want to know its information in Africa")
search = input(">>>")

# This print the result of the search
print(
    f"{search} has a population of {population[country_dict[search]]} and a literacy rate of {literacy[country_dict[search]]}%.")
print(
    f"estimate of the number of mobile subscriptions is {mobile_subs[country_dict[search]]}, while that of internet users is {internet_users[country_dict[search]]}")
print(
    f"{search} produces {elect_production[country_dict[search]]} billion KWh of electricity annually, while it consumes {elect_consumption[country_dict[search]]}billion KWh of electricity")


mobile_capita = []
internet_capita = []

for i in range(len(country_name)):
    mobile_capita.append(round(mobile_subs[i] / population[i], 2))
    internet_capita.append(round(internet_users[i] / population[i], 2))

report_capita = pd.DataFrame({"Country Name": country_name,
                              "Mobile user per capita": mobile_capita,
                              "Internet user per capita": internet_capita})
report_capita.to_csv("per_report_2.csv")


def africa_pop(country_pop):
    tot_pop = 0
    for i in country_pop:
        tot_pop = tot_pop + i
    return tot_pop


# function to find the least and most populous country
def most_least_pop(pop, country_name):
    new_pop = sorted(pop)
    pop = list(pop)

    least = pop.index(new_pop[0])
    highest = pop.index(new_pop[-1])
    my_rep = {"Least populous is": country_name[least], "The most Populous": country_name[highest]}
    return my_rep


# function to find the high and low literate country
def high_low_liter(liter, country_name):
    new_lit = sorted(liter)
    liter = list(liter)
    least = liter.index(new_lit[0])
    highest = liter.index(new_lit[-1])
    my_rep = {"Least literate country is": country_name[least], "The most literate country is": country_name[highest]}
    return my_rep


# function to find the high and low mobile adoption per capita

def high_low_mob(mobile_sub, country):
    new_mob = sorted(mobile_sub)
    mobile_sub = list(mobile_sub)
    high = mobile_sub.index(new_mob[-1])
    low = mobile_sub.index(new_mob[0])
    rep = {"The country with highest Mob subs per capita": country[high],
           "The country with lowest Mob subs per capita": country[low]}
    return rep


# function to find the low or high internet user per capita
def high_low_int(internet, country):
    new_int = sorted(internet)
    internet = list(internet)
    high = internet.index(new_int[-1])
    low = internet.index(new_int[0])
    rep = {"The country with highest internet user per capita": country[high],
           "The country with lowest internet user per capita": country[low]}
    return rep


# function to find country which produce more energy than they consume
def produce_more(ele_prod, ele_cons, country):
    ret_country = []
    for i in range(len(ele_prod)):
        if ele_prod[i] > ele_cons[i]:
            ret_country.append(country[i])
    return ret_country


# the function to find the country that produce less electricity than they use
def produce_less(ele_prod, ele_cons, country):
    p = []
    for i in range(len(country)):
        if ele_prod[i] < ele_cons[i]:
            p.append(country[i])
    return p


# function to find the average literacy in africa
def average_pop(literacy, pop):
    tot_pop = 0
    tot_lit = 0
    for i in range(len(pop)):
        tot_pop = tot_pop + pop[i]
        tot_lit = tot_lit + literacy[i]
    return tot_lit / tot_pop


print("The africa population is ", africa_pop(population))
print()
print(most_least_pop(population, country_name))
print()
print(high_low_liter(literacy, country_name))
print()
print("The average of african literate is", average_pop(literacy, population))
print()
print(high_low_mob(mobile_capita, country_name))
print()
print(high_low_int(internet_capita, country_name))
print()

print("Country that produce more electricity than they consume",
      produce_more(elect_production, elect_consumption, country_name))
print()
print("Country than produce less electricity than they consume",
      produce_less(elect_production, elect_consumption, country_name))

















