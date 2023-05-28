auto = [
    {
        "manufakturer" : "vw" ,
        "price" :800
    },

    {
        "manufakturer": "bmw",
        "price": 1500
    },

    {
        "manufakturer": "MB",
        "price": 2500
    },

    {
        "manufakturer": "Ford",
        "price": 2800
    },
]

def shaw_car ():

    i = 0

    while i < len(auto) :

        car_by_index = auto[i]

        for key, value in car_by_index.items():

            print(key, value)

        i += 1

def add_car (auto):

    new_car = {}

    new_car["manufakturer"] = input("Enter car manufacture:\n")

    new_car["price"] = int(input("Enter price in $"))

    auto.append(new_car)

def remove_car (auto):

    del_car = input("Enter manufacturer for delete\n")

    for item in auto.copy():

        if item.get('manufakturer') == del_car:

            auto.remove(item)

            print("NEW LIST OF CARS")

            shaw_car()

            break

# def sort_car (auto) :
#
#     sort_price = int(input("Enter price for Sort list of cars by Price"))
#
#     sort_cars = {}
#
#     for itims in auto:
#         if int(auto["price"]) >= sort_price :
#             sort_cars.values()
#     print(sort_cars)

def decore_msg (msg):
    print(len(msg) * "*" + "\n" + msg + "\n" + len(msg) * "*" + "\n")

def quit():

    if choose_option() == 0:

        is_running = False


def run(is_running):

    while is_running == True:

        options()

        choose_option()


def options():

    list_of_option = ["Add new car" , "Shaw all cars" , "Remove car", "Get expansive cars"]

    i = 0

    while i < len(list_of_option):

        print((str(i +1 ) + ")" + list_of_option[i]))

        i += 1

def choose_option():

    option_index = int(input("Enter number, what you wont to do?\n"))

    match(option_index):

        case 1 :

            add_car(auto)

        case 2 :

            shaw_car()

        case 3 :

            remove_car(auto)

        case 0 :

            print("Goodbye!!!")

            quit()

        case 4 :
            sort_car(auto)

        case _ :
            print("Incorrect data")


def main():

    decore_msg ("Hello")

    decore_msg ("ENTER NUMBER OF OPTIONS")

    is_running = True

    run(is_running)

if __name__ == "__main__" :
    main()

# Write function
# 1) add_new_car input : (manufakturer,price) => auto
# 2) shaw_all_cars input : (arr_of_auto) -> show us every object into att
# 3) remove_auto_from_arr : (arr_of_auto , name_of_car) -> new_arr (without entered name_of_car)
# 4) get_expensive_car :  (arr_of_auto) -> if car's price over than 1800$ add it to expensive_car arr ,
# and then return it
