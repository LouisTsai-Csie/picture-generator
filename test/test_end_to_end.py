from playwright.sync_api import sync_playwright

def test_picture_generator_correct():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto('localhost:5000')

        page.fill('#width', '800')
        page.fill('#height', '600')

        page.click('input[type="submit"]')

        img_element = page.query_selector('img')
        assert img_element is not None

        context.close()
        browser.close()
    return

def test_picture_generator_invalid_input_height():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto('localhost:5000')

        page.fill('#width', '400')
        page.fill('#height', '')

        page.click('input[type="submit"]')

        p_element = page.query_selector('p')
        assert p_element is not None
        assert p_element.inner_text() == 'Invalid Input'

        context.close()
        browser.close()
    return

def test_picture_generator_invalid_input_width():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto('localhost:5000')

        page.fill('#width', '')
        page.fill('#height', '600')

        page.click('input[type="submit"]')

        p_element = page.query_selector('p')
        assert p_element is not None
        assert p_element.inner_text() == 'Invalid Input'

        context.close()
        browser.close()
    return
