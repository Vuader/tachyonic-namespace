.. _components:

Components
==========

Tachyonic consists of multiple components such as a Web application frontend and multiple API endpoints.

* tachyonic_neutrino is a python WSGI framework developed for developing endpoints and web application interface.
* tachyonic_ui being the web interface only communicates with endpoints via RESTAPI using JSON data models.
* tachyonic_api is the base endpoint responsible for authentication and all common modules.

The Endpoint API(s) are responsible for interacting with the databases, executing RPC calls, messaging bus operations and all have there own configurations.

All API endpoints are exposed to the User Interface when they are registered via the base API configuration.

* tachyonic_common contains commonly used code by either workers, ui, api etc.
* tachyonic_client contains client modules for authenticating and using Tachyonic endpoints.

All the components developed are registered Tachyonic projects. Different endpoints can consume each other via the client.

Tachyonic comes with built-in customer database that provides multi-tiered, multi-tenant approach. Customers can have their own customers and domains are used as administrative domain for the infrastructure. Multiple domains mean one installation can be used to manage multiple infrastructures separately.

Modules or rather additional endpoints and web ui modules can be added to provide functionality such as managing the cloud, dns servers, email servers, network resources and monitoring. Even a billing engine can be integrated or built-into Tachyonic.


