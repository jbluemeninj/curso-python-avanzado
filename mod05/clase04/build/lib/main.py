import logging

from prefect import flow
from tasks.get_offers import (
    get_offers
)

from tasks.save_offers import (
    save_offers
)

SKILL = 'python'
log = logging.getLogger()

@flow(name="LINKEDIN SCRAPPER")
def main_flow():
    log.info(f"PROCESO DE EXTRACCION")
    offers = get_offers(SKILL)
    save_offers(offers)

if __name__ == "__main__":
    main_flow()