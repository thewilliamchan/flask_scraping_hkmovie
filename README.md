# PROJECT HKMOVIE SCRAPING
# Looking for available showtimes for a selected movie on a specified date after a timepoint
# hkmovie6.com

## Requirements:
- Run `pip install -r requirements.txt`
- Download Geckodriver from https://github.com/mozilla/geckodriver/releases and place the geckodriver.exe in the project directory

## Compulsory parameters:
- Movie name `movie_name`; accept string values
- Month of the date `watch_month`; accept numeric values
- Day of the date `watch_day`; accept numeric values
- Hour of the date `watch_hour`; accept numeric values
- Minute of the date `watch_minute`; accept numeric values

## Output:
List of available showtimes with
- Cinema name
- Date
- Time
- Price

## Instructions:
Domain name: your defined IP address or hostname
URL (after domain name): `/movie_search?movie_name={parameter1}&watch_month={parameter2}&watch_day={parameter3}&watch_hour={parameter4}&watch_minute={parameter5}`

Example:

I want to watch **黑寡婦** on **Aug** **2** after **19**:**30** this year.

`movie_name`: **黑寡婦**

`watch_month`: **8**

`watch_day`: **2**

`watch_hour`: **19**

`watch_minute`: **30**

URL (after domain name):
`/movie_search?movie_name=黑寡婦&watch_month=8&watch_day=2&watch_hour=19&watch_minute=30`

## Important facts:
- Developed in macOS environment
- Requires high memory from the machine as there are many pages and many elements to process
- Dependant on the website HTML structure. If there is website revamp so that the HTML structure is changed on hkmovie6.com, this program might have to be modified
