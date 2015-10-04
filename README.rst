BoredBot is an exercise at packaging Python applications.

The application is pretty simple: a web UI in Flask, and a robot using a hand-rolled loop.
The robot connects to Parse.com using two different accounts (one for the mood and one for the update),
to simulate using more than one API service and needing several API keys.

It is packaged securely (the sources are all public on GitHub, but the API keys are encrypted)
and reliably (it builds a Pex file inside a Docker, in order to maximize isolation).
It is also intended as a proof of concept for separating the build docker (needing to include
a build environment) and a smaller runner docker, which has fewer dependencies.
