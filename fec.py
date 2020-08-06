import requests
# fec = FEC(API)

# fec.search_candidates(year=2020, district=00, election_year=2020, candidate_status="C", office="P").process()

# fec.search_candidate_by_id("P00014340").process()

class FEC:

    PER_PAGE = 20

    URL = 'https://api.open.fec.gov/v1'

    SCHEDULES = "/schedules/schedule_a{}/"

    CANDIDATE_URL = '/candidate/{}/'
    CANDIDATES_URL = '/candidates/{}/'

    CANDIDATES = {
        "SEARCH": "/candidates/search/",
        "FIND": "/candidate/"

    }
    PARAMETERS = {
        "STATUS": {
            "PRESENT": "C",
            "FUTURE": "F",
            "NOT": "N",
            "PRIOR": "P"
        },
        "OFFICE": {
            "HOUSE": "H",
            "SENATE": "S",
            "PRESIDENT": "P"
        },
        "PARTY": {
            "DEMOCRAT": "DEM",
            "REPUBLICAN": "REP"
        },
        "ELECTION_FULL": True, # True indicates that full election period of a candidate.
        "INCUMBENT_CHALLENGE": {
            "INCUMBENT": "I",
            "CHALLENGE": "C",
            "OPEN": "O"
        }
    }

    def __init__(self, key=None):
        self.api = key
        self.url = URL

    def _get(self, end_point, params):
        payload = params
        payload["api_key"] = self.api
        self.r = requests.get(self.url + end_point, params=payload)
        return self


    def search_candidates(self, **params):
        params["party"] = self.PARAMETERS["PARTY"]["REPUBLICAN"]
        return self._get(self.CANDIDATES_URL.format('search'), params)

    def search_candidate_by_id(self, id):
        return self._get(self.CANDIDATE_URL.format(id), {})

    def schedule_a(self, **params):
        return self._get(self.SCHEDULES.format(''), params)

    def process(self):
        print("Request URL: {}".format(self.r.url))
        results = self.r.json()['results']
        for r in results:
            print(r["name"])
            print(r["candidate_id"])








"""
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)

https://api.open.fec.gov/v1
/candidates/search/?
year=2020&api_key=ByMQIBq4bJSoLS5m2YHQQI4ehfCngzb2JBQaEyAZ&district=00&election_year=2020&candidate_status=C&sort=name&sort_null_only=false&sort_hide_null=false&per_page=20&sort_nulls_last=false&page=1


"""
"""
base_url = 'https://api.open.fec.gov/v1'

payload = {
    'year': '2020',
    'api_key': API,
    'candidate_status': 'C'
}


# r = requests.get(base_url + '/candidates/search/', params=payload)
r = requests.get("https://api.open.fec.gov/v1/candidates/search/?year=2020&api_key=ByMQIBq4bJSoLS5m2YHQQI4ehfCngzb2JBQaEyAZ&district=00&election_year=2020&candidate_status=C&incumbent_challenge=I&sort=name&office=P&sort_null_only=false&sort_hide_null=false&sort_nulls_last=false")
print(r.json()['results'][0]['candidate_id'])

r = requests.get(base_url + "/candidate/" + r.json()['results'][0]['candidate_id']+"/?api_key=" + API)

print(r.json())

"""
