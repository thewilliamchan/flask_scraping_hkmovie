# PROJECT HKMOVIE SCRAPING
# Looking for available showtimes for a selected movie on a specified date

## Requirements:
- Developed in a MacOS environment
- Run `pip install -r requirements.txt`
- Download Geckodriver from https://github.com/mozilla/geckodriver/releases and place the geckodriver.ext in the project directory
- For Windows environment, please put the full absolute path of the geckodriver.exe into the `executable_path` parameters in the following line of code
`driver = webdriver.Firefox(executable_path=f"{os.getcwd()}/geckodriver", options=options)`

## Compulsory parameters:
- Movie name `movie_name`; accept string values
- Month of the date `watch_month`; accept numeric values
- Day of the date `watch_day`; accept numeric values

## Output:
List of available showtimes with
- Cinema name
- Date
- Time

## Instructions:
URL: `127.0.0.1:5000/movie_search?movie_name={parameter1}&watch_month={parameter2}&watch_day={parameter3}`

Example:

I want to watch **黑寡婦** on **Aug** **2** this year.

`movie_name`: **黑寡婦**

`watch_month`: **8**

`watch_day`: **2**

URL:
`/movie_search?movie_name=黑寡婦&watch_month=8&watch_day=2`

## Future Enhancements:
Search by
- Time
- Region

Sort by
- Price

Output:
- price
