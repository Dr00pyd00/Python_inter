
from functools import partial

def envoyer_message(plateforme, destinataire, message):
    print(f"[{plateforme}] -> {destinataire} : {message}")



envoyer_message_slack = partial(envoyer_message, "Slack")
envoyer_message_email = partial(envoyer_message, "Email")

envoyer = partial(envoyer_message, plateforme="FB", destinataire="SASA" )

envoyer_message_email("koko","salut je test")
envoyer_message_slack("kiki","message etcetc")
envoyer(message="salut a toi")
