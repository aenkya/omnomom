from mtnmomo.collection import Collection

import settings as settings

# Initialise collection
client = Collection({
    "COLLECTION_USER_ID": settings.COLLECTION_USER_ID,
    "COLLECTION_API_SECRET": settings.COLLECTION_API_SECRET,
    "COLLECTION_PRIMARY_KEY": settings.COLLECTION_PRIMARY_KEY
})

if __name__=='__main__':
    # request to pay
    res = client.requestToPay(
        mobile='256772343555',
        amount='600',
        external_id='123456789',
        payee_note='test',
        payer_message='test',
        currency='EUR'
    )
    print(res)