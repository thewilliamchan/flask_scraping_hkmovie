from flask import Flask
from flask import request
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h3>Please enter the movie name you would like to watch with a date.</h3> 
    <h3>We would help you to look for available schedules in all the cinemas in HK.</h3>
    <h4>Example: I want to watch <span style='color:#134e6f'>黑寡婦</span> on <span style='color:#ffa822'>Aug</span> <span style='color:#ff6150'>2</span> this year.</h4>
    <h4>URL would be: /movie_search?movie_name=<span style='color:#134e6f'>黑寡婦</span>&watch_month=<span style='color:#ffa822'>8</span>&watch_day=<span style='color:#ff6150'>2</span></h4> 
    """

@app.route("/movie_search")
def movie_search():
    movie_name = request.args.get("movie_name")
    watch_month = request.args.get("watch_month")
    watch_day = request.args.get("watch_day")

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(executable_path=f"{os.getcwd()}/geckodriver", options=options)
    driver.get("https://hkmovie6.com/")

    # ===== SEARCH =====
    search = driver.find_element_by_css_selector("div.search-wrapper")
    search.click()
    search_input = driver.find_element_by_css_selector("div.searchOverlayWrapper input")
    # User variable 1
    search_input.send_keys(movie_name)
    driver.implicitly_wait(10)
    first_search_result_name = driver.find_element_by_css_selector("div.searchOverlayMovies a.movie").text
    if movie_name != first_search_result_name:
        search_results = driver.find_elements_by_css_selector("div.searchOverlayMovies a.movie")
        result_list = []
        for result in search_results:
            result_list.append(result.text)
            potential_movie_names = "<h4>Your movie name cannot be matched. Are you looking for?</h4>"
            for potential_movie_name in result_list:
                potential_movie_names += f"<p>{potential_movie_name}</p>"
        driver.close()
        return potential_movie_names
    first_search_result = driver.find_element_by_css_selector("div.searchOverlayMovies a.movie")
    first_search_result.click()

    # ===== DATE CHECK =====
    driver.switch_to.window(driver.window_handles[1])
    schedule_btn = driver.find_element_by_css_selector("div.buttons button")
    schedule_btn.click()
    # User variable 2
    search_date_month = int(watch_month)
    print(search_date_month)
    # User variable 3
    search_date_day = int(watch_day)
    print(search_date_day)
    search_after_time = '20:00'
    movie_dates = driver.find_elements_by_css_selector("div.showDates div.swiper-wrapper div.swiper-slide div.date")
    showtime_date = datetime.datetime.now()
    if movie_dates is None:
        driver.close()
        return f"<h4>Unfortunately no available showtime for <span style='color:#134e6f'>{movie_name}</span>. Would you consider another day or another movie?</h4>"
    for movie_date in movie_dates:
        date_matched = False
        movie_date_month = movie_date.text.split("/")[1]
        movie_date_day = movie_date.text.split("/")[0]
        movie_date_full = datetime.datetime(datetime.datetime.now().year, int(movie_date_month), int(movie_date_day))
        search_date_full = datetime.datetime(datetime.datetime.now().year, search_date_month, search_date_day)
        if movie_date_full == search_date_full:
            date_matched = True
            break
    if not date_matched:
        driver.close()
        return f"<h4>Unfortunately no available showtime for <span style='color:#134e6f'>{movie_name}</span>. Would you consider another day or another movie?</h4>"
    showtime_date = movie_date_full
    movie_date.click()

    # ===== GET SCHEDULES =====
    driver.implicitly_wait(10)
    cinemas = driver.find_elements_by_css_selector("div.cinemas div.cinema")
    matched_showtime_list = []
    for cinema in cinemas:
        cinema_name = cinema.find_element_by_css_selector("div.cinemaName").text
        showtimes = cinema.find_elements_by_css_selector("div.show div.time[style='background-color: rgb(3, 151, 4);']")
        for showtime in showtimes:
            showtime_time = showtime.text
            matched_showtime_list.append([cinema_name, showtime_date.strftime("%Y-%m-%d"), showtime_time])
    matched_showtime_results = f"<h4>There are available showtimes for <span style='color:#134e6f'>{movie_name}</span>!</h4>"
    for matched_showtime in matched_showtime_list:
        matched_showtime_results += f"<tr><td>{matched_showtime[0]}</td><td>{matched_showtime[1]}</td><td>{matched_showtime[2]}</td></tr>"
    driver.close()
    return "<table>" + matched_showtime_results + "</table>"
