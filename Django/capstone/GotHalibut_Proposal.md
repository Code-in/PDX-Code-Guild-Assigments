# GotHalibut Support Site - Capstone Proposal

## What is GotHalibut Support Site ?
I've published an iPhone app called GotHalibut and am starting to build a customer base. To take my app to the next level I need a support site which will provide documentation, customer support, privacy policy and a admin tool for managing the data from support requests, etc... 

## Project Overview
The key apps will revolve around documentation, customer support, privacy policy. The documentation will explain how to utilize the GotHalibut App, customer support which will have a form page for submitting support questions and customer data privacy policy which is required for iPhone apps submitted to the AppStore. Depending on time I would also like to include an admin page where the admin can manage the support submission with a dashboard like page.

## Functionality
- Allow GotHalibut customers to submit support request on the website (restful support so eventually I can enable support directly in the iOS app).
- Allow iPhone users to review privacy policy (restful support so eventually I can enable support directly in the iOS app).
- Allow users to access GotHalibut documentation on how to get the most out of the GotHalibut app.
- A dashboard which allows the admin to manage customer support requests. 

## Data Model
- Support ticket
    - Submission date 
    - User's email for support response
    - Message body asking for details on the support ticket
    - iPhone model
    - iOS version
    - Foreign key to connect additional responses linkages

- Response ticket
    - Response to support ticket
    - Response date
    - Foreign key to Support ticket


## Schedule
### Week 1
- [X] Create a Git project for this work
- [X] Create the 3 app starter stubs
- [X] Created importDB command for my model
- [X] Created a cleanDB command for when I need to migrate in new changes
- [X] Define the model for the support app
    - [X] Implement the Support model 
    - [X] Create the support page
    - [X] Uploading Images
- [x] Define Response ticket model
    - [x] Implement the Response model 
    - [0] Create issue request dashboard page
    - [0] Create issue response page which emails them back from a form

- [ ] Need to add responsed and requested support date in the data


### Week 2
- [X] Create Vue app for viewing GotHalibut documentation
    - [O] Create GotHalibut documentation using html/css
    - [O] Build a restful call functionality for the View app to pull the documentation from the back-end

### Week 3 (functionally complete capstone by the end of week 3)
- [ ] Create the policy page which is required by Apple for AppStore Apps
- [X] Create a management dashboard where I can link histories from tickets and Reponses if a support request spans over multiple support requests and responses.
- [X] Have management dashboard show pending support requests, resolved support requests, create filtering to help find linkages.

### Week 4
- [ ] Deploy to Heroku 
- [ ] Beautify the pages
- [ ] Test and verify that everything is working on Production
