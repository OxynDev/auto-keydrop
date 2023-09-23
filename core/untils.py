import browser_cookie3



def get_cookie_browser(browser_name: str = 'chrome'):

    domain = 'key-drop.com'
    all_cookies = None
    if browser_name == "chrome":
        all_cookies = list(browser_cookie3.chrome())
    elif browser_name == "chromium":
         all_cookies = list(browser_cookie3.chromium())
    elif browser_name == "firefox":
         all_cookies = list(browser_cookie3.firefox())
    elif browser_name == "opera":
         all_cookies = list(browser_cookie3.opera())
    elif browser_name == "opera_gx":
         all_cookies = list(browser_cookie3.opera_gx())
    elif browser_name == "edge":
         all_cookies = list(browser_cookie3.edge())

    keydrop_cookies ={}
    for cookie in all_cookies:
        if (domain in cookie.domain):
                keydrop_cookies[cookie.name]=cookie.value

    return keydrop_cookies



