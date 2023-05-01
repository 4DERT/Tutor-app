from flask import make_response, jsonify
import requests


def forward_response(r):
    cookies = r.cookies.get_dict()
    resp = make_response(jsonify(r.json()), r.status_code)
    for c in cookies:
        resp.set_cookie(c, cookies[c])
    return resp


def get_annocements():
    return requests.get("https://chatty-bulldog-76.telebit.io/announcements").json()


def filter_annoucements(search_for):
    search_for = search_for.lower()
    search_for = search_for.split()
    annocements = get_annocements()
    if len(search_for) == 0:
        return annocements
    filtered = []
    for a in annocements:
        values = str(a.values())
        values = values.lower()
        
        add = True
        for s in search_for:
            if values.find(s) < 0:
                add= False
        
        if add: 
            filtered.append(a) 
            
    return filtered
