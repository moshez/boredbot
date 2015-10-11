BoredBot
========

BoredBot is an exercise at packaging Python applications.

The application is pretty simple: a web UI in Flask, and a robot using a hand-rolled loop.
The robot connects to Parse.com using two different accounts (one for the mood and one for the update),
to simulate using more than one API service and needing several API keys.

It is packaged securely (the sources are all public on GitHub, but the API keys are encrypted)
and reliably (it builds a Pex file inside a Docker, in order to maximize isolation).
It is also intended as a proof of concept for separating the build docker (needing to include
a build environment) and a smaller runner docker, which has fewer dependencies.

The Inner Life of Web Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Web applications usually involve three distinct roles
(though, especially in small companies, can sometimes be done by the same people):

* Product code
* Infrastructure code
* Configuration

Product code is what people typically think of when they think of web applications:
a Django or Flask application, connecting to a database, executing business logic
and rendering pages.

Configuration is where decisions about deployment are made: do we connect to the
staging or master database? Which WSGI container should we use? Where do we keep
the logs?

Infrastructure is whatever code that is used by either product or configuration.
It can often be recognized as what companies tend to open source -- Facebook,
for example, open-sourced MCRouter_ and Square open-sourced Keywhiz_.
Product code is usually where companies differentiate, and so will usually
not open-source, while configuration tends to be too specific to be worthwhile
to open-source: it has API keys, names of databases, number of machines and
so forth. The parts of configuration that are general enough to be worthwhile
to open-source can just be called "infrastructure".

It is worthwhile to structure the code in a way that acknowledges these distinct
roles, and helps people remember which role they are executing.
In boredbot, the distinction is:

* "boredbot" is our product. Since this is meant to explain the other parts,
  the product is extremely simple: one web page, one updating loop.
* "luggage" is generic infrastructure.
* Everything else is configuration: boredbot_deploy, build.docker, run.docker, create and requirements.txt

.. _MCRouter: https://github.com/facebook/mcrouter
.. _Keywhiz: https://github.com/square/keywhiz

The Robot
~~~~~~~~~ 

* boredbot.parse -- has an easy way to create Parse.com headers.
* boredbot.update -- loops and update a Parse table with "I'm bored"
* boredbot.web -- pull data from two different Parse accounts: bored updates, and current mood.

The Infrastructure
~~~~~~~~~~~~~~~~~~

The infrastructure is in a package called "luggage", because it helps you pack your code.
For some reason, infrastructure engineers love these puns [#writer]_ .

* luggage.run -- has some utilities to help figure out current command line, and take advantage of NColony_
* luggage.buildpex -- has some utilities to help build a pex
* luggage.crypto -- has wrappers around PyNaCl to help maintain secrets in a dictionary.

.. _NColony: https://github.com/moshez/ncolony

The Configuration
~~~~~~~~~~~~~~~~~

* setup.py -- packages everything into one 'boredbot' wheel
* create -- script that assumes 'docker' and builds a docker image to deploy
* requirements.txt -- a list of dependencies, with exact versions
* build.docker -- Dockerfile describing the docker image to produce a 'boredbot.pex' (a Pex_ file)
* run.docker -- Dockerfile describing the docker image to deploy, which consumes boredbot.pex
* boredbot_deploy.__main__ -- Using mainland_, it outsources subcommands to other modules
* boredbot_deploy.config -- contains all configuration parameters. Secrets are encrypted.
* boredbot_deploy.encrypt -- a utility to encrypt new secrets
* boredbot_deploy.gunicorn -- wrapper for gunicorn to make it available in the Pex
* boredbot_deploy.mkpex -- parameters for building the pex file
* boredbot_deploy.wsgi -- WSGI app, adding the secrets to the boredbot.web blueprint
* boredbot_deploy.loop -- wrapper for the updating robot loop
* boredbot_deploy.start -- NColony configuration parameters for process running

.. _Pex: https://pex.readthedocs.org/en/stable/
.. _mainland: https://github.com/moshez/mainland/

The Deployment
~~~~~~~~~~~~~~

After running "./create", use "docker push" to push the images to Docker Hub.
The benefit of not keeping any unencrypted secrets in the Docker image is now apparent:
even if Docker Hub is compromised, sensitive keys are not leaked.

Now it is possible to run it anywhere, but for simplicity, here is how to use
docker-machine_:

.. code::

    $ eval $(docker-machine env <Logical machine name>)
    $ ## OK This is horrible. But hey, better than some used in real life!
    $ docker rm -f $(docker ps | python -c 'import sys;print " ".join(x.split()[-1] for x in sys.stdin if x.split()[1].startswith("moshez/boredbot"))')
    $ docker run --env SECRET_KEY=$(cat ../boredbot-secret-key)  -p 8000:8000  moshez/boredbot:latest

Note that this will not work for you! Because you do not have the file "borebdot-secret-key".
This is a feature, not a bug.
If you really want to try it out for yourself,
create a nacl secret key, put they public key in boredbot_deploy/config.py,
create two Parse.com applications, and update the application ID and keys in
boredbot_deploy/config.py.

In a real environment, the boredbot-secret-key might be kept on an encrypted Amazon EBS volume,
and mounted to a "beachhead" machine that deployers have access to.

The snippet above might be run in a loop, deployed to several machines.

.. _docker-machine: https://docs.docker.com/machine/get-started/

.. rubric:: Footnotes

.. [#writer] The writer of this README is an infrastructure engineer.
