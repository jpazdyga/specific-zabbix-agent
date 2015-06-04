# specific-zabbix-agent

###########################################################################################
     This repository contains source, scripts and config files to build a RPM
     package for specific configuration of zabbix-agent daemon.
     The RPM comes with configuration file, config fragments directory, example
     addidtional custom configs and a custom init script.
###########################################################################################

Please take a closer look at build script in 'rpmbuild/build.sh' when you run it, the rpm should be created and stored in rpms/noarch/<br />
This file contains couple of variables requierd for successful build. Thay are pretty self-explanatory I think. Those I'd consider as most important:<br />
1. $versiontobuild: Change this for each next version of package to be built.<br />
2. $zabbixserver: Hostname or IP address of target Zabbix server.<br />
3. $specname: Spec file location. This file is actually only a template, I'm using sed's substitution to edit this.<br />
4. $changelogtxt: Just write your Changelog note here. It'll be added to spec file.<br />
!! Important: You need to cwd to directory containing 'build.sh' script before executing it. !!<br />
<br />
This rpm requires the original 'zabbix-agent' rpm to be installed.<br />
Take a look at first line of 'config/zabbix_agentd.conf' also: there's a Zabbix server address provided (it's configured from 'rpmbuild/build.sh' script), and this can be modified before rpmbuild for each server needed (or changed by using puppet, after rpm installation).<br />

