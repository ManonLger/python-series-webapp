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
    result_list = json.loads(r)["results"]

    paginator = Paginator(result_list, 5)  # 10 liens par page
    page = request.GET.get('page')
    try:
        # La définition de nos URL autorise comme argument « page » uniquement
        # des entiers, nous n'avons pas à nous soucier de PageNotAnInteger
        result = paginator.page(page)
    except EmptyPage:
        # Nous vérifions toutefois que nous ne dépassons pas la limite de page
        # Par convention, nous renvoyons la dernière page dans ce cas
        result = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        result = paginator.page(1)
    return render(request, 'app_series/search.html', locals())
