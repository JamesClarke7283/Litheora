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

## 3: Manage and View User Attributes
**As a** Website Author

**I want** To be able to view and edit user attributes

**So that** I can manage user accounts

## Acceptance Criteria

### Scenario 1: View User Attributes
**Given** I am logged in
  
**And** I click on the view user button
  
**When** I view the user attributes

**Then** I should see the user attributes

### Scenario 2: Edit User Attributes
**Given** I am logged in

**And** I click on the edit user button

**When** I change the user attributes

**Then** The user attributes should be updated

---

## 4: Manage and View Site Attributes

**As a** Website Author

**I want** To be able to view and edit site attributes

**So that** I can manage the site

## Acceptance Criteria

### Scenario 1: View Site Attributes

**Given** I am logged in

**And** I click on the view site button

**When** I view the site attributes

**Then** I should see the site attributes

### Scenario 2: Edit Site Attributes

**Given** I am logged in

**And** I click on the edit site button

**When** I change the site attributes

**Then** The site attributes should be updated

---

## 5: Manage and View Block Attributes

**As a** Website Author

**I want** To be able to view and edit block attributes

**So that** I can manage the site

## Acceptance Criteria

### Scenario 1: View Block Attributes

**Given** I am logged in

**And** I click on the view block button

**When** I view the block attributes

**Then** I should see the block attributes

### Scenario 2: Edit Block Attributes

**Given** I am logged in

**And** I click on the edit block button

**When** I change the block attributes

**Then** The block attributes should be updated

---

## 6: Manage and View Block Type's

**As a** Experianced Website Author

**I want** To be able to view and edit block type's

**So that** I can manage the site

## Acceptance Criteria

### Scenario 1: View Block Type's

**Given** I am logged in

**And** I click on the view block type button

**When** I view the block type

**Then** I should see the block type

### Scenario 2: Edit Block Type's

**Given** I am logged in

**And** I click on the edit block type button

**When** I change the block type

**Then** The block type should be updated

### Scenario 3: Create Block Type

**Given** I am logged in

**And** I click on the create block type button

**When** I create a block type

**Then** The block type should be created

### Scenario 4: Delete Block Type

**Given** I am logged in

**And** I click on the delete block type button

**When** I confirm the deletion

**Then** The block type should be deleted

---

## 7: Install and Manage Site

**As a** Website Author

**I want** To be able to install and manage the site

**So that** I can create or manage the site

## Acceptance Criteria

### Scenario 1: Install Site

**Given** I am at the install page

**And** I enter the site name

**And** I enter the database Type and details.

**And** I enter the admin username and password

**When** I click the install button

**Then** The site should be installed

### Scenario 2: Manage Site

**Given** I am logged in

**And** I click on the site settings button

**When** I change the site settings

**Then** The site settings should be updated

---

## 8: Create and Manage Blocks

**As a** Website Author

**I want** To be able to create and manage blocks

**So that** I can manage the site

## Acceptance Criteria

### Scenario 1: Create Block

**Given** I am logged in

**And** I click on the create block button

**And** I pick a block type

**And** I enter the block attributes

**When** I click the create block button

**Then** The block should be created

### Scenario 2: Manage Block

**Given** I am logged in

**And** I click on the edit block button on the block

**When** I change the block attributes

**Then** The block should be updated

### Scenario 3: Delete Block

**Given** I am logged in

**And** I click on the delete block button

**When** I confirm the deletion

**Then** The block should be deleted

---

## 9: Uploading And Managing Assets(Images, CSS, JS)

**As a** Website Author

**I want** To be able to upload and manage assets

**So that** I can manage the site

## Acceptance Criteria

### Scenario 1: Upload Asset

**Given** I am logged in

**And** I click on the upload asset button in the asset library page or block editor

**And** I pick a file

**When** I click the upload button

**Then** The asset should be uploaded

### Scenario 2: Manage Asset

**Given** I am logged in

**And** I click on the edit asset button on the asset

**When** I pick a file to replace the asset

**Then** The asset should be updated

### Scenario 3: Delete Asset

**Given** I am logged in

**And** I click on the delete asset button

**When** I confirm the deletion

**Then** The asset should be deleted

---

## 10: Create and Manage Tiles:

**As a** Plugin Developer or Block Author

**I want** To be able to create and manage tiles

**So that** I can improve the CMS experiance.

## Acceptance Criteria

### Scenario 1: Create Tile

**Given** I am logged in

**And** I click on the create tile button

**And** I pick a tile image.

**And** I enter the tile name and description

**When** I click the create tile button

**Then** The tile should be created

### Scenario 2: Manage Tile

**Given** I am logged in

**And** I click on the edit tile button on the tile

**When** I change the tile attributes

**Then** The tile should be updated

### Scenario 3: Delete Tile

**Given** I am logged in

**And** I click on the delete tile button

**When** I confirm the deletion

**Then** The tile should be deleted

---







