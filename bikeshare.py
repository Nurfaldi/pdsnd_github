import time
import pandas as pd
import numpy as np

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    '''
    city = 'chicago'
    month = 'all'
    day = 'all'
    '''

    city_list = list()
    for key in CITY_DATA:
        city_list.append(key.title())

    print('-'*40)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Cities that are included in our data are: ' + color.BOLD + '{}, and {}\n'.format(", ".join(city_list[:-1]), city_list[-1]) + color.END)
    input("Please Press Enter to continue...")
    print('-'*40)

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Please input city name')
    while True:
        city = input("\nEnter city name: ").lower()
        if not (city in CITY_DATA or city == 'all') :
            print('\nPlease enter valid city name')
            continue
        else:
            break

    print('-'*40)

    # TO DO: get user input for month (all, january, february, ... , june)
    filter_month = input('Do you want to filter by Month [y/n]? ').lower()
    if filter_month == 'n':
        month = 'all'
    else:
        months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
        while True:
            month = input("\nPlease enter month name, you can write 'all' to show data from all month: ").lower()
            if not (month in months or month == 'all'):
                input('\nPlease enter valid month name for example: ' + color.BOLD + 'January' + color.END + '\nPress Enter to try again...')
                continue
            else:
                break

    print('-'*40)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    filter_day = input('Do you want to filter by Day Name [y/n]? ').lower()
    if filter_day == 'n':
        day = 'all'
    else:
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        while True:
            day = input("\nPlease enter day name, you can write 'all' to show data from all day: ").lower()
            if not (day in days or day == 'all'):
                input('\nPlease enter valid day name for example: ' + color.BOLD + 'Tuesday' + color.END + '\nPress Enter to try again...')
                continue
            else:
                break

    print('-'*40)

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('-'*40)

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return (df)

def data_head_print(df):

    # print data head by 5 lines if requested
    see_data_head = input('Do you want to see the first 5 lines of the data?, Enter y to continue[y/n]: ').lower()
    row_count = 0
    # print with the next 5 lines of data head if requested
    while see_data_head == 'y':
        row_count += 5
        print('\n {} \n'.format(df.head(row_count)))
        see_data_head = input('Do you want to see the next 5 lines of the data?, Enter y to continue[y/n]: ').lower()

    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month, if all months is choosen, print the chosen month
    popular_month = df['month'].mode()[0]
    months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    popular_month = months[popular_month - 1]
    if df['month'].nunique() != 1:
        print('Most Popular Month:', popular_month.title())
    else:
        print('You chose spcific month:', popular_month.title())

    # TO DO: display the most common day of week, if all months is choosen, print the chosen week
    popular_day = df['day_of_week'].mode()[0]
    if df['day_of_week'].nunique() != 1:
        print('Most Popular Month:', popular_day)
    else:
        print('You chose spcific day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["Start End Station"] = 'From ' + df['Start Station'] + ' to '+ df['End Station']
    Start_End_Station = df['Start End Station'].mode()[0]
    print('Most Popular Combination of Start and End Station:', Start_End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_sum = df['Trip Duration'].sum()
    print('Total Travel Time: {} Seconds or {} Minutes or {} Hours'.format(travel_time_sum, "%.2f"%(travel_time_sum/60),  "%.2f"%(travel_time_sum/3600)))

    # TO DO: display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print('Average Travel Time: {} Seconds or {} Minutes or {} Hours'.format(travel_time_mean, "%.2f"%(travel_time_mean/60), "%.2f"%(travel_time_mean/3600)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['User Type'].value_counts(),'\n'

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('there is no gender data in this city')
    print('\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]

        print('Earliest Birth Year: {} with {} person counts'.format(int(earliest_birth_year), df[df['Birth Year'] == earliest_birth_year]['Birth Year'].count()))
        print('Most Recent Birth Year: {} with {} person counts'.format(int(recent_birth_year), df[df['Birth Year'] == recent_birth_year]['Birth Year'].count()))
        print('Most Commonn Birth Year: {} with {} person counts'.format(int(common_birth_year), df[df['Birth Year'] == common_birth_year]['Birth Year'].count()))
    else:
        print('there is no birth year data in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

        # Input Block Check
        while True:
            city, month, day = get_filters()
            print("\nHere is your input prompt:\n\n    City: {} \n    month: {} \n    day: {}\n".format(color.BOLD + city.title() + color.END,color.BOLD + month.title() + color.END, color.BOLD + day.title() + color.END))
            print('-'*40)
            confirm_input = input('Confirm your choices, Enter y to continue[y/n]: ').lower()
            if confirm_input != 'y':
                print ('\nInput Values Not Confirmed Program Restarted\n')
                continue
            else:
                break

        # program end if dataframe is empty
        df = load_data(city, month, day)
        if df.empty == True:
            print('Filtered data empty, please start over the program and try another filter parameter')
            break

        data_head_print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter y to continue[y/n]:\n').lower()
        if restart.lower() != 'y':
            print("Thankyou for using our service :)")
            break


if __name__ == "__main__":
	main()
