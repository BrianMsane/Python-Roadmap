<h1>FastAPI Important concepts</h1>

<ol>
    <li>
    Split things up with routers.
    <p>if the endpoints are or can be logically grouped, it can be a really good way to organize things into different routers instead of having one file filled with many a large number of endpoints. So now in the main file you can then include all the different routers in your FastAPI app. Add a prefix to your router. The common reasons for doing that are: Namespace management, avoiding conflicts, security and access control, clarity and readability, and modularity. </p>
    </li>
    <li>
    Remove operation code from the endpoint function. 
    <p>The mixes the routing behavior with the operation. The only thing you need to do is to call specific functions or instantiate class objects and call the specific methods, specifying the parameters using the request body or the path parameters. Also, you might want to pass some parameters as default parameters to ensure that you avoid coding them in the endpoint function but rather define it in another file and only import it.</p>
    </li>
    <li>
    Pydantic request and response bodies
    <p>For successful type hints, and schema verification, ensure that you make use of Pydantic request bodies so that the API will get the data from the request body and run it against the predefined schema and if it does not meet that schema, the request is rejected otherwise it goes through. The exact same thing can be done for the response. This also helps SwaggerUI to automatically create the documentation and the schemas for you API in a way that every contributing developer can understand. Also, the data is always predictable so we can easily handle it responses of requests within any part of the codebase.</p>
    <p>It is important to take into consideration the fact that you need to request or respond with only the data you need. This means that you should not add unnecessary fields in the request and response bodies as this can add overhead to the API. This feature is handled in GraphQL not HTTP's RESTful APIs so we are the ones who need to ensure this.</p>
    </li>
    <li>
    Control Access
    <p>Make sure that the users do not abuse your resources in deployment. Use authentication flows using OAuth, Bear JWT tokens.</p>
    </li>
    <li>
    Rate limiting
    <p>Restrict the number of requests that the users can get access to in a specified amount of time. Use your usernames, IP addresses. Bear in mind that FastAPI does not have direct support, unless you use the middleware, for rate limiting so you might use other packages like slow api. Using decorators within each endpoint when you use this option. [I recommend this one because it gives you easy accessibility for controling the resources].</p>
    <p>This helps protect you from attacks like Denial of Service (Dos) or its varient Distributed Denial of Service (DDoS).
    </p>
    </li>
</ol>

<h2>Dependency Injection</h2>
<p>
Dependecny Injection is a design pattern that allows the separation of the creation of an object from its dependencies. It allows a class to receive its dependencis from an external source instead of creating them itself. This makes your code more modular, easier to test, and maintain. One area where DI is particularly useful is managing database connections and operations.
</p>

<p>
For instance, connecting to MongoDB can be done by creating a function that will handle the database connection and then use this dependency injection. It can be used in API endpoints whereby you can use the Depends class from FastAPI and use it for all the endpoints which need to have access to your database. There are a couple of benefits to this and those could be:
</p>

<ul>
<li>Separation of concerns: By separating the database logic from the business logic, you code is easier to manage</li>
<li>Reusability of code: You connection function can be used across the code base</li>
<li>Easier testing: it is easy to pinpoint issues.</li>
</ul>

Uses of Dependency injection
<ul>
<li>Authetication</li>
<li>Database connection</li>
<li></li>
</ul>
