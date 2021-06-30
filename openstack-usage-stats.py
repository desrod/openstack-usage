#!/usr/bin/env python3

import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

horizon_url = "http://192.168.103.211/horizon"
download_dir = "/tmp/"

# TODO: Parse ~/.config/openstack/clouds.yaml for auth
# Statically define credentials here... (not secure)
horizon_username = "admin"
horizon_password = "openstack"
horizon_domain = "admin_domain"

# or, prompt for input (more secure)
# horizon_username = input("Enter your OpenStack username: ")
# horizon_password = getpass(
#    prompt=f"Enter your OpenStack password for {horizon_username}: ", stream=None
# )
# horizon_domain = input("Enter the domain you wish to log into: ")

options = Options()
options.add_argument("--headless")
options.add_experimental_option(
    "prefs",
    {
        f"download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)
driver = webdriver.Chrome(options=options)

print(f"Logging into Horizon as {horizon_username}...", end="", flush=True)
driver.get(f"{horizon_url}/auth/login/")
driver.find_element(By.ID, "id_domain").send_keys(horizon_domain)
driver.find_element(By.ID, "id_username").send_keys(horizon_username)
driver.find_element(By.ID, "id_password").send_keys(horizon_password)
driver.find_element(By.CSS_SELECTOR, "#loginBtn > span").click()
print(f" downloading usage.csv {download_dir}", flush=True)
driver.find_element(By.ID, "project_usage__action_csv_summary").click()
time.sleep(0.5)
driver.quit()

with open("usage.csv", "r") as usage:
    print(usage.read())
