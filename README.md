# general
Generic / random Odoo apps not related to one feature or app:
- [by_pass_restrictive_test] (#by_pass_restrictive_test): allows you to configure which automated Odoo tests you want to be skipped.

## by_pass_restrictive_test
In some cases there are Odoo tests that you want to skip as they are too restrictive and you change the results you get back on purpose.
In these cases it is handy to be able to bypass the test and then write your own tests to check your own behaviour.
This app support it in two ways:
1. Through the code by setting the `ir.config_parameter` named `set_by_pass_restrictive_test` to `True` (see `data/bypass_meta_data.xml`) and by passing a list of test names you'd like to skip in the `ir.config_parameter` named `by_pass_restrictive_test_names`
2. Through the frontend, under General Settings, by toggling the flag `By pass restrictive test` on and providing the names of tests to skip:
![image](https://user-images.githubusercontent.com/6352350/184090883-5eae7684-ca23-4e01-96c3-2377fdf4718f.png) <br/>
Tip: this allows skipping multiple tests, just place a comma between every test name.
