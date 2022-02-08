  
# Eze Report Results


## Summary  ![tools](https://img.shields.io/static/v1?style=plastic&label=Tools&message=5&color=blue)
---


![critical](https://img.shields.io/static/v1?style=plastic&label=critical&message=0&color=red)
![high](https://img.shields.io/static/v1?style=plastic&label=high&message=0&color=orange)
![medium](https://img.shields.io/static/v1?style=plastic&label=medium&message=0&color=yellow)
![low](https://img.shields.io/static/v1?style=plastic&label=low&message=0&color=lightgrey)
            
<b>Branch tested: </b>main

<b>Tools executed: </b>

* python-piprot (SCA)
            
* python-bandit (SAST)
            
* python-safety (SAST)
            
* python-cyclonedx (SBOM)
            
* trufflehog (SECRET)
            

Errors
=================================

    [python-safety] Errors
    =================================
        Eze cannot access 'reports/safety-report.json', File could not be found

    [python-cyclonedx] Errors
    =================================
        Eze cannot access 'reports/python-cyclonedx-bom.json', File could not be found

## Warnings
---

    [python-piprot] Warnings
    =================================
    usage: piprot [-h] [-v] [-l] [-x] [-q] [-o] [-g GITHUB] [-b BRANCH] [-t TOKEN]
                  [-p PATH] [-d DELAY] [-u URL]
                  file [file ...]
    piprot: error: argument file: can't open 'requirements.txt': [Errno 2] No such file or directory: 'requirements.txt'
    

    [python-bandit] Warnings
    =================================
    {"filename": "app", "reason": "No such file or directory"}

