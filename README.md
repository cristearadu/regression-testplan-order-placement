# regression-testplan-order-placement

This testing framework is used in "Specification by Example". The test steps are preferred to be written 
from a 'business' point of view. 


---
`pip install -r requirements.txt` - to install the libraries for this framework

For this project you need to install Gauge, create a Gauge_Home folder and add 'GAUGE_HOME' sys environment in 
system variables. Install html-report, python and screenshot using `gauge install {package_name}`. Test using 
`gauge --version` command to verify the installed plugins on your device.
```commandline
PS E:\Python\bitedender-interviu> gauge --version
Gauge version: 1.4.3
Commit Hash: f98dd40

Plugins
-------
html-report (4.1.4)
jira (0.4.2)
python (0.3.17)
screenshot (0.1.0)
```

---
A few words about Gauge
---
By using Gauge framework it becomes easier and cleaner to write test scenarios. Inside `.specs\` folder you can find 
two types of files:
1. `file_name.spec`= defines the test plan. Inside this file you can find three types of symbols:
`#`, `##`, and `*`
    <dl>
      <dt>Symbol #</dt>
      <dd>This symbol is used to write the test plan name.</dd>
      <dt>Symbol ##</dt>
      <dd>This symbol is used to write the name of the test.</dd>
     <dt>Symbol *</dt>
      <dd>This symbol is used to write a test step.</dd>
    </dl>
   
2. `file_name.cpt` = defines the "concepts" steps for tests, meaning that you can define repetitive steps here. 
 The three symbols are present here as well, only they have different meanings. 
    <dl>
      <dt>Symbol #</dt>
      <dd>This symbol is used to write name of the concept. It can be called from inside a spec file.</dd>
     <dt>Symbol *</dt>
      <dd>This symbol is used to write a test step.</dd>
    </dl>

**After defining each step and keep the functions simple, it becomes easier to refactor, to write new test cases. And I 
believe the most important aspect is that anyone with no coding knowledge can run and create tests  using this framework.**


---
How to run the project
---
TODO