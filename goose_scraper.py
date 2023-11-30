import re

from goose3 import Goose
from loguru import logger

from constants import UNWANTED_SPACES_PATTERN


class GooseScraper:
    """
    Scraper using goose
    """

    def scrape_get_text_from_page(self, url):
        g = Goose()
        g.config.browser_user_agent = "Mozilla 5.0"
        logger.info(f"Sending request to page '{url}'")
        article = g.extract(url=url)
        logger.info(f"Extracting the response")
        g.close()
        return self._clean_data(article.cleaned_text)

    def _clean_data(self, text):
        logger.info(f"Cleaning extracted data")
        return re.sub(UNWANTED_SPACES_PATTERN, " ", text).lstrip().rstrip()
