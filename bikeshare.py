import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_data = ['january', 'february', 'march', 'april', 'may', 'june', 'all' ]

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']


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
    city = input('Enter the cityname, Please Choose between Chicago, New York City, or Washington: \n').lower()                           
    while city not in CITY_DATA.keys():     
      print('Oops! it appears that you have entered a wrong city. Please Choose between Chicago, New York City, or Washington \n')
      city = input('Enter the cityname, Please Choose between Chicago, New York City, or Washington: \n').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
      # get user input for month (all, january, february, ... , june)

    month = input('Which month do you want to look at? or enter all if you do not want to filter the month:\n').lower()
    while month not in months_data:
        print('Oops! Looks like you have entered a wrong month. Please try again!\n')
        month = input('Which month do you want to look at? or enter all if you do not want to filter the month:\n').lower()

    day = input('Which weekday are you interested  to look at ?\nchoose between : monday tuesday  wednesday  thursday  friday  saturday sunday or all if you want to select all days:):\n').lower()
    while day not in days:
        print('Oops! Looks like you have entered a wrong day.  try again!')
        day = input('Which weekday are you interested  to look at ? \n choose between : monday tuesday  wednesday  thursday  friday  saturday sunday or all if you want to select all days:\n').lower()
         
        
    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time and End Time to datatime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #get month / week day / hour from Start Time
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day'] = df['Start Time'].dt.day
    

    # to apply filters by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months_data.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the weekday list to get the corresponding int
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print('Most Popular Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


 #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////      


 

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print("The most often selected start station is: " +
          common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most often selected end station is: " 
        + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['Start and End Stations'] = df['Start Station'] + ' --> ' + df['End Station']
    common_combo_station = df['Start and End Stations'].mode()[0]
    print('The most common station to start at was {}.\nThe most common station to end at was {}.\nThe most common trip was {}.'.format(common_start_station, common_end_station, common_combo_station))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("\n- The total travel time based on your selection is: " +
          str(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("- The mean travel time based on your selection is: " +
          str(mean_time))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
    
    
    # TO DO: Display counts of user types
    
    user_type = df['User Type'].value_counts()
    print("The count of user types based on your selection is: \n" + str(user_type))


    # TO DO: Display counts of gender
    if 'Gender' in df:
     gender_count = df['Gender'].value_counts()
     print("The numbers of user gender based on your selection is: \n" + str(gender_count))
    else:
     print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest=df['Birth Year'].min()
        max_recent=df['Birth Year'].max()
        most_common=df['Birth Year'].mode()[0]
    
        print('\n The Earliest Year of Birth: ',earliest)
        print('The Most Recent Year of Birth: ',max_recent)
        print('The Most Common Year of Birth: ',most_common)
    
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
    
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you want to see 5 rows of individual travel data? Please enter a yes or no \n')
    start_loc = 0
    while (view_data) == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Would you like to continue with the next five rows ? Please enter a yes or no \n'").lower()
        continue 
        view_data = input('\n Would you like to continue with the next five rows ? Please enter a yes or no \n \n')
def main():
    while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)

       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)
       display_data(df)
        
       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
    
    
    
