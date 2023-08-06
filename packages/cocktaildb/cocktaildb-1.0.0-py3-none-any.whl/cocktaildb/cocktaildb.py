# Copyright 2022 XXIV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import http.client as client
from types import SimpleNamespace
import json
from urllib.parse import quote_plus


def http(endpoint):
    try:
        conn = client.HTTPSConnection('www.thecocktaildb.com')
        conn.request('GET', f'/api/json/v1/1/{endpoint}')
        data = conn.getresponse().read().decode('UTF-8')
        conn.close()
        return data
    except:
        return None


def search(s: str):
    """
    Search cocktail by name
    :param s: cocktail name
    :return: list of objects
    """
    try:
        response = http(f"search.php?s={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks
            else:
                return None
        else:
            return None
    except:
        return None


def search_by_letter(c: str):
    """
    Search cocktails by first letter
    :param c: cocktail letter
    :return: list of objects
    """
    try:
        response = http(f"search.php?f={c}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks
            else:
                return None
        else:
            return None
    except:
        return None


def search_ingredient(s: str):
    """
    Search ingredient by name
    :param s: ingredient name
    :return: object
    """
    try:
        response = http(f"search.php?i={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.ingredients is not None:
                return data.ingredients[0]
            else:
                return None
        else:
            return None
    except:
        return None


def search_by_id(i: int):
    """
    Search cocktail details by id
    :param i: cocktail id
    :return: object
    """
    try:
        response = http(f"lookup.php?i={i}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks[0]
            else:
                return None
        else:
            return None
    except:
        return None


def search_ingredient_by_id(i: int):
    """
    Search ingredient by ID
    :param i: ingredient id
    :return: object
    """
    try:
        response = http(f"lookup.php?iid={i}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.ingredients is not None:
                return data.ingredients[0]
            else:
                return None
        else:
            return None
    except:
        return None


def random():
    """
    Search a random cocktail
    :return: object
    """
    try:
        response = http("random.php")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks[0]
            else:
                return None
        else:
            return None
    except:
        return None


def filter_by_ingredient(s: str):
    """
    Filter by ingredient
    :param s: ingredient name
    :return: list of objects
    """
    try:
        response = http(f"filter.php?i={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks
            else:
                return None
        else:
            return None
    except:
        return None


def filter_by_alcoholic(s: str):
    """
    Filter by alcoholic
    :return: list of objects
    """
    try:
        response = http(f"filter.php?a={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks
            else:
                return None
        else:
            return None
    except:
        return None


def filter_by_category(s: str):
    """
    Filter by Category
    :param s: Category
    :return: list of objects
    """
    try:
        response = http(f"filter.php?c={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks
            else:
                return None
        else:
            return None
    except:
        return None


def filter_by_glass(s: str):
    """
    Filter by Glass
    :param s: glass name
    :return: list of objects
    """
    try:
        response = http(f"filter.php?g={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                return data.drinks
            else:
                return None
        else:
            return None
    except:
        return None


def categories_filter():
    """
    List the categories filter
    :return: list of categories
    """
    try:
        response = http("list.php?c=list")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                data_list = []
                for i in data.drinks:
                    data_list.append(i.strCategory)
                return data_list
            else:
                return None
        else:
            return None
    except:
        return None


def glasses_filter():
    """
    List the glasses filter
    :return: list the glasses
    """
    try:
        response = http("list.php?g=list")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                data_list = []
                for i in data.drinks:
                    data_list.append(i.strGlass)
                return data_list
            else:
                return None
        else:
            return None
    except:
        return None


def ingredients_filter():
    """
    List the ingredients filter
    :return: list the ingredients
    """
    try:
        response = http("list.php?i=list")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                data_list = []
                for i in data.drinks:
                    data_list.append(i.strIngredient1)
                return data_list
            else:
                return None
        else:
            return None
    except:
        return None


def alcoholic_filter():
    """
    List the alcoholic filter
    :return: list the alcoholic
    """
    try:
        response = http("list.php?a=list")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.drinks is not None:
                data_list = []
                for i in data.drinks:
                    data_list.append(i.strAlcoholic)
                return data_list
            else:
                return None
        else:
            return None
    except:
        return None
