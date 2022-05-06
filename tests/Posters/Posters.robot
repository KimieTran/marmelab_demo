*** Settings ***
Library    	Selenium2Library
Library    	PageObjectLibrary
Library     String
Library     Collections
Library     Posters
Library     DateTime
Variables   gconf.py
Resource    common.robot


*** Testcases ***

Posters: select 3rd poster
    [Arguments]        ${3rd_poster}
    Login To System
    Go to Posters
    Enter 3rd poster    ${3rd_poster}
    wait for 3rd poster appears

