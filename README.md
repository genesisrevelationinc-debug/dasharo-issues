# Dasharo Issues repository

This repository tracks issues and feature development progress for the
[Dasharo Project](https://dasharo.com/). This repository tracks issues
for most of the repositories in the Dasharo universe. There are some exceptions
with their own trackers, listed below:
- [Open Source Firmware Validation](https://github.com/Dasharo/open-source-firmware-validation/issues)

You can [file a new issue](https://github.com/Dasharo/dasharo-issues/issues/new/choose)
or [view all issues](https://github.com/Dasharo/dasharo-issues/issues).

## Bug Bounty

You can find more details on the Bug Bounty program
[on our website](https://3mdeb.com/bug-bounty/).

Bounties are categorized per difficulty:
- [Warmup](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+label:bounty-warmup)
- [Easy](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+label:bounty-easy)
- [Medium](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+label:bounty-medium)
- [Hard](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+label:bounty-hard)

Bounties per product:
- [DasharoToolsSuite](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+%28label:bounty-warmup+OR+label:bounty-easy+OR+label:bounty-medium+OR+label:bounty-hard+OR+label:bounty%29+AND+label:DasharoToolsSuite)
- [Others (mostly Dasharo firmware or documentation)](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+%28label:bounty-warmup+OR+label:bounty-easy+OR+label:bounty-medium+OR+label:bounty-hard+OR+label:bounty%29+-label:DasharoToolsSuite)

You can also view all bounties
[here](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+%28label:bounty-warmup+OR+label:bounty-easy+OR+label:bounty-medium+OR+label:bounty-hard+OR+label:bounty%29).

<!-- BEGIN DEVICE ISSUES -->
## Issues per device

Below is a list of open issues affecting specific devices:
- [Asus KGPE-D16](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22asus_kgpe-d16%22)
- [Dell OptiPlex 7010](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22dell_optiplex_9010%22)
- [Dell OptiPlex 9010](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22dell_optiplex_9010%22)
[here](https://github.com/Dasharo/dasharo-issues/issues?q=is:issue+state:open+%28label:bounty-warmup+OR+label:bounty-easy+OR+label:bounty-medium+OR+label:bounty-hard+OR+label:bounty%29).

## EC Testability Interface Implementation

### Overview

This document describes the implementation of an EC testability interface to enable comprehensive remote testing capabilities for laptops. The interface provides a simple console interface to control platform aspects like generating key presses, button presses, and controlling power.

### Features

- **Remote Control Interface**: Simple console interface over SMBus or parallel interface for EC control
- **Key Press Generation**: Ability to simulate key presses remotely
- **Button Press Simulation**: Capability to simulate hardware button presses
- **Power Control**: Remote power state control functionality
- **BIOS Configuration**: Debugging option that defaults to disabled

### Implementation Details

The implementation extends the debugger firmware to support a bidirectional console interface that allows:

- Sending commands to the EC for key/button simulation
- Controlling power states remotely
- Configuring via BIOS settings (must be enabled explicitly)

### Security Considerations

- BIOS debugging option defaults to disabled
- Proper authentication and access controls should be implemented
- Interface should only be enabled in controlled testing environments

### Usage

This interface is intended for remote testing scenarios and should be used with appropriate security measures in controlled environments only.

<!-- BEGIN DEVICE ISSUES -->
- [NovaCustom NS5x 11th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_tgl%22)
- [NovaCustom NS5x 11th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_adl%22)
- [NovaCustom NS7x 11th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_tgl%22)
- [NovaCustom NS7x 12th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_ns5x/7x_adl%22)
- [NovaCustom NUC BOX 14th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_nuc_box%22)
- [NovaCustom NV4x 11th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_nv4x_tgl%22)
- [NovaCustom NV4x 12th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_nv4x_adl%22)
- [NovaCustom V54 14th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_v54_mtl%22)
- [NovaCustom V56 14th Gen](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22novacustom_v56_mtl%22)
- [PC Engines APU2](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22pcengines_apu2%22)
- [PC Engines APU3](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22pcengines_apu2%22)
- [PC Engines APU4](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22pcengines_apu2%22)
- [PC Engines APU6](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22pcengines_apu2%22)
- [Protectli FW2B](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_bsw%22)
- [Protectli FW4B](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_bsw%22)
- [Protectli FW4C](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_bsw%22)
- [Protectli FW6](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_kbl%22)
- [Protectli V1210](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_jsl%22)
- [Protectli V1211](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_jsl%22)
- [Protectli V1410](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_jsl%22)
- [Protectli V1610](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_jsl%22)
- [Protectli VP2410](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_glk%22)
- [Protectli VP2420](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_ehl%22)
- [Protectli VP2430](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_adln%22)
- [Protectli VP2440](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_adln%22)
- [Protectli VP3210](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_adln%22)
- [Protectli VP3230](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_adln%22)
- [Protectli VP4630](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_cml%22)
- [Protectli VP4650](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_cml%22)
- [Protectli VP4670](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_cml%22)
- [Protectli VP6630](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_adl%22)
- [Protectli VP6650](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_adl%22)
- [Protectli VP6670](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22protectli_vault_adl%22)
- [QEMU Q35 Emulator](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22qemu_q35%22)
- [Raptor CS Talos II](https://github.com/dasharo/dasharo-issues/issues?q=is%3Aissue+state%3Aopen+label%3A%22raptor-cs_talos-2%22)
<!-- END DEVICE ISSUES -->

## GitHub help

* [GitHub search syntax](https://help.github.com/articles/search-syntax/)
* [GitHub search syntax related to issues](https://help.github.com/articles/searching-issues/)
