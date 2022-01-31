# Eze Docker Github Action
This is a Github Action for executing [Eze](https://hub.docker.com/r/riversafe/eze-cli) security tool in your repository, to identify security vulnerabilities. 

The test will generate a SARIF output and can be viewed in the `Security tab`.

You can use more advanced features in the Eze Console, a web interface we have designed to monitor the security of all your repos.


## Usage
To use the action, you will have to set the job inside the workflow, you can get a template and replace as needed.

And you will need to set a config file for Eze to run based on the language your code is in and the security scans you want to perform.

There are 2 possible outcomes: sarif and markdown, and an individual template for each of them. 