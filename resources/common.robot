*** Settings ***
Library    	            Selenium2Library
Library    	            PageObjectLibrary
Library    	            page_object/LoginPage.py
Library                 page_object/Poster.py
Library                 page_object/AddCustomer.py
Variables               gconf.py

*** Keywords ***
Open chrome
    [Arguments]     ${root}
    ${chrome options} =     Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Run keyword If  "${G_headless}" == "true"  Run keywords
    ...  Call Method    ${chrome options}   add_argument    headless
    ...  AND  Call Method    ${chrome options}   add_argument    disable-gpu
    Call Method    ${chrome options}    add_argument    disable-infobars
    Create Webdriver    Chrome    chrome_options=${chrome options}
    Run keyword If  "${G_headless}" == "true"  Set Window Size  1920  1080
    ...  ELSE
    ...  Maximize browser window
    Go to   ${root}

Logout
    Delete all cookies

Login To System
    [Arguments]    ${user_name}    ${password}
    Go To Dynamic Page    LoginPage
	Enter username 	${user_name}
	Enter password 	${password}
	Click signin button

Go to Posters
    Go To Dynamic Page      Posters
    wait for posters appear
    Click the search box

Go to Add Customer
    Go to Dynamic Page      AddCustomer
    wait for create button appears
    Click create button