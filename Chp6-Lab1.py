#Jackie_Merritt-Chp6_Lab1-6/28/2025
days = ('Sunday   ', 'Monday   ', 'Tuesday  ', 'Wednesday', 'Thursday ', 'Friday   ', 'Saturday ')

def main():
    print("Daily Sales Tracker\n")
    #Takes the value from weekly_sales() and translates it into a list.
    ammount_list = weekly_sales()
    #Calculates the total ammount via the calculate_total function and translates it to the variable 'total'.
    total = calculate_total(ammount_list)
    #Calculates average and translates it to the variable 'average'
    average = calculate_average(total)
    
    #Prints out total and average sales as well as the highest, lowest, and days correlated to highest and lowest.
    print(f'\nTotal weekly sales    : $ {total:.2f}')
    print(f'Average weekly sales  : $ {average:.2f}')

    #Takes the place number for the highest and lowest values and translates them to the days tuple
    print(f'\nThe highest sales were ${max(ammount_list):.2f} on {days[ammount_list.index(max(ammount_list))]}')
    print(f'The lowest sales were ${min(ammount_list):.2f} on {days[ammount_list.index(min(ammount_list))]}')


def weekly_sales():
    #sets an empty list
    ammount_list = []
    for d in days:
        m = float(input(f'Enter the sales amount for {d} : '))
        #adds to the empty list each of the entered ammounts
        ammount_list.append(m)
    return ammount_list

def calculate_total(ammount_list):
    total = 0
    for value in ammount_list:
        total += value
    return total

def calculate_average(total):
    return total / 7 

if __name__ == '__main__':
    main()
