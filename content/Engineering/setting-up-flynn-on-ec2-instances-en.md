Title: Setting up Flynn PaaS on EC2 Instances
Date: 2017-08-07
Slug: setting-up-flynn-on-ec2-instances
Lang: en
Tags: deployment; flynn;
Author: Shauryadeep Chaudhuri
Summary: A Guide to setup Flynn as an in-house PaaS in Amazon EC2 Instances.

Continuing from [The Game of Deployment](https://blog.xoxzo.com/2017/07/26/the-game-of-deployment/), Today we will discuss from how to start from setup Flynn clusters to how to deploy your app to these clusters. This serves as an end to end guide for Flynn, from my experience researching Flynn as a possible deployment management candidate.

Basically, you would need to follow certain steps and everything would be ready. It's just that simple.

For a nice smooth performance of the cluster, Flynn recommends, each node should be a machine with 2 GB Ram, 40 GB Storage, 2 CPUs with 2 cores each.
And for high availability, a cluster should have at least 3 nodes.

Although Flynn runs on both Ubuntu 14.04 & 16.04 while setting up I faced lesser issues on Ubuntu 16.04.
We would assume you would setup Flynn on yourflynn.yourdomainname.com

Setup Flynn Cluster
------------------

1. Run:
		
		sudo bash < <(curl -fsSL https://dl.flynn.io/install-flynn)	

	This would install Flynn. Repeat this in each machine which should act as a node in the cluster.

2. Make sure the nodes have all their TCP & UDP ports open between them internally.
	That is if there are two nodes -> node1 & node2, they should be able to communicate among themselves through any of the ports.
	Although all the ports do not need to be open to the external world.

3. Open the following ports to be accessed by the external world.

	* 80 -> HTTP ports
	* 443 -> https ports
	* 3000-3500 -> TCP Ports which are used by certain processes like Postgres,MySQL  etc.

	Note: If you cannot define the internally & externally open ports separately, you should put a firewall blocking external access to the ports.

4. Next on, you would need to generate a token which would allow the cluster to discover each node during bootstrapping of the cluster.
	
	* Generate Token on any one of the nodes -: 
		
			sudo flynn-host init --init-discovery
		*O/P: https://discovery.flynn.io/clusters/53e8402e-030f-4861-95ba-d5b5a91b5902*
	
	* Now you need to use this token and attach it to other nodes.
		
			sudo flynn-host init --disovery https://discovery.flynn.io/clusters/53e8402e-030f-4861-95ba-d5b5a91b5902
	
5. Start the flynn-host service in each node.

	If you are working on Ubuntu 14.04

			sudo start flynn-host
			sudo status flynn-host   ---> Check The status of the service.

	If you are working on Ubuntu 16.04

			sudo systemctl start flynn-host
			sudo systemctl status flynn-host   ---> Check The status of the service.

6. Setup DNS Names -> Since It is a clustered approach you would need to setup DNS Records that point to each of the nodes.
You would need to set A records for each of the node & a wildcard domain cname to the cluster domain name.

		Domain 							DNS Record Type						Address
		yourflynn.yourdomainname.com 			A						10.0.0.11
		yourflynn.yourdomainname.com 			A						10.0.0.12
		yourflynn.yourdomainname.com 			A						10.0.0.13
		yourflynn.yourdomainname.com 			A						10.0.0.14
		*.yourflynn.yourdomainname.com 		  CNAME					yourflynn.yourdomainname.com
		
7. After You have done all this, you have to bootstrap Flynn. You need to run the following command in any one of the nodes.

        sudo \
            CLUSTER_DOMAIN=demo.localflynn.com \
            flynn-host bootstrap \
            --min-hosts 3 \
            --discovery https://discovery.flynn.io/clusters/53e8402e-030f-4861-95ba-d5b5a91b5902

	
The discovery token should be the same one which you generated in Step 3.


Congratulations, You are done with setting up your cluster. Copy the message you get and keep it secure. This contains Token needed to add this Flynn cluster in your Flynn cli.


Configuring a project for Flynn
--------------------------------

1. Make sure you can run your application locally without Flynn.
2. Create a file "Procfile" and add the processes that need to run for your processes, like:
	
		process_name: process command

	For example, if we want to run a Django app with celery scheduler and celery beat for periodic tasks.

			web: gunicorn projectapp.wsgi --log-file -
			celeryd : celery -A projectapp worker -l info
			celerybeat: celery -A projectapp beat -l info
	
	
3. Make sure you have the file which lists all the dependencies. For ex:- requirements.txt in Python, package.json in NodeJs.

	The above steps should be sufficient to deploy. But you can do further customization.

4.  Generally, the latest version of the detected environment is used. But if you want your application to run on a particular environment, you can create a file "runtime.txt" which would list the environment. runtime.txt containing one line -> python-2.7.8

5. Flynn similar to Heroku uses Buildpacks to compile your application. Right from detecting your app environment to installing and running your dependencies.
Sometimes it might be possible that you may want to use multiple buildpacks. 
Ex:-
	You may want to install extra Linux dependencies before you compile.

Or you may want to

	Run an application which is not yet supported by the default buildpack like a Tornado or CherryPy Application.

For this, you would need to create a file *".buildpacks"*, and list out URL of every buildpack that you need.


Installing Flynn CLI(on your development box)
---------------------
It's just one command to run:

	L=/usr/local/bin/flynn && curl -sSL -A "`uname -sp`" https://dl.flynn.io/cli | zcat >$L && chmod +x $L

Once Flynn CLI is installed, just run the command which you got when Bootstrapping finished for Flynn Cluster.
The command looks like:-

    flynn cluster add -p <tls pin> <cluster name> <controller domain> <controller key>

Example:-

     flynn cluster add -p KGCENkp53YF5OvOKkZIry71+czFRkSw2ZdMszZ/0ljs= production https://controller.dev.localflynn.com e09dc5301d72be755a3d666f617c4600


Deploying an Application to Flynn
----------------------------------
Once you setup the clusters, configured your projects and setup the CLI, you would want.

1. List your clusters:
	flynn cluster
	
2. Switch to your cluster
	flynn -c cluster name
	
3. The project needs to be initialized with Git. If it is not initialized with git init folder_name

4. Attach it to an app in flynn cluster

    * If it is a new app
        flynn create new_app_name

    * If you want to attach with an existing app in Flynn
        flynn -a <app_name> remote add <git_remote_name>  --> git_remote_name defaults to flynn.
	
5. Push it like you push to any git repo.
	git add .
	git commit
	git push flynn master
	
After the push is completed you will see that the application is building. If any errors occur, you will get them in the command line.


Additional Information
-----------------------

Setting up local Flynn
-----------------
You can try Flynn on your local machine before you actually set up on the cloud, just to get a bit of taste of it. 
You would need VirtualBox & Vagrant Box installed.
Copy the Flynn Repo
	git clone https://github.com/flynn/flynn

Setup :-

		make init
		make dashboard

Start & Shutdown

		make down
		make up

Logging in Flynn
----------------
Since Flynn is a cloud based clustered solution, meaning you will probably not be able to retrieve your logs, and you could lose them with each deployment.
There are two solutions to this

* You can send all the INFO,DEBUG,WARNING,ERROR messages to stdout/stderr and it will be automatically be logged by  flynn.

* If you would like to segregate logging of different modules, you can use a remote syslog server and send your logs there.

