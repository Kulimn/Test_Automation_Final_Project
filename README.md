## **Full Stack Automation Final Project**
[Short Video - Demonstration](https://drive.google.com/file/d/1qWVOhaOUcezKeUcokyzht-RtT9yvo3Il/view?usp=sharing&t=12)
### **_This project created to demonstrate my knowledge and skills in Automation Testing._**
***
### _About_
The project demonstrates a smart automation infrastructure. It is built in hierarchy order of modules. The modules contain number of classes with methods.
There are main/common/helpers/actions/page_object modules.
In this way, the tests can be created in very simple way with a minimum lines of code.
Also the infrastructure allows to work with differend kinds of applications.
**Big advantage of the infrastructure is that it can be easy maintained!**

### _Project Overview_

The project is an example of infrastructure for automation testing of different kinds of applications:
* Web based application
* Mobile application
* Web API

### **_Infrastructure project includes using of:_**
* Page Object Design Pattern
* Project Layers(Extensions/Work Flows/Test Cases...)
* Support of Different Clients/Browsers
* Failure Mechanism
* Common Functionality
* External Files Support
* Reporting System (including screenshots) 

***

### _List of applications were used in this project:_
* Swag Lub webpage - Web based application
* Mortgage calculator - Mobile application
* Grafana API - Web API

### _Tools & Frameworks used in the project:_
* PyTest - Testing Framework
* WebDriver - To control browsers for automated testing
* Selenium - For web application testing automation
* Appium - For mobile application testing automation
* REST API Requests - for API testing
* [Jenkins](https://www.jenkins.io/)- for tests execution
* [Allure](https://allurereport.org/) Reports - as the main reporting system

### Tests Execution:
> Each of the applications has a few tests for demonstration purpose.
These tests can be developed in a very simple way, due to a lot of work with the infrastructure.
[[Test Cases]](https://github.com/Kulimn/Test_Automation_Final_Project/tree/main/test_cases)

### _Known Issues:_
Sometimes can be conflicts with some dependencies the applications are using.
Hence, the project is for DEMO purpose only. In production it should be divided into several projects.
