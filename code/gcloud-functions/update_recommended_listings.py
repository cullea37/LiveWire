#requirements.txt file should contain:
#google-cloud-firestore>=1.6.0

from google.cloud import firestore

def update_recommended_listings(event, context):
    #print (event)
    #print (context)

    fclient = firestore.Client()
    path_parts = context.resource.split('/documents/')[1].split('/')
    users = fclient.collection("users").stream()
    for doc in users:
        new_listing_artists = event['value']['fields']['artists']['stringValue']
        recommended_artists = doc.to_dict()['recommendedArtists']
        
        if any([rec_artist == new_listing_artists for rec_artist in recommended_artists]):
            fclient.collection("notifications").document(doc.id).set(
                {u'recommendedListings': firestore.ArrayUnion([path_parts[1]])})
                
"""
'oldValue': {},
 'updateMask': {},
 'value': {'createTime': '2020-03-04T18:02:21.491183Z', 'fields': {'artists': {'stringValue': 'Blossoms'}, 'locations': {'arrayValue': {'values': [{'stringValue': 'Olympia Theatre'}]}}, 'pricerange': {'arrayValue': {'values': [{'stringValue': '27.0'}, {'stringValue': '31.5'}]}}, 'startdate': {'stringValue': '2020-03-04'}, 'starttime': {'stringValue': '19:00:00'}, 'status': {'stringValue': 'onsale'}}, 'name': 'projects/livewire-ca/databases/(default)/documents/listings/4b5f078a-5e42-11ea-a394-87698385c8ae', 'updateTime': '2020-03-04T18:02:21.491183Z'}}
 """