### Ucloud Python SDK and Command-Line Tool
UcloudClient is a python sdk and a command-line client for Ucloud that brings
the command set for Uhost, Unet, Umon APIs together in a single shell with a
uniform command structure.
welcome to contribute to this tools.		
feel free to contact me if you find any bugs or have good advices.

#### 设计理念    
这个项目包含python sdk 和 命令行工具,覆盖了UHOST,UNET,UMON这三大资源管理.SDK设计上也是按前面三大资源来做区分.
由于一直有研究openstack,发现它的命令行做得很不错,所以这里命令行则是参考了openstack 命令行工具的资源管理命令,
基本上每种资源都有以下五个操作:	

1. list:查询本类所有的创建的资源,输出应该是列表,包含资源名称和ID等重要信息.    
2. show:通过ID查询本类资源的某个创建资源的详细信息.    
3. CUD:create, update, delete. 增删改三个操作.

#### 特色:

1. 命令可以加 "--debug" 来查看操作的关键路径的打印信息.
2. 命令可以加 "--timming" 来获得执行命令所花费的时间.

#### Unit Test:
已经完成shell,client,HTTPClient的unit test.主要使用了testtools,mock,fixtures等第三方模块.
依赖请查看teset-requirements.txt.

#### 软件查看下载:
pypi: [https://pypi.python.org/pypi/ucloudclient](https://pypi.python.org/pypi/ucloudclient)

#### 贡献：
代码遵守PEP8风格。

#### 1. sdk usage:

install via pip:
	
	#pip install ucloudclient

example codes:

        from ucloudclient.client import Client as uclient
        cl = uclient(base_url, public_key, private_key)
        uhosts = cl.uhost.get(region="us-west-01")
        print uhosts

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



#### 2. command-line usage:
使用之前,先编辑下uclud.rc文件,然后导入环境变量,接下来的命令就不用输入你的认证信息了.

		hyphendeMacBook-Air:ucloud-python-sdk hyphen$ cat ucloud.rc 
		export UCLOUD_REGION="cn-north-03"
		export UCLOUD_URL="https://api.ucloud.cn"
		export UCLOUD_PUBKEY="asdf"
		export UCLOUD_PRIKEY="asdf"
		export PS1='[\u@\h \W(ucloud)]\$ '

		hyphendeMacBook-Air:ucloud-python-sdk hyphen$ source ucloud.rc

命令帮助:

        (.venv)hyphendeMacBook-Air:ucloud-python-sdk hyphen$ $ ucloud
        usage: ucloud [--debug] [--timing] <subcommand> ...

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
            uhost-image-show         show image details
            uhost-list               list uhosts
            uhost-list-snapshot      list snapshots of an instance
            uhost-modify-name        modify a host's name
            uhost-modify-tag         modify a host's tag
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
            unet-eip-list            list eip
            unet-eip-price-get       get eip price
            unet-eip-release         release an eip
            unet-eip-show            show eip details info
            unet-eip-unbind          unbind ip to given resource
            unet-eip-update          update an eip
            unet-eip-weight-modify   modify weight of a given eip
            unet-sec-create          create security group
            unet-sec-delete          delete given security group
            unet-sec-grant           grant given security group to specified resource
            unet-sec-list            get security group info.you can filte by reource
                                     id or resource type.
            unet-sec-resource-get    get resource attached to given security group
            unet-sec-show            get security group details info.
            unet-sec-update          update security group
            unet-vip-allocate        allocate a vip
            unet-vip-list            list vip
            unet-vip-release         release a vip
            bash-completion          Prints all of the commands and options to stdout
                                     so that the ucloud.bash_completion script doesn't
                                     have to hard code them.
            help                     Display help about this program or one of its
                                     subcommands.

        Optional arguments:
          --debug                    Print debugging output
          --timing                   Print call timing info

        See "ucloud help COMMAND" for help on a specific command.

命令样例:

        hyphendeMacBook-Air:ucloud-python-sdk hyphen$ ucloud uhost-show uhost-4dmzop
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

        (.venv)hyphendeMacBook-Air:ucloud-python-sdk hyphen$ ucloud  uhost-image-list

        +---------------+------------------------+---------+
        | ImageId       | ImageName              | OsType  |
        +---------------+------------------------+---------+
        | uimage-0duw4w | CentOS 5.8 64位        | Linux   |
        | uimage-0nvikt | RHEL 6.2 64位          | Linux   |
        | uimage-0xalan | Gentoo 2.2 64位        | Linux   |

        (.venv)hyphendeMacBook-Air:ucloud-python-sdk hyphen$ ucloud  uhost-image-show uimage-0duw4w
        +------------------+--------------------------------------------------+
        | Property         | Value                                            |
        +------------------+--------------------------------------------------+
        | CreateTime       | 1394435416                                       |
        | ImageDescription | Community ENTerprise Operating System 5.8 64-bit |
        | ImageId          | uimage-0duw4w                                    |
        | ImageName        | CentOS 5.8 64位                                  |
        | ImageType        | Base                                             |
        | OsName           | CentOS 5.8 64位                                  |
        | OsType           | Linux                                            |
        | State            | Available                                        |
        +------------------+--------------------------------------------------+
