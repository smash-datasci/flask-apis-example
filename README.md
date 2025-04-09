# Flask Basic API teaching app

This is a bare-bones Flask app that serves 3rd party API data to teach how to use `requests` library to make HTTP requests from APIs. It is not an app with a UI or front-end, but an API playground to test and experiment with APIs. 
It relies on returning API data from other sources covering: 
1. What are HTTP get requests.
2. What JSON data looks like and how to handle it.
3. How to build structured URLs in Python to make requests.
4. How APIs work.

   
There are 3 main branches:
1. **basic app** a Basic hard-coded route that fetches song lyrics.
2. **added api routes** branch that shows 3 more example routes that fetch data from other sources, including using query parameters.
3. **basic front-end** branch that has basic HTML links to the app routes. Copy and modify this in your project if you want to simplify navigation. 

### To run this application:

Open in a Codespaces environment and run this command:
```
flask --debug run
```
