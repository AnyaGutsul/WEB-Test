# Testing website with Selenium

1. Create Gitlab public project
·         Acquire shared docker runner (i.e. use one of the default publics GitLab allows)

·         Create .gitlab-ci.yml file in project

·         Make sure CI/CD pipeline works

2. Create PyTest test and run it
·         Use web resource https://the-internet.herokuapp.com/context_menu .

·         Test should PASS if the string “ Right-click in the box below to see one called 'the-internet' “ found on page.

·         Another Test should FAIL if string “Alibaba” is not found on the same page.

·         Show tests run in a pipeline in CI/CD of the Gitlab project.


