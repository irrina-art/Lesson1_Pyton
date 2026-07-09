from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "MjZiZDEyMGItZDc1NS00MDEzLWE2M2UtYTQ5NWFmZjk2ZWRl",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/zina")
    url_user1 = driver.current_url
    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie({
        "name": "SESSION",
        "value": "YzJlYjU5OTgtNDY0My00OGUwLTllNTMtNDNiNjViNTgyMmRj",
        "domain": "gitflic.ru"
         })
    driver.refresh()

    driver.get("https://gitflic.ru/user/melissa")
    url_user2 = driver.current_url
    assert url_user1 != url_user2
    driver.quit()
