from firebase import firebase
from TwitterAPI import TwitterAPI

api = TwitterAPI('HaRkHchUXROSHDqvBbynCsyDc', 'vs7vn4JFpV4VIq90LcwRaepB8yJQWitxEGyTzrn8HsNNxns962', '763153901323419649-gNJRtqOH7aSQ0bqqCaPkDC1ZoeJqqid', 'Xe5eGwZ9buxvDBBKJbwGKuQC3ADsw21bg5QKAQBRyxuVL')
firebase = firebase.FirebaseApplication('https://tweetsweep-d70a2.firebaseio.com', None)

r = api.request('search/tweets', {'q':'#tweetsweep679'})
for item in r:
    place = item['coordinates']
    ident = item['id']
    firebase.post('/',{'coordinates':place, 'id':ident})
