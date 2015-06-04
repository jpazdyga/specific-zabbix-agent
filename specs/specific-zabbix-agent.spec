Summary:	Specific Zabbix Agent configuration.
Name:		specific-zabbix-agent
Version:	version2sub
Release:	release2sub
Vendor:		Zabbix
Group:		System Environment/Libraries
License:	GPL
URL:		https://github.com/jpazdyga/specific-zabbix-agent
Source0:	specific-zabbix-agent-version2sub-release2sub.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	zabbix-agent

%description
This RPM provides specific configuration for zabbix-agent daemon.
Configuration file, config fragments directory and a custom init script.
https://github.com/jpazdyga/specific-zabbix-agent

%pre
echo "Running pre..."
/etc/init.d/zabbix-agent stop

%prep
echo "PREP:"
pwd
tar -xvf %{SOURCE0}
cd %{name}-%{version}-%{release}
ls

%setup -c -n %{name}-%{version}

%build
echo "BUILD:"
pwd
cd %{name}-%{version}-%{release}

%install
pwd
cd %{name}-%{version}-%{release}
mkdir -p $RPM_BUILD_ROOT/{opt/specific-zabbix-agent/etc/zabbix,opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d,etc/init.d}
cp ./config/zabbix_agentd.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix
cp ./config/zabbix_agentd.d/openssl_check.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/remote_icmp_monitoring.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/sockstat_tcp_alloc.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/sockstat_tcp_inuse.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/sockstat_tcp_mem.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/sockstat_tcp_orphan.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/sockstat_tcp_tw.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/sysctl_var.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./config/zabbix_agentd.d/userparameter_mysql.conf $RPM_BUILD_ROOT/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d
cp ./initscript/specific-zabbix-agent $RPM_BUILD_ROOT/etc/init.d

%post
/sbin/chkconfig --add specific-zabbix-agent
/sbin/chkconfig --level 345 specific-zabbix-agent on
/sbin/service specific-zabbix-agent start

%files
%defattr(644, zabbix, zabbix)
%config /opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/openssl_check.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/remote_icmp_monitoring.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/sockstat_tcp_alloc.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/sockstat_tcp_inuse.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/sockstat_tcp_mem.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/sockstat_tcp_orphan.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/sockstat_tcp_tw.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/sysctl_var.conf
/opt/specific-zabbix-agent/etc/zabbix/zabbix_agentd.d/userparameter_mysql.conf
%attr(755, root, root) /etc/init.d/specific-zabbix-agent

%define date    %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%changelog

* Fri Apr 20 2015 Jakub Pazdyga <admin@lascalia.com> - 0.0.1-4
- First test release on aws-based host.
        
* Mon Feb 23 2015 Jakub Pazdyga <admin@lascalia.com> - 0.0.1-1
- Initial release just to try things out.
