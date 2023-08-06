mac
====

mac is a command line tool that allows to
  - bootstrap bash scripts when you are creating a new cloud server, allowing to hook configuration management systems like Puppet, Chef, Ansible and more
  - create cloud infrastructures in Amazon Web Services, Google Cloud Engine, Digital Ocean and Rackspace.
  - manage servers and infrastructures

mac is very useful for a set of business cases such:
 - `Orchestration of geographically disperse infrastructures <https://manageacloud.com/case-study/geographically-disperse-infrastructures>`_
 - `Continuous Integration <https://manageacloud.com/case-study/continuous-integration>`_
 - `Disaster Recovery <https://manageacloud.com/case-study/disaster-recovery>`_
 - `Continuous Delivery <https://manageacloud.com/case-study/continuous-delivery>`_
 - `Cloud benchmarking <https://manageacloud.com/case-study/cloud-benchmark>`_
 - `A/B Testing <https//manageacloud.com/case-study/ab-testing>`_



Installing the CLI
------------------

An automatic installation can be performed with the following command:

.. sourcecode:: bash

    curl -sSL https://manageacloud.com/mac | bash

You can also use ``pip install``:

.. sourcecode:: bash

    pip install mac --pre


Getting started with the CLI
----------------------------

Once is installed, you need to login. `Create an account <https://manageacloud.com/register>`_ (it takes 1 minute)
if you don't have one available.

.. sourcecode:: bash

    $ mac -h
    usage: mac [-h] [--version] [-v] [-q]
               {login,instance,configuration,infrastructure} ...

    Manageacloud.com CLI

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program\'s version number and exit
      -v, --verbose         Show verbose information
      -q, --quiet           Enable loggable output

    mac's CLI commands:
      {login,instance,configuration,infrastructure}
        login               Login into Manageacloud.com
        instance            Instance related operations
        configuration       Server configuration related operations
        infrastructure      Infrastructure operations

Documentation
-------------
Documentation is available at https://manageacloud.com/article/orchestration/cli

Examples
--------

Create two instances of `Demo Application <https://manageacloud.com/configuration/demo_application>`_ in Amazon Web Services and configure a load balancer.

.. sourcecode:: yaml

    mac: 0.7.1
    description: Infrastructure demo
    name: demo
    version: '1.0'

    roles:

      app:
        instance create:
          configuration: demo_application
          environment:
          - DB_IP: 127.0.0.1
          - APP_BRANCH: master

    actions:
       get_id:
          ssh: wget -q -O - http://169.254.169.254/latest/meta-data/instance-id

       get_availability_zone:
          ssh: wget -q -O - http://169.254.169.254/latest/meta-data/placement/availability-zone


    resources:

       build_lb:
          create bash:
            aws elb create-load-balancer
              --load-balancer-name my-load-balancer
              --listeners Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80
              --region infrastructure.app_inf.location
              --availability-zones role.app.get_availability_zone

       register_lb:
          create bash:
            aws elb register-instances-with-load-balancer
              --load-balancer-name my-load-balancer
              --instances role.app.get_id
              --region infrastructure.app_inf.location

    infrastructures:

      app_inf:
        name: app
        provider: amazon
        location: us-east-1
        hardware: t1.micro
        role: app
        amount: 2

      build_lb_inf:
        resource: build_lb

      register_lb_inf:
        resource: register_lb

Demo requirements:
 - Install and configure `aws cli <http://docs.aws.amazon.com/cli/latest/userguide/installing.html#install-with-pip>`_ and `mac cli <https://manageacloud.com/article/orchestration/cli/installation>`_
 - Deploy a production server at `Manageacloud <https://manageacloud.com/login>`_ (sign up takes 1 minute)
 - save the previous contents to a file called ``infrastructure.macfile`` and run the command ``mac infrastructure macfile infrastructure.macfile``


Build status
------------

|mac-1| Debian Wheezy 7

|mac-2| Ubuntu Trusty Tahr 14.04

|mac-3| CentOS 6.5

|mac-5| CentOS 7

|mac-6| Ubuntu Utopic Unicorn 14.10

|mac-7| Debian Jessie 8

|mac-8| Ubuntu Ubuntu Vivid Vervet 15.04

.. |mac-1| image:: https://manageacloud.com/configuration/mac/build/1/image
.. _mac-1: https://manageacloud.com/configuration/mac/builds
.. |mac-2| image:: https://manageacloud.com/configuration/mac/build/2/image
.. _mac-2: https://manageacloud.com/configuration/mac/builds
.. |mac-3| image:: https://manageacloud.com/configuration/mac/build/3/image
.. _mac-3: https://manageacloud.com/configuration/mac/builds
.. |mac-5| image:: https://manageacloud.com/configuration/mac/build/5/image
.. _mac-5: https://manageacloud.com/configuration/mac/builds
.. |mac-6| image:: https://manageacloud.com/configuration/mac/build/6/image
.. _mac-6: https://manageacloud.com/configuration/mac/builds
.. |mac-7| image:: https://manageacloud.com/configuration/mac/build/7/image
.. _mac-7: https://manageacloud.com/configuration/mac/builds
.. |mac-8| image:: https://manageacloud.com/configuration/mac/build/8/image
.. _mac-8: https://manageacloud.com/configuration/mac/builds