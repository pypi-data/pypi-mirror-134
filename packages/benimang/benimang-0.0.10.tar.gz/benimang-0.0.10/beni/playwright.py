from typing import cast

from playwright.sync_api import BrowserContext, sync_playwright

_test_context: BrowserContext | None = None


def playwright_test(*, url: str = '', storage_state: str | None = None):
    global _test_context
    if not _test_context:
        import nest_asyncio
        nest_asyncio.apply()
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False, channel='chrome')
        _test_context = browser.new_context(storage_state=cast(str, storage_state))
    page = _test_context.new_page()
    if url:
        page.goto(url)
    return page
