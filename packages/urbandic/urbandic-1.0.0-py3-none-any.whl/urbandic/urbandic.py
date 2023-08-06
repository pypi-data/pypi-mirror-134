# Copyright (c) 2022 XXIV

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, andor sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import http.client as client
from types import SimpleNamespace
import json
from urllib.parse import quote_plus


def http(endpoint):
    try:
        conn = client.HTTPSConnection('api.urbandictionary.com')
        conn.request('GET', f'/v0/{endpoint}')
        data = conn.getresponse().read().decode('UTF-8')
        conn.close()
        return data
    except:
        return None


def search(input: str, page: int):
    try:
        response = http(f"define?term={quote_plus(input)}&page={page}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.list is not None and len(data.list) != 0:
                return data.list
            else:
                return None
        else:
            return None
    except:
        return None


def random():
    try:
        response = http("random")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.list is not None and len(data.list) != 0:
                return data.list
            else:
                return None
        else:
            return None
    except:
        return None


def definition_by_id(id: int):
    try:
        response = http(f"define?defid={id}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.list is not None and len(data.list) != 0:
                return data.list[0]
            else:
                return None
        else:
            return None
    except:
        return None


def tool_tip(term: str):
    try:
        response = http(f"tooltip?term={quote_plus(term)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.string is not None:
                return data.string
            else:
                return None
        else:
            return None
    except:
        return None
