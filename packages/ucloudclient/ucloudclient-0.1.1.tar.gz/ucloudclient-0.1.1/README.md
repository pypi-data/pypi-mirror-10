###Ucloud Python SDK and Command-Line Tool
this is a python sdk for ucloud,as well as a CLI tools for ucloud in linux bash env.
pypi: [https://pypi.python.org/pypi/ucloudclient](https://pypi.python.org/pypi/ucloudclient)    
welcome to contribute this tools.


####1. sdk usage:

a.install via pip:
	
	#pip install ucloudclient

example codes:

        from ucloudclient.client import Client as uclient
        cl=uclient(base_url, public_key, private_key)
        print cl.uhost.get(region="us-west-01")

output:

        {u'Action': u'DescribeUHostInstanceResponse', u'TotalCount': 1, u'RetCode': 0,
        u'UHostSet': [{u'Remark': u'', u'Tag': u'Default', u'Name': u'yan-1',
        u'State': u'Running', u'IPSet': [{u'IP': u'10.11.1.126', u'Type': u'Private'},
        {u'IPId': u'eip-yci4qr', u'IP': u'107.150.97.103', u'Bandwidth': 2,
        u'Type': u'International'}], u'DiskSet': [{u'Type': u'Boot',
        u'Drive': u'/dev/sda', u'DiskId': u'ce3b1751-d837-4949-9c73-29368b7fe820',
        u'Size': 20}], u'CPU': 1, u'OsName': u'Ubuntu 14.04 64\u4f4d',
        u'BasicImageId': u'uimage-nhwrqn',
        u'ImageId': u'ce3b1751-d837-4949-9c73-29368b7fe820', u'ExpireTime': 1429632272,
        u'UHostType': u'Normal', u'UHostId': u'uhost-4dmzop', u'NetworkState': u'Connected',
        u'ChargeType': u'Month', u'Memory': 2048, u'OsType': u'Linux', u'CreateTime': 1426953872,
         u'BasicImageName': u'Ubuntu 14.04 64\u4f4d'}]}



####2. command-line usage:
使用之前,先编辑下uclud.rc文件,然后导入环境变量,接下来的命令就不用输入你的认证信息了.

		hyphendeMacBook-Air:ucloud-python-sdk hyphen$ cat ucloud.rc 
		export UCLOUD_REGION="cn-north-03"
		export UCLOUD_URL="https://api.ucloud.cn"
		export UCLOUD_PUBKEY="asdf"
		export UCLOUD_PRIKEY="asdf"
		export PS1='[\u@\h \W(ucloudclient)]\$ '

		hyphendeMacBook-Air:ucloud-python-sdk hyphen$ source ucloud.rc
命令帮助:

        (.venv)hyphendeMacBook-Air:ucloud-python-sdk hyphen$ ucloud help
        usage: ucloud [--debug] [--timings] <subcommand> ...

        Command line interface for ucloud

        Positional arguments:
          <subcommand>
            uhost-attach-disk        attach a disk to a host
            uhost-create             boot a host
            uhost-create-image       create an image from a given host
            uhost-create-snapshot    create a snapshot from a host
            uhost-delete-image       delete an image by id
            uhost-detach-disk        attach a disk to a host
            uhost-get-price          get price of given type of host/s
            uhost-get-vnc            get a host's vnc connection information
            uhost-image-list         list all images
            uhost-list               list uhosts
            uhost-list-snapshot      list snapshots of an instance
            uhost-modify-name        modify a host's tag
            uhost-reboot             reboot a host
            uhost-reinstall          reinstall a host
            uhost-reset-password     reset a host's password
            uhost-resize             resize a host
            uhost-show               show detail of a host
            uhost-start              start a host
            uhost-stop               stop a host
            uhost-terminate          terminate a host
            umon-metric-get          get metic data
            unet-eip-bandwidth-modify
                                     modify bandwidth of a given eip
            unet-eip-bind            bind ip to given resource
            unet-eip-create          create an eip
            unet-eip-get             query eip in given id/s
            unet-eip-price-get       get eip price
            unet-eip-release         release an eip
            unet-eip-unbind          unbind ip to given resource
            unet-eip-update          update an eip
            unet-eip-weight-modify   modify weight of a given eip
            unet-sec-creat           create security group
            unet-sec-delete          delete given security group
            unet-sec-get             get security group info
            unet-sec-grant           grant given security group to specified resource
            unet-sec-reource-get     get resource attached to given security group
            unet-sec-update          update security group
            unet-vip-allocate        allocate a vip
            unet-vip-get             list vip
            unet-vip-release         release a vip
            bash-completion          Prints all of the commands and options to stdout
                                     so that the ucloud.bash_completion script doesn't
                                     have to hard code them.
            help                     Display help about this program or one of its
                                     subcommands.

        Optional arguments:
          --debug                    Print debugging output
          --timings                  Print call timing info

        See "ucloud help COMMAND" for help on a specific command.

命令样例:

        hyphendeMacBook-Air:ucloud-python-sdk hyphen$ ucloud uhost-show --uhostid uhost-4dmzop
        +----------------+------------------------------------------------------------------+
        | Property       | Value                                                            |
        +----------------+------------------------------------------------------------------+
        | BasicImageId   | uimage-nhwrqn                                                    |
        | BasicImageName | Ubuntu 14.04 64位                                                |
        | CPU            | 1                                                                |
        | ChargeType     | Month                                                            |
        | CreateTime     | 2015-03-22 00:04:32                                              |
        | Disk_0         | /dev/sda 20GB Type:Boot ID:ce3b1751-d837-4949-9c73-29368b7fe820  |
        | ExpireTime     | 2015-04-22 00:04:32                                              |
        | IP_0           | Private  10.11.1.126                                             |
        | IP_1           | International 2Mb/s 107.150.97.103 ID:eip-yci4qr                 |
        | ImageId        | ce3b1751-d837-4949-9c73-29368b7fe820                             |
        | Memory         | 2048                                                             |
        | Name           | yan-1                                                            |
        | NetworkState   | Connected                                                        |
        | OsType         | Linux                                                            |
        | Remark         |                                                                  |
        | State          | Running                                                          |
        | Tag            | Default                                                          |
        | UHostId        | uhost-4dmzop                                                     |
        | UHostType      | Normal                                                           |
        +----------------+------------------------------------------------------------------+