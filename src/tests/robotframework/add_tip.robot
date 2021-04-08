*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Variables ***
${tip_author}  Author
${tip_url}  www.test.com

*** Test Cases ***
Input New Tip
    Set Tip Author
    Set Tip URL
    Submit Tip

Confirm New Tip
    Search Author
    Submit Search
    ${response}    Get Text    result
    Should Be Equal As Strings  ${response}  Kirjoittaja: ${tip_author}_${number}, URL: ${tip_url}/${word}

*** Keywords ***
Set Tip Author
    Input Text  tip_name  ${tip_author}_${number}

Set Tip URL
    Input Text  tip_url  ${tip_url}/${word}

Submit Tip
    Click Button  Lisää

Search Author
    Input Text  tip_search  ${tip_author}_${number}

Submit Search
    Click Button  Hae

Submit Tip Failed
    Title Should Be  Virhe
