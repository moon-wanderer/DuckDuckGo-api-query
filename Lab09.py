import pytest
import requests as requests

url_ddg = "https://api.duckduckgo.com"
potus = {'Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk',
         'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur',
         'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman',
         'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump',
         'Biden'}
results = []
potus_found = []


def test_presidents():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data["RelatedTopics"]

    # append all text results to a list
    for topic in related_topics:
        results.append(topic["Text"])

    # append all found presidents to a list
    for president in potus:
        for result in results:
            if president in result:
                potus_found.append(president)
                break

    # check if all presidents were found
    assert set(potus_found) == potus
