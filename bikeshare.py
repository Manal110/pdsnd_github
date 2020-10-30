import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Peaes enter the city you want to see the data for(chicago, new york city or washington): \n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('invalid input!!  \n')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Peaes enter the month by number, January=1, February=2, March=3, April=4, May=5, or June=6 or you can enter "All" for all months: \n').lower()
        if month in ['all','1', '2', '3', '4', '5', '6']:
            break
        else:
            print('invalid input!! \n')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Peaes enter the day. Ex: monday, tuesday..etc or you can enter "All" for all days:\n').lower()
        if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('invalid input!!\n')

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
    # load data for the enterd city
    df = pd.read_csv(CITY_DATA[city])
    
    # change 'start time' type from object to datetime to get the month and the day from it
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #gets month from start date then filters by month in case user entered a month
    df['ext_month'] = df['Start Time'].dt.month
    if month != 'all':
        month=int(month)
        df = df[df['ext_month'] == month]
    
    
     #gets day from start date then filters by day in case uesr entered a week day 
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['weekday']=df['weekday'].str.lower()
    if day !='all':
       df = df[df['weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print ('the most common month is:\n',df['ext_month'].mode()[0]) # selcting [0] to get the mode of the coulms only

    # TO DO: display the most common day of week
    print ( 'the most common day of week is:\n',df['weekday'].mode()[0])

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print ( 'the most common start hour is:\n',df['start_hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station is:\n',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print(' most commonly used end station is:\n',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination']= 'start: '+df['Start Station']+','+' end: '+df['End Station']
    print('most frequent combination of start station and end station trip is:\n',df['station_combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time (travel Time= Trip duration)
    print('total of travel time is:\n',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean of travel time is:\n',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types (subsecribers or customers)
    print('counts of user types:\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender

    print('counts of gender:\n',df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    #calculate values
    earliest=df['Birth Year'].min()
    recent=df['Birth Year'].max()
    common=df['Birth Year'].mode()[0]
   
    
    #print values as int
    print('earliest year of birth is:\n',int(earliest))
    print('most recent year of birth is:\n',int(recent))
    print('most common year of birth is:\n',int(common))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
<<<<<<< HEAD

#completed by Manal Alshehri
||||||| merged common ancestors
=======

#Completed by Manal
#for Udacity nano degree program
#program name: Programming for data since 
#30 oct 2020
>>>>>>> refactoring
