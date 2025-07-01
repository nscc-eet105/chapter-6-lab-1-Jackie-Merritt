
days = ('Sunday   ', 'Monday   ', 'Tuesday  ', 'Wednesday', 'Thursday ', 'Friday   ', 'Saturday ')

def main():
    print("Daily Sales Tracker\n")
    ammount_list = weekly_sales()
    total = calculate_total(ammount_list)
    average = calculate_average(total)
    

    print(f'\nTotal weekly sales    : $ {total:.2f}')
    print(f'Average weekly sales  : $ {average:.2f}')
    print(f'\nThe highest sales were ${max(ammount_list):.2f} on {days[ammount_list.index(max(ammount_list))]}')
    print(f'The lowest sales were ${min(ammount_list):.2f} on {days[ammount_list.index(min(ammount_list))]}')


def weekly_sales():
    ammount_list = []
    for d in days:
        m = float(input(f'Enter the sales amount for {d} : '))
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
