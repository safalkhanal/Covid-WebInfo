from django.shortcuts import render
import json
import urllib.request
import urllib.parse
from operator import itemgetter
from django.http import JsonResponse
from django.http import HttpResponse


def index(request):
    url = "https://api.covid19api.com/summary"
    data = urllib.request.urlopen(url).read()
    obj = json.loads(data)
    country = obj['Countries']
    country = sorted(country, key=lambda k: (-k['TotalConfirmed']))
    return render(request,
                  'index.html',
                  {'country': country,
                   'totalConfirmed': obj['Global']['TotalConfirmed'],
                   'newConfirmed': obj['Global']['NewConfirmed'],
                   'newDeaths': obj['Global']['NewDeaths'],
                   'totalDeaths': obj['Global']['TotalDeaths'],
                   'newRecovered': obj['Global']['NewRecovered'],
                   'totalRecovered': obj['Global']['TotalRecovered'],
                   }
                  )


def country(request, country_code):
    url = "https://api.covid19api.com/summary"
    data = urllib.request.urlopen(url).read()
    obj = json.loads(data)
    country_details = obj['Countries']

    for items in country_details:
        if country_code == items['CountryCode']:
            detail_url = "https://api.covid19api.com/total/country/" + items['Country']
            #replacing spaces in url and validating the url
            valid_url = urllib.parse.quote(detail_url).replace('%3A', ':')
            data = urllib.request.urlopen(valid_url).read()
            details = json.loads(data)
            return render(request,
                          'countrydetails.html',
                          {'details': details,
                           'country': items}
                          )
        else:
            continue


def test(request):
    url = "https://api.covid19api.com/summary"
    data = urllib.request.urlopen(url).read()
    # parse json object
    obj = json.loads(data)
    # return HttpResponse(obj['Countries'])
    return render(request,
                  'test.html',
                  {'country': obj['Countries'],
                   'totalConfirmed': obj['Global']['TotalConfirmed']}
                  )
