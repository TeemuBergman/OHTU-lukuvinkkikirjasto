*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Variables ***
${tip_author}  Author
${tip_title}  Teoksen nimi
${tip_url}  www.test.com
${email}  testisapo@testi.fi
${name}  Testi Tunnus
${password}  salasana

*** Test Cases ***

Go To Register
    Go To Register
    Title Should Be  Rekisteröidy

Register And Login New User
    Go To Register
    Title Should Be  Rekisteröidy
    Set User Email
    Set User Name
    Set User Password
    Submit Registration 
    Title Should Be  Kirjaudu

    Set User Email
    Set User Password
    Submit Login
    Title Should Be  Lukuvinkkejä

Input New Tip
    Set User Email
    Set User Password
    Submit Login
    Title Should Be  Lukuvinkkejä
    Set Tip Author
    Set Tip Title
    Set Tip URL
    Submit Tip

Confirm New Tip
    Set User Email
    Set User Password
    Submit Login
    Title Should Be  Lukuvinkkejä
    Search Author
    Submit Search
    ${response}    Get Text    result
    Should Be Equal As Strings  ${response}  Kirjoittaja: ${tip_author}_${number}, Teoksen nimi: ${tip_title}_${number}, URL: ${tip_url}/${word}

Logout
    Set User Email
    Set User Password
    Submit Login
    Title Should Be  Lukuvinkkejä
    Go To Logout
    Title Should Be  Kirjaudu

Delete Tip
    Set User Email
    Set User Password
    Submit Login
    Title Should Be  Lukuvinkkejä
    Delete Tip
    Title Should Be  Delete

*** Keywords ***
Set Tip Author
    Input Text  tip_name  ${tip_author}_${number}

Set Tip Title
    Input Text  tip_title  ${tip_title}_${number}

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

Go To Register
    Click Link  link:rekisteröitymään

Set User Email
    Input Text  email  ${number}_${email}

Set User Name
    Input Text  name  ${name}_${number}

Set User Password
    Input Text  password  ${password}${number}

Submit Registration
    Click Button  Rekisteröidy

Submit Login
    Click Button  Kirjaudu

Go To Logout
    Click Link  link:kirjaudu ulos

Delete Tip
    Click Button  Poista

