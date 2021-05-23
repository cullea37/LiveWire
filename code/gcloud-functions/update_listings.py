#requirements.txt file should contain:
#google-cloud-firestore>=1.6.0
#ticketpy>=1.1.2

import ticketpy
import uuid
import ast
from google.cloud import firestore

def find_price_range(event_prange):
    if len(event_prange) == 2:
        return [str(event_prange[0]['min']),str(event_prange[1]['max'])]
    else:
        return []
             
def new_listings():
    tm_client = ticketpy.ApiClient('n87GZFAnAmTRKvAmZfItTkRPAU9E0JbY')
    db = firestore.Client()

    pages = tm_client.events.find(
        classification_name='Music',
        country_code = "IE")
    event_no = 1
    for page in pages:
        for event in page:
            doc_ref = db.collection('listings').document("{:04d}".format(event_no)).set({
                u'artists': event.name,
                u'startdate': str(event.local_start_date),
                u'starttime': str(event.local_start_time),
                u'locations': [str(i.name) for i in event.venues],
                u'pricerange': find_price_range(event.price_ranges),
                u'status': str(event.status)})
            event_no += 1
            if event_no == 100:
                break
        if event_no == 100:
            break
def update_listings(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    r = ast.literal_eval(str(request.data, "utf-8"))
    if r['schedule']:
        new_listings()