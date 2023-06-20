# User Stories
---
## 1: User Authentication
**As a** Account Holder

**I want** to be able to login and create an account

**So that** I can access my account and create content

## Acceptance Criteria

### Scenario 1: Register
**Given** A username, email and password
  
**And** The username and email are not already in use.
  
**When** I click the register button

**Then** I should be registered
  
**And** Logged in

### Scenario 2: Login
**Given** A username and password

**And** The username and password are correct

**When** I click the login button

**Then** I should be logged in

---

## 2: Manage Pages
**As a** Website Author

**I want** To be able to create/update/delete a page.

**So that** I can add content to my website

## Acceptance Criteria

### Scenario 1: Create Page
**Given** I am logged in
  
**And** I click on the create page button
  
**When** I enter a title and URL.

**Then** A new page should be created
  
**And** I should be redirected to the new page

### Scenario 2: Edit Page Attributes
**Given** I am logged in

**And** I click on the edit page button

**When** I change the title and URL

**Then** The page should be updated

### Scenario 3: Edit page content

**Given** I am logged in

**And** I click on the edit page button

**When** I change the content

**Then** The page should be updated


### Scenario 4: Delete Page

**Given** I am logged in

**And** I click on the delete page button

**When** I confirm the deletion

**Then** The page should be deleted

---