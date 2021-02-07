import os
from chalice import Chalice, BadRequestError
from nacl.signing import VerifyKey

app = Chalice(app_name='smolbreinsystem')

PUBLIC_KEY = os.getenv("DISCORD_PUBLIC_KEY")
RESPONSE_TYPES =  { 
    "PONG": 1, 
    "ACK_NO_SOURCE": 2, 
    "MESSAGE_NO_SOURCE": 3, 
    "MESSAGE_WITH_SOURCE": 4, 
    "ACK_WITH_SOURCE": 5
}


def verify_signature(request):
    raw_body = request.raw_body
    auth_sig = request.headers.get('x-signature-ed25519')
    auth_ts  = request.headers.get('x-signature-timestamp')
    
    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    verify_key.verify(message, bytes.fromhex(auth_sig)) # raises an error if unequal



@app.route('/', methods=["POST"])
def index():
    request = app.current_request

    try:
        verify_signature(request)
    except:
        raise BadRequestError("Signature can't be verified")

    # Handle PING payload
    if request.json_body["type"] == 1:
        return {"type": 1}

    return {
        "type": 4,
        "data": {
            "tts": False,
            "content": "BEEP BOOP",
            "embeds": [],
            "allowed_mentions": []
        }
    }
