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

Register And Automatic Login
    Go To Register
    Title Should Be  Rekisteröidy
    Set User Email
    Set User Name
    Set User Password
    Submit Registration
    Title Should Be  Lukuvinkit
    Go to personal page
    Title Should Be  Omat lukuvinkit

Input New Tip
    Go to personal page
    Title Should Be  Omat lukuvinkit
    Set Tip Author
    Set Tip Title
    Set Tip URL
    Submit Tip

Confirm New Tip
    Go to personal page
    Title Should Be  Omat lukuvinkit
    Search Author
    Submit Search
    ${response}    Get Text    result
    ${compare}    Set Variable    ${tip_author}_${number}\n${tip_title}_${number}\n${tip_url}/${word}
    Should Be Equal As Strings  ${response}  ${compare}
Mark Tip As Read
    Go to personal page
    Title Should Be  Omat lukuvinkit
    Submit Read
    ${read_tips}    Get Text    read_tips
    Should Be Equal As Strings  ${read_tips}  ${tip_title}_${number}
    Submit Read
    ${notread_tips}    Get Text    notread_tips
    Should Be Equal As Strings  ${notread_tips}  ${tip_title}_${number}

Go To Main Page And Back To Personal Page
    Go to personal page
    Title Should Be  Omat lukuvinkit
    Click Frontpage
    Title Should Be  Lukuvinkit
    Go to personal page
    Title Should Be  Omat lukuvinkit

Delete Tip
    Go to personal page
    Title Should Be  Omat lukuvinkit
    Delete Tip
    Handle Alert
    Title Should Be  Omat lukuvinkit

 

Logout
    Go To Logout
    Title Should Be  Lukuvinkit
    Wait Until Page Contains  Kirjaudu lukuvinkkisovellukseen



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

Go to personal page
    Click Link  link:Oma sivu

Go To Logout
    Click Link  link:Kirjaudu ulos

Delete Tip
    Click Button  Poista

Submit Read
    Click Button  Luettu / Ei luettu

Click Frontpage
    Click Link  link:Etusivu
