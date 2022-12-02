*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${FORM URL}  http://${SERVER}/form
${ALL URL}  http://${SERVER}/all
${BIBTEX URL}  http://${SERVER}/bibtex

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Etusivu

Form Book Page Should Be Open
    Title Should Be  Lisää Viite Book

All Page Should Be Open
    Title Should Be  Kaikki Viitteet

Bibtex Page Should Be Open
    Title Should Be  Bibtex

Go To Bibtex Page
    Go To  ${BIBTEX URL}

Go To Home Page
    Go To  ${HOME URL}

Go To Form Page
    Go To  ${FORM URL}

Go To All Page
    Go To  ${ALL URL}

Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id}  ${text}

Submit Form
    Click Button  Luo viite