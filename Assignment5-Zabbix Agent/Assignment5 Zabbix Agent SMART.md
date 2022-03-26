## Assignment 5 - Zabbix Agent

### What is going on?
Zabbix Agent info:
https://www.zabbix.com/ru/zabbix_agent

Zabbix Trigger setup:
https://www.zabbix.com/documentation/5.4/ru/manual/config/triggers/trigger


### Steps
1. Create/Install/Deploy your own Zabbix server.
Hint: Zabbix supports preinstalled Zabbix-servers "Zabbix Appliances" VMware/VirtualBox/KVM images https://www.zabbix.com/download_appliance

Login:password for appliance is
* System
appliance:zabbix ( in 5.0 and 6.0 root:zabbix )
* Frontend
Admin:zabbix
https://www.zabbix.com/documentation/6.0/manual/appliance

3. Install Zabbix agent
During installation, change only Servers to your_zabbix_server_ip (for example 192.168.88.254)
Prefer MSI-installer Zabbix Agent (if you install on Windows)
https://www.zabbix.com/download_agents

Better to use zip archive to install.

4. Edit zabbix_agentd.conf file. Set "Server=", "Hostname="

5. Run Zabbix Agent service with settings. For example
c:\zabbix\zabbix_agentd.exe -c c:\zabbix\zabbix_agentd.conf -i

6. Update Firewall settings.

netsh advfirewall firewall add rule name="ZabbixAgent" protocol=TCP localport=10050 action=allow dir=IN

7. Add host Configuration > Hosts > Create host

Set hostname, Templates (for example Windows CPU by Zabbix agent), Groups (for example Windows Agents), Interfaces: Type Agent, value = <monitoring machine IP>

8. Monitoring > Hosts, your host, Graphs. Check that graphs appears.

9. Monitoring > Dashboard > Add > Graph
Set name (for example P50 CPU load), Refresh interval, Data set (for example p50), Item pattern (for example CPU utilization)

10. Setup Trigger for CPU load
https://www.zabbix.com/documentation/current/ru/manual/config/triggers


11. Add trigger with Trigger Expression for Example 
min(/p50/system.cpu.util,1m)>10

12. Check on Dashboard that trigger works

13. Create report with Assignment6 description into docx and send by e-mail for checking.