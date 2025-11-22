Feature: Para Bank Home Page Functionality

#Scenario 1: Verify Para Bank homepage elements
  Scenario: Validate Para Bank homepage loads correctly
    Given   I open the Para Bank homepage
    Then    I should see the title as "ParaBank | Welcome | Online Banking"
    # Then    I should see the top panel
    # And     Top panel should contain Para Bank logo
    # And     I should see the header panel
    # And     Header panel should contain "Welcome to the ParaBank!"
    # And     Header panel shouuld contain Left Menu and Buttons
    # And     there is no console errors on the page