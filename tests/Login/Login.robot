*** Settings ***
Library    	Selenium2Library
Library    	PageObjectLibrary
Library     String
Library     Collections
Library     LoginPage
Library     Posters
Library     DateTime
Variables   gconf.py
Resource    common.robot


*** Testcases ***

Login: All valid field
    Login To System
    wait for posters appear


