from selenium import webdriver
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_exchange_rate(date, currency_code):
    currency_name = convert_currency_code(currency_code)
    if currency_name is None:
        print("Invalid currency code.")
        return None

    driver = webdriver.Chrome()

    try:
        # 打开中国银行外汇牌价网站
        driver.get("https://www.boc.cn/sourcedb/whpj/")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))

        time.sleep(10)

        # 日期
        date_input = driver.find_element_by_id("txtDate")
        date_input.clear()
        date_input.send_keys(date)

        # 选择货币种类
        currency_select = driver.find_element_by_id("pjname")
        currency_select.send_keys(currency_name)

        # 查询按钮
        search_button = driver.find_element_by_id("btn_query")
        search_button.click()
        time.sleep(2)

        exchange_rate = driver.find_element_by_xpath("//td[text()='现汇卖出价']/following-sibling::td[2]").text
        return exchange_rate
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        driver.quit()

def convert_currency_code(currency_code):
    currency_codes = {
        "USD": "1316",
        "EUR": "1314"
    }
    return currency_codes.get(currency_code)

def main():

    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
        return

    date = sys.argv[1]
    currency_code = sys.argv[2].upper()

    exchange_rate = get_exchange_rate(date, currency_code)
    if exchange_rate is not None:
        with open("result.txt", "w") as file:
            file.write(f"On {date}, the exchange rate for {currency_code} is {exchange_rate}.")

if __name__ == "__main__":
    main()