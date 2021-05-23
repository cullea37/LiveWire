#requirements.txt file should contain:
#spotify>=0.8.4
#google-cloud-firestore>=1.6.0

import asyncio
import spotify
from google.cloud import firestore
from typing import (Optional, Awaitable)

CLIENT_ID = "030016c2c30245a5a3325ffe9065833a"
CLIENT_SECRET = "a4355e96f13c4065ac7d7906fc40a6d1"
recommended_artists = set([])

async def get_top_artists(token, client):

    user = await client.user_from_token(token)
    top_longterm_artists = await user.top_artists(limit=50,offset=0, time_range="long_term")
    top_mediumterm_artists = await user.top_artists(limit=50,offset=0, time_range="medium_term")
    top_artists = top_longterm_artists + top_mediumterm_artists
    
    artist_names = []
    for artist in top_artists:
        r = await artist.related_artists()
        for related_artist in r:
            artist_names.append(related_artist.name)
        artist_names.append(artist.name)
    recommended_artists.update(artist_names)
    
async def get_saved_artists(token):
    user = spotify.HTTPUserClient(CLIENT_ID, CLIENT_SECRET, token)
    
    saved_tracks = await user.saved_tracks(limit=50,offset=0)
    saved_albums = await user.saved_albums(limit=50,offset=0)
    saved_tracks = saved_tracks['items']
    saved_albums = saved_albums['items']
    
    
    liked_artists = []
    for track in saved_tracks:
        for artist in track['track']['artists']:
            liked_artists.append(artist['name'])
            
    for album in saved_albums:
        for artist in album['album']['artists']:
            liked_artists.append(artist['name'])
            
    recommended_artists.update(liked_artists)
    

async def main(new_user_token):

    client = spotify.Client(CLIENT_ID, CLIENT_SECRET)
    
    await asyncio.gather(
        get_top_artists(new_user_token, client),
        get_saved_artists(new_user_token)
    )

def recommender(event, context):
    fclient = firestore.Client()
    path_parts = context.resource.split('/documents/')[1].split('/')
    
    parent = path_parts[0]
    user = path_parts[-1]
    document_path = parent + "/" + user
        
    new_user_token = event['value']['fields']['SpotifyToken']['stringValue']
    asyncio.get_event_loop().run_until_complete(main(new_user_token))
    print (parent, user, document_path)
    fclient.collection(parent).document(user).set({"recommendedArtists": dict.fromkeys(recommended_artists, 1)})   

"""
----EVENT EXAMPLE----
    {
    'oldValue': {},
    'updateMask': {},
    'value': 
        {
        'createTime': '2020-03-02T10:03:37.628031Z',
        'fields': 
            {
            'SpotifyToken': 
                {
                'nullValue': None
                }
            },
        'name': 'projects/livewire-ca/databases/(default)/documents/users/jCgBNIpSVlbXtgFGI4S4Yx5m6Jj2',
        'updateTime': '2020-03-02T10:03:37.628031Z'
        }
    }
    ----CONTEXT EXAMPLE----
    {
    event_id: 9a4ec5d6-2f16-4c0d-a3e8-f7354efd44b2-0,
    timestamp: 2020-03-02T10:03:37.628031Z,
    event_type: providers/cloud.firestore/eventTypes/document.write,
    resource: projects/livewire-ca/databases/(default)/documents/users/jCgBNIpSVlbXtgFGI4S4Yx5m6Jj2
    }
    """