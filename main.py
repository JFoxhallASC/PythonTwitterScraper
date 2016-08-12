
from TwitterAPI import TwitterAPI
api = TwitterAPI('HaRkHchUXROSHDqvBbynCsyDc', 'vs7vn4JFpV4VIq90LcwRaepB8yJQWitxEGyTzrn8HsNNxns962', '763153901323419649-gNJRtqOH7aSQ0bqqCaPkDC1ZoeJqqid', 'Xe5eGwZ9buxvDBBKJbwGKuQC3ADsw21bg5QKAQBRyxuVL')


r = api.request('search/tweets', {'q':'#tweetsweep679'})
for item in r:
    print(item['coordinates'])
    print(item['id'])
    place = item['coordinates']
    thing = item['id']


def sendToFirebase(place, thing):
    
