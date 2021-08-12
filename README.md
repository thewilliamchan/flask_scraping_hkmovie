# PROJECT HKMOVIE SCRAPING
# Looking for available showtimes for a selected movie on a specified date after a timepoint
# hkmovie6.com

## Requirements:
- Run `pip install -r requirements.txt`
- Download Geckodriver from https://github.com/mozilla/geckodriver/releases and place the geckodriver.exe in the project directory
- Install firefox on your machine

## Compulsory parameters:
- Movie name `name`; accept string values
- Month of the date `month`; accept numeric values
- Day of the date `day`; accept numeric values
- Hour of the date `hour`; accept numeric values
- Minute of the date `minute`; accept numeric values

## Output:
List of available showtimes with
- Cinema name
- Date
- Time
- Price

## Instructions:
Domain name: your defined IP address or hostname
URL (after domain name): `/movie_search?name={parameter1}&month={parameter2}&day={parameter3}&hour={parameter4}&minute={parameter5}`

Example:

I want to watch **黑寡婦** on **Aug** **2** after **19**:**30** this year.

`name`: **黑寡婦**

`month`: **8**

`day`: **2**

`hour`: **19**

`minute`: **30**

URL (after domain name):
`/movie_search?name=黑寡婦&month=8&day=2&hour=19&minute=30`

## Important facts:
- Developed in macOS environment
- Requires high memory from the machine as there are many pages and many elements to process
- Dependant on the website HTML structure. If there is website revamp so that the HTML structure is changed on hkmovie6.com, this program might have to be modified
