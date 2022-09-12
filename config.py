import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "15430744"))
    API_HASH = os.environ.get("API_HASH", "5723974576:AAFsxorOuj2iwEqgwA-UuBwyjBmGJK-jTFk")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5723974576:AAFsxorOuj2iwEqgwA-UuBwyjBmGJK-jTFk") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "761686219")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://eva:eva@cluster0.wn73m.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'workflow')
    SESSION = os.environ.get("SESSION", "BQBk-G3hHTDytHtDroeAAcU20XIrVhh0BV3iuKYpidM2JbMGNTWc8qLl0xXa6fzdfYdYlBYAaDZ0SFVJkb_Uv7vf7qiHUXmJiAtrT5Kc3WDQrN3x-qfruIb6BYTW7E2q9U7S7uSBKfbVFqV20u1qTpoD3mAU8dg_TWX7GsraAJVY30Pe70AN-NkDw9yBr8yax06EQPv80tjTNazZgEb-inHPCkcl_WuGnDD8dCRVto7fhyh-HrMLJFNpk9jSKwUYlr3wZgiJzB07XhNE1U2jEtvUjm1CZf-QCD1L2lyYgZr-mlLg5bcRUKqXfeXxlZ-9ErpTrgdM9uDo0SdyLQFKpLWHUZ27_AA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001795586205"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
