import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    
def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    
     # get user input for city (chicago, new york city, washington)
    city = input('Enter city name: (chicago, new york city, or washington)\n').lower()
    while(city not in CITY_DATA):
        city = input('You did not write the city name correctly, try again: ').lower()
          
    # get user input for month (all, january, february, ... , june)
    month = input('Enter the month name: (all, january, february, march, ...)\n').lower()
    while (month not in MONTHS):
        month = input('You did not write the month correctly, try again: ').lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day name: (all, monday, tuesday, wednesday, ...)\n').lower()
    while (day not in DAYS):
        day = input('You did not write the day correctly, try again: ').lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month 
    if month != 'all':
        month = MONTHS.index(month)
        df = df[df['month'] == month]
        
    # filter by day
    if day != 'all':
        day = day.capitalize()
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is: ' + MONTHS[df.month.value_counts().index[0]])
   
    # display the most common day of week
    print('The most common day of week is: ' + df.day_of_week.value_counts().index[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ' + str(df.hour.value_counts().index[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # display most commonly used start station
    print('The most commonly used start station: ' + str(df['Start Station'].value_counts().index[0]))


    # display most commonly used end station
    print('The most commonly used end station: ' + str(df['End Station'].value_counts().index[0]))


    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip respectively: ' + str(df.groupby(['Start Station','End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('Total travel time: {}s, {:.2f}m, {:.2f}h'.format(total , total/60, total/60/60))


    # display mean travel time
    average = df['Trip Duration'].mean()
    print('Average travel time: {:.2f}s, {:.2f}m, {:.2f}h'.format(average, average/60, average/60/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, c):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('count of user types: \n' + str(df['User Type'].value_counts()))


    # Display counts of gender
    # no gender data for washington city table
    if c == 'washington':
        print('there is no GENDER data for washington city')
    else: 
        print('counts of gender: \n' + str(df.Gender.value_counts()))


    # Display earliest, most recent, and most common year of birth
    # no year of birth data in washington table 
    if c == 'washington':
        print('there is no YEAR OF BIRTH data for washington city')
    else: 
        print('Earliest year of birth: ' + str(int(df['Birth Year'].min()))) 
        print('Most recent year of birth: ' + str(int(df['Birth Year'].max())))
        print('Most common year of birth: ' + str(int(df['Birth Year'].value_counts().index[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_rows(df):
    counter = 0 
    while True: 
        display_data = input('would you like to see 5 lines of the raw data?\n').lower()
        
        if display_data == 'yes':
            print(df.iloc[counter:counter+5]) 
            counter += 5 
        elif display_data == 'no': 
            break
        else:
            print('I dont get it, try again, ')
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_rows(df)
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
