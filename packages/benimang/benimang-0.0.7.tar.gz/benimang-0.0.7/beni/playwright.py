from playwright.sync_api import sync_playwright


def playwright_open(*, storage_state: str = ''):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    context = browser.new_context(storage_state=storage_state)
    page = context.new_page()
    return page
