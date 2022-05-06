*** Settings ***
Library    	Selenium2Library
Library    	PageObjectLibrary
Library     String
Library     Collections
Library     LoginPage
Library     Posters
Library     AddCustomer
LIbrary     CustomerInfo
Library     DateTime
Variables   gconf.py
Resource    common.robot

Suite Setup    	 Suite Setup For Add Customer
Suite Teardown    Suite Teardown For Add Customer
Test Teardown    Run Keyword If Test Failed    Capture Page Screenshot

*** Testcases ***

Create a new customer: all valid values
    [Arguments]         ${G_first_name}   ${G_last_name}    ${G_email}
                        ${G_birthday} ${G_Address}  ${G_City} ${G_State}
                        ${G_zipcode} ${G_Password}  ${G_Confirm_pwd}
    Go to Add Customer
    Wait For Save Button Appears
    Enter first name                ${G_first_name}
    Enter last name                 ${G_last_name}
    Enter email                     ${G_email}
    Enter birthday                  ${G_birthday}
    Enter address                   ${G_Address}
    Enter city                      ${G_City}
    Enter state                     ${G_State}
    Enter zipcode                   ${G_zipcode}
    Enter new customer password     ${G_Password}
    Enter Confirm_prd               ${G_Confirm_pwd}
    Click Save Button
    wait for customer info first name contains text     ${G_first_name}
    wait for customer info last name contains text      ${G_last_name}
    wait for customer info email contains text          ${G_email}
    wait for customer info birthday contains text       ${G_birthday}
    wait for customer info address contains text        ${G_Address}
    wait for customer info city contains text           ${G_City}
    wait for customer info state contains text          ${G_State}
    wait for customer info zipcode contains text        ${G_zipcode}
 *** Keywords ***
 Suite Setup For Add Customer
     Open chrome     ${G_root_url}
     Login To  System    ${user_name}    ${password}

 Suite Teardown For Add Customer
     Logout
     Close all browsers



