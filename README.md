# MyCloud (working name)
---------------------------------

_What is this?_
My cloud is a personal cloud storage application for documents, music, and contacts. These are the trinity of personal mobility right now. I'm aware of applications like owncloud. This project is part experiment to learn how to build something like this and part project to apply that learning to it's constant improvement and maybe even offer an alternative (however similar) to something like owncloud!

_How will it work?_
The main interface is an upload page. The app is primarily an api for uploading documents from things like your phone or home server -- designed to interface with applications. Therefore the web interface isn't a top priority right now. 

However, the upload page will feature an upload and description input. The description is a drop down: document, contact, music. The file will be stored in one of those categories and available on your mobile devices.

# Features

My Cloud is an API. It allows users to set up their own cloud server and interface with it via mobile devices. Users can upload documents, contacts and music as well as download them and share them.

My Cloud can be installed on pretty much any Unix environment.

### The My Cloud App

The other half of the project is the mobile app, which will interface with My Cloud. To set it up, users will simply enter their server address and security code.

Security access is configured with DUO. When the server is built, it communicates with DUO. When accessed from mobile it will send a code to that phone to verify the configuration and proceed. The goal is no passwords. Users who set up a server should be able to install the app, enter the code and use it.