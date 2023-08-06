*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  ../lib/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote
Library  DebugLibrary

Test Setup  Prepare test browser
Test Teardown  Close all browsers

*** Test Cases ***

Member can change the title of a document
    Given I am in a workspace as a workspace member
    And I browse to a document
    And I change the title
    And I view the document
    The document has the new title

Member can change the description of a document
    Given I am in a workspace as a workspace member
    And I browse to a document
    And I change the description
    And I view the document
    Then the document has the new description

Member can tag a document
    Given I am in a workspace as a workspace member
    And I browse to a document
    And I tag the description
    And I view the document
    Then the document has the new tag

Member can change the title of an image
    Given I am in a workspace as a workspace member
    And I browse to an image
    And I change the title
    And I view the image
    Then the document has the new title

Member can change the description of an image
    Given I am in a workspace as a workspace member
    And I browse to an image
    And I change the description
    And I view the image
    Then the document has the new description

Member can tag an image
    Given I am in a workspace as a workspace member
    And I browse to an image
    And I tag the description
    And I view the image
    Then the document has the new tag

Member can change the title of a file
    Given I am in a workspace as a workspace member
    And I browse to a file
    And I change the title
    And I view the file
    Then the document has the new title

Member can change the description of a file
    Given I am in a workspace as a workspace member
    And I browse to a file
    And I change the description
    And I view the file
    Then the document has the new description

Member can tag a file
    Given I am in a workspace as a workspace member
    And I browse to a file
    And I tag the description
    And I view the file
    Then the document has the new tag

# Member can change the title of a folder
#     Given I am in a workspace as a workspace member
#     And I view the folder
#     And I change the title
#     And I view the folder
#     Then the document has the new title

# Member can change the description of a folder
#     Given I am in a workspace as a workspace member
#     And I view the folder
#     And I change the description
#     And I view the folder
#     Then the document has the new description

# Member can tag a folder
#     Given I am in a workspace as a workspace member
#     And I view the folder
#     And I tag the description
#     And I view the folder
#     Then the document has the new tag

*** Keywords ***
I browse to a workspace
    Go To  ${PLONE_URL}/workspaces/open-market-committee
    Click Link  link=Documents
    Click Link  link=Manage Information

I browse to a document
    I browse to a workspace
    Wait Until Page Contains Element  xpath=//a[contains(@href, 'repurchase-agreements')]
    Click Link  xpath=//a[contains(@href, 'repurchase-agreements')]

I view the document
    Go To  ${PLONE_URL}/workspaces/open-market-committee/manage-information/repurchase-agreements

I browse to an image
    I browse to a workspace
    Wait Until Page Contains Element  xpath=//a[contains(@href, 'budget-proposal')]
    Click Link  xpath=//a[contains(@href, 'budget-proposal')]

I view the image
    Go To  ${PLONE_URL}/workspaces/open-market-committee/manage-information/budget-proposal/view

I browse to a file
    I browse to a workspace
    Wait Until Page Contains Element  xpath=//a[contains(@href, 'minutes')]
    Click Link  xpath=//a[contains(@href, 'minutes/view')]

I view the file
    Go To  ${PLONE_URL}/workspaces/open-market-committee/manage-information/minutes/view

I view the folder
    Go To  ${PLONE_URL}/workspaces/open-market-committee/manage-information/projection-materials/view

I change the title
    Comment  Toggle the metadata to give the JavaScript time to load
    Wait Until Page Contains  Toggle extra metadata
    Click Link  link=Toggle extra metadata
    Click Link  link=Toggle extra metadata
    Input Text  title  New title ♥
    Wait Until Page Contains  New title ♥
    Click Button  Save
    Wait Until Page Contains  Your changes have been saved

The document has the new title
    Textfield Should Contain  title  New title ♥

I change the description
    Wait Until Page Contains  Toggle extra metadata
    Click Link  link=Toggle extra metadata
    Input Text  xpath=//textarea[@name='description']  New description ☀
    Click Button  Save
    Wait Until Page Contains  Your changes have been saved

The document has the new description
    Page Should Contain  New description ☀

I tag the description
    Wait Until Page Contains  Toggle extra metadata
    Click Link  link=Toggle extra metadata
    Input Text  id=s2id_autogen2  NewTag☃,
    Click Button  Save
    Wait Until Page Contains  Your changes have been saved

The document has the new tag
    Click Link  link=Toggle extra metadata
    Page Should Contain  NewTag☃
