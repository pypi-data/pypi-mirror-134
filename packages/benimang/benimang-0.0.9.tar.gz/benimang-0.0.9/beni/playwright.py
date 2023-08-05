from typing import cast

import nest_asyncio

from playwright.sync_api import sync_playwright


def playwright_open(*, url: str = '', storage_state: str | None = None):
    nest_asyncio.apply()
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    context = browser.new_context(storage_state=cast(str, storage_state))
    page = context.new_page()
    if url:
        page.goto(url)
    return page
