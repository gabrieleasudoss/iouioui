import os
from datetime import datetime, timedelta

def make_commits(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
        with open('data.txt', 'a') as file:
            file.write(f'{formatted_date} <- this was the commit for the day!!\n')
        
        # Staging 
        os.system('git add data.txt')

        # Commit 
        os.system(f'git commit --date="{formatted_date}" -m "Commit for {formatted_date}"')

        # Increment to the next day
        current_date += timedelta(days=1 - 13)

start_date = datetime(2022, 1, 1)  # Replace with your desired start date
end_date = datetime(2022, 9, 13)  # Replace with your desired end date

make_commits(start_date, end_date)