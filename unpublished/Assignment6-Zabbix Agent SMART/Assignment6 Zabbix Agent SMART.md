## Assignment 6 - Agent SMART

### What is going on?
Agent for SMART status monitoring. On Windows or Linux host - as you prefer.
Based on:
* https://share.zabbix.com/storage-devices/smart-monitoring-with-smartmontools-lld
* https://github.com/v-zhuravlev/zbx-smartctl/



### Steps
1. Create/Install/Deploy your own Zabbix server.
Hint: Zabbix supports preinstalled Zabbix-servers "Zabbix Appliances" VMware/VirtualBox/KVM images https://www.zabbix.com/download_appliance

Login:password for appliance is
* System
appliance:zabbix ( in 5.0 root:zabbix )
* Frontend
Admin:zabbix
https://www.zabbix.com/documentation/5.0/manual/appliance

2. Install smartmontools tools on machine which you going to monitor (SMART is unavailable on Virtual Machine guest!)
When installing, the settings do not need to be changed
https://sourceforge.net/projects/smartmontools/files/

3. Install Zabbix agent
During installation, change only Servers to your_zabbix_server_ip (for example 192.168.88.254)
Prefer MSI-installer Zabbix Agent (if you install on Windows)
https://www.zabbix.com/download_agents

4. Put the smartctl-disks-discovery.ps1 script in the Zabbix Agent folder
https://github.com/v-zhuravlev/zbx-smartctl/blob/master/discovery-scripts/windows/smartctl-disks-discovery.ps1

5. Put the configuration file zabbix_smartctl.win.conf in the Zabbix Agent/zabbix_agentd.conf.d folder
https://github.com/v-zhuravlev/zbx-smartctl/blob/master/zabbix_smartctl.win.conf

6. Restart the Zabbix agent service. In Windows run "services.msc" and find Zabbix agent there.
7. Put the Template_3.4_HDD_SMARTMONTOOLS_2_WITH_LLD.xml table to the Zabbix Agent folder
https://github.com/v-zhuravlev/zbx-smartctl/blob/master/Template_3.4_HDD_SMARTMONTOOLS_2_WITH_LLD.xml

8. Go to http://<your_zabbix_server_ip_here> Go to Configuration > Templates
import table Template_3.4_HDD_SMARTMONTOOLS_2_WITH_LLD.xml

9. Go to Configuration > Hosts > Add host.
Name the computer by its hostname, specify its IP address, click add.

10. Set Test-item for your Host to get green ZBX. (Ideally Trigger or Item setup should be done).

3. Create report with Assignment6 description into docx and send by e-mail for checking.