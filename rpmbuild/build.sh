#!/bin/bash

####
#
#       This script should be executed always from "./"
#       Also, you need to edit variables to adjust them to your rpmbuild env
#
####

variables()
{

        reponame="specific-zabbix-agent"
        versiontobuild="0.0.1-5"
        currentdir=`pwd`
        root=`echo $currentdir | awk -F '/' 'sub(FS $NF,x)'`
        specname="specific-zabbix-agent.spec"
        fullversionname="$reponame-$versiontobuild"
        bldroot="$HOME/rpmbuild"
        srcroot="$bldroot/SOURCES"
        specsroot="$bldroot/SPECS"
        rpmroot="$bldroot/RPMS"
        zabbixserver="zabbix.internal.domain.com"
        arch="noarch"
        rpmname="$fullversionname.$arch.rpm"
        oldchangelogtxt=`sed -n '/%changelog/,$p' $root/specs/$specname | grep -v '%changelog'`

        ## Do not forget to update the Changelog:

        changelogtxt="
        * Fri May 15 2015 Jakub Pazdyga <admin@lascalia.com> - $versiontobuild
        - Changed dummy Zabbix server name to zabbix.internal.domain.com.
        "

##

}

buildconf()
{

        cd $srcroot

        ## Substitute spec file template to make it working, updated SPEC:
        if [ -w $specsroot ];
        then
                version2sub=`echo $versiontobuild | awk -F '-' '{print $1}'`
                release2sub=`echo $versiontobuild | awk -F '-' '{print $2}'`
                sed -e "s/version2sub/$version2sub/g" -e "s/release2sub/$release2sub/g" $root/specs/$specname | sed '/%changelog/q' > $specsroot/$specname
                echo "$changelogtxt" >> $specsroot/$specname
                echo "$oldchangelogtxt" >> $specsroot/$specname
                sed '/%changelog/q' $root/specs/$specname > $root/specs/$specname.tmp
                echo "$changelogtxt" >> $root/specs/$specname.tmp
                echo "$oldchangelogtxt" >> $root/specs/$specname.tmp
                mv $root/specs/$specname.tmp $root/specs/$specname
        else
                echo "No 'SPECS' subdirectory"
        fi
        ##

        ## Subsitute Zabbix server name in configuration file:
        sed -e "s/server2sub/$zabbixserver/g" $root/config/zabbix_agentd.conf > $root/config/zabbix_agentd.conf.tmp
        mv $root/config/zabbix_agentd.conf $root/config/zabbix_agentd.conf.orig
        mv $root/config/zabbix_agentd.conf.tmp $root/config/zabbix_agentd.conf
        ##

        ## Create Source0 archive:
        cp -rp $root $fullversionname
        tar -cvf $fullversionname.tar --exclude .git --exclude specs --exclude rpmbuild --exclude rpms $fullversionname
        gzip -f $fullversionname.tar
        rm -fr $fullversionname
        ## Build preparation ends here ##
}

builcommand()
{
        cd $bldroot
        rpmbuild -bb $specsroot/$specname
}

## Variables:
variables

## Configuring the build:
buildconf

## Perform actual RPM package build:
builcommand

## Move configuration file to be a template again:
mv $root/config/zabbix_agentd.conf.orig $root/config/zabbix_agentd.conf

## Place new rpm in subdirectory:
cd $currentdir
cp -rpv $rpmroot/$arch/$rpmname $root/rpms/$arch/$rpmname
ls -la $root/rpms/$arch/$rpmname
