*** Settings ***
Library  FakerLibrary  WITH NAME  faker
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.2 seconds
${HOME URL}  http://${SERVER}/
# ${RESULTS URL}  http://${SERVER}/results?tip_name=${search}&action=Hae

*** Keywords ***
Open And Configure Browser
    ${word}=  faker.Word
    ${number}=  faker.Random Int
    Set suite variable  ${word}
    Set suite variable  ${number}
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Kirjaudu

Go To Main Page
    Go To  ${HOME URL}
