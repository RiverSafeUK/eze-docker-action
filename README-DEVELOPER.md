
# Eze Github Action (Developers documentation)

## Process
---

Eze Action runs a `Dockerfile` that is based on the `riversafe/eze-cli` docker image and runs a python file `entrypoint.py` to modify the config file (named as .ezerc.toml) that Eze test will use to export a markdown report or sarif report, based on the user input.

Also if you want to test any change inside a workflow, you can use the sample workflows in `.github/workflows`. 

- Note: When you want to use this action in another repo and before publish the latest change, you can refer with the name of the branch (ex. *RiverSafeUK/eze-docker-action@develop*) and test:

    ```
    - name: Testing with Eze - markdown
    uses: <user>/<repo_name>@<branch_name>
    ```

Once testing is done you can publish your action, first merge the changes into main branch and create a [release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) with tag.

## Contribute
---
To contribute in adding more security tools to our EZE-CLI project, you can go to the following links: 
- https://github.com/RiverSafeUK/eze-cli
- https://pypi.org/project/eze-cli/
- SARIF format: https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning#result-object
- Publish action: https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace


## License
You can review details in []