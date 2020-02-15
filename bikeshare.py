import time
import pandas as pd
import numpy as np





"""
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "No" to apply no month filter
        (str) day - name of the day of week to filter by, or "No" to apply no day filter

"""
   # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

""" I am asking the user for which city they would like to see the data from. """

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Please input city name: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("City is name is invalid! Please input either (chicago,new york city or washington): ").lower()
        continue
        break


    while 1:
        respones_month = input("Would you like to take a look at any particular month: Yes or No: ").lower()
        if respones_month == "yes":
            respones_month=True
        elif respones_month == "no":
            respones_month=False
        else:
            input("You did not enter a valid response, please enter Yes or No: ").lower()
            continue
        break

    while 1:
        if respones_month:
            month = input("What month would you like to take a look at? January, February, March, April, May or June: ").lower()
            while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                month = input("Sorry that is not a correct month. Please try again: ").lower()
                continue
        else:
            print("We will just pull up the entire data set for you....")
            month = 'all'
        break

    while 1:
        respones_day = input("Would you like to take a look at a specific day of the week? (yes/no): ").lower()
        if respones_day == "yes":
            respones_day=True
        elif respones_day == "no":
            respones_day=False
        else:
            respones_day = input("you did not enter a valid response, please enter Yes or No: ").lower()
            continue
        break

    while 1:
        if respones_day:
            day = input("what day would you like to look at?: ").lower
            while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                day = input("sorry that is not a valid day, please try again: ").lower()
                continue
        else:
            print("no problem we will pull up the entire data set for")
            day = 'all'
        break

    print('-'*40)
    return city, month, day

"""
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
"""

def load_data(city, month, day):

    df = pd.read_csv("{}.csv".format(city.replace(" ", "_")))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    start_time = time.time()
    #find Most popular Month.
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    #Find most popular day of week.
    popular_day = df['day_of_week'].mode()[0]
    print("The most popular day of the week is: {}".format(popular_day))


    # Find most popular Start Time.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    print("most popular start time is the {}th hundred hour ".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("The most commonly used start station is: {}".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station

    print("The most commonly used end station is: {}".format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip

    freq_combination_station = df['Start Station'] + " " + "to" + " " + df['End Station']
    print("The most frequently combined Start and End stations are: {}". format(freq_combination_station.mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time of every user.
    df['Duration'] = df['End Time'] - df['Start Time']


    #Diplay the the sum of all users travel times.
    print("the total travel time for all users is {}".format(df['Duration'].sum()))


    # TO DO: display mean travel time

    print("the mean travel time is {}".format(df['Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displaying statistic related to users"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if city != 'washington':
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else:
        print("Sorry Washington does not have any information on Gender")

     # TO DO: Display earliest, most recent, and most common year of birth
    #Ealriest Year
    if city != 'washington':
        oldest = df['Birth Year'].min()
        print("The edlest birth year using this service is: {}".format(oldest))


    #Most Recent Year
    if city != 'washington':
        youngest = df['Birth Year'].max()
        print("he most recent birth year using this service is: {}".format(youngest))

    #Most common Year
    if city != 'washington':
        mean_year = df['Birth Year'].mean()
        print("The most common year is: {}".format(mean_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        def funl():
            return time_stats(df)

        ts = input("Would you like to look at statistics realated to time?: ").lower()
        while 1:
            if ts == "yes":
                funl()
                break
            elif ts == "no":
                print("moving on to next... ")
                break
            else:
                ts = input("Sorry that was not a valid input, please respond (yes/no): ").lower()
                continue

        def funl2():
            return station_stats(df)

        ss = input("Would you like to look at statistics realated to stations?: ").lower()
        while 1:
            if ss == "yes":
                funl2()
                break
            elif ts == "no":
                print("moving onto next...")
                break
            else:
                ss = input("Sorry that was not a valid input, please respond (yes/no): ").lower()
                continue

        def funl3():
            return trip_duration_stats(df)

        tds = input("Would you like to look related to trip duration? (yes/no): ").lower()
        while 1:
            if tds == 'yes':
                funl3()
                break
            elif tds =='no':
                print("moving onto next....")
                break
            else:
                tds = input("Sorry that as not a valid input, please respond with yes or no: ").lower()
                continue

        def funl4():
            return user_stats(df,city)

        us = input("Would you like to take a look at stats related to users? (yes/no):  ").lower()
        while 1:
            if us == 'yes':
                funl4()
                break
            elif us == 'no':
                print("moving onto next....")
                break
            else:
                input("Sorry but that is not a valid input, please respond yes or no: ").input()
                continue

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
