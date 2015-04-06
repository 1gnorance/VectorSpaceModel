__author__ = 'aferraz'

import json, requests, re

class GPlus:
    url = "https://www.googleapis.com/plus/v1/activities"
    key = "AIzaSyCAAzF35cGixGPpcoc6xwIttI9HaFff07M"

    def __init__(self, key):
        self.key = key

    def __init__(self):
        pass

    def getActivities(self, query):
        #https://www.googleapis.com/plus/v1/activities?query=dilma&key=AIzaSyCAAzF35cGixGPpcoc6xwIttI9HaFff07M

        params = dict(
            query=query,
            key=self.key,
        )

        resp = requests.get(url=self.url, params=params)
        data = json.loads(resp.text)

        return data

    def getContentActivities(self, query):
        activities = self.getActivities(query)["items"]

        data = []

        for item in activities:
            data.append(self.remove_tags(item["object"]["content"]))

        return data

    def remove_tags(self, raw_html):
        cleanr =re.compile('<.*?>')
        cleantext = re.sub(cleanr,'', raw_html)
        return cleantext