from mtnmomo.collection import Collection

import settings as settings

client = Collection({
    "COLLECTION_USER_ID": settings.COLLECTION_USER_ID,
    "COLLECTION_API_SECRET": settings.COLLECTION_API_SECRET,
    "COLLECTION_PRIMARY_KEY": settings.COLLECTION_PRIMARY_KEY
})
