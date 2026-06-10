 ```diff
--- a/update_readme.py
+++ b/update_readme.py
@@ -1,6 +1,7 @@
 #!/usr/bin/env python3
 
 import re
+import os
 
 def update_readme():
     with open('README.md', 'r') as f:
@@ -12,6 +13,10 @@
     # Find the device issues section
     pattern = r'(<!-- BEGIN DEVICE ISSUES -->.*?<!-- END DEVICE ISSUES -->)'
     
+    # Check if we need to add EC testability interface documentation
+    ec_issue_link = 'https://github.com/Dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22EC%22'
+    ec_testability_link = 'https://github.com/Dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22EC%22+label%3A%22enhancement%22'
+    
     # The device issues section content
     device_issues = '''<!-- BEGIN DEVICE ISSUES -->
 ## Issues per device
@@ -24,6 +29,7 @@
 - [MSI Pro Z690-A](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22MSI%20PRO%20Z690-A%20boards%22)
 - [MSI Pro Z790-P](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22MSI%20PRO%20Z790-P%20boards%22)
 - [NovaCustom NS5x 11th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_tgl%22)
+- [NovaCustom NS5x 12th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_adl%22)
 - [NovaCustom NS5x 11th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_tgl%22)
 - [NovaCustom NS5x 12th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_adl%22)
 - [NovaCustom NS7x 11th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_tgl%22)
@@ -32,6 +38,8 @@
 - [NovaCustom NV4x 12th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_nv4x_adl%22)
 - [NovaCustom V54x 14th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_v54_mtl%22)
 - [NovaCustom V56x 14th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_v56_mtl%22)
+- [NovaCustom V54x 14th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_v54_mtl%22)
+- [NovaCustom V56x 14th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label% scraper