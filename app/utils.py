import base64
from uuid import uuid4

def short_uuid():
    return base64.urlsafe_b64encode(uuid4().bytes)[:12].decode("utf-8")