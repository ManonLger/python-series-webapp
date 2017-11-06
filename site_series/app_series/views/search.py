from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests, json
import site_series.settings as settings

def search(request, query, page=1):
    params = {
        "query": query,
        "api_key": settings.TMDB_API_KEY,
        "language": "en-US"
    }
    r = requests.get(settings.TMDB_API_URL + "search/tv", params=params).content.decode()
    #get the endpoint of tmdb API for the search feature and decode it to be used
    result_list = json.loads(r)["results"]

    paginator = Paginator(result_list, 5)  # 5 links per page
    page = request.GET.get('page') 
    try:
        result = paginator.page(page)
    except EmptyPage:
        result = paginator.page(paginator.num_pages) #if the page is empty, return to the last page of pagination
    except PageNotAnInteger:
        result = paginator.page(1) #return to the  first page of the search
    return render(request, 'app_series/search.html', locals()) #return to the search template 
