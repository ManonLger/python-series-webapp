Overview:
This service gathers most popular series and provides information on series: overview, seasons, episodes, etc.
After registering, each user manages his wishlist by adding and deleting series.

Pre-requisite:
- Install the latest version of Python 3.6 (make sure pip is installed on your computer)
- Install Django through your terminal: `pip install django`
- Install the module Requests through your terminal: `pip install requests`

Steps to download the app:
- Clone the repo: `git clone https://github.com/Manon-L/python-series-webapp.git`
- On TMDB (`https://www.themoviedb.org`), ask for a new API key
- Add a file `env.py` in the folder `gitmyseries/site_gitmyseries` and write on it: `TMDB_API_KEY = "<Your_API_key>"`

Steps to run the application:
- Go to the folder « site_series » in your terminal: `cd site_series`
- Run the following command in your terminal: `python manage.py runserver`
- Browse: `localhost:8000/gitmyseries/`
