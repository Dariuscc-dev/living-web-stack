# 07 - Node.js, CORS and REST API Development

## Module Goal

This module documents my understanding of Node.js as a JavaScript runtime, the REST architectural style, CORS as a browser security mechanism, and the practical development of a REST API using Express. It reflects a working knowledge level: I understand the core concepts, can explain them, and can build and consume a basic REST API.

---

## What is Node.js?

**Node.js** is a JavaScript runtime built on Chrome's V8 engine, designed outside the browser to run JavaScript on the server. It is event-driven and non-blocking, which makes it efficient for handling many concurrent connections.

Key points:

- No `window` object like in browsers; instead it exposes a global object (`globalThis` / `global`).
- Ideal for REST APIs, microservices, real-time apps (chats), and automation/scraping tools.
- Not ideal for CPU-intensive tasks (heavy computation, image processing) because it is single-threaded.
- Huge ecosystem through **npm**, the largest package registry in the world.
- Companies like Netflix, Uber, PayPal and LinkedIn use Node.js in production.

### Module Systems
- **CommonJS**: classic syntax, uses `require` and `module.exports`.
- **ES Modules (ESM)**: modern standard, uses `import` / `export`, files typically use `.mjs` or `type: module` in `package.json`.

### Entry Point
`index.js` is the conventional entry file of a Node.js application, where the server is initialized, middlewares configured, and routes defined.

---

## What is REST?

**REST (Representational State Transfer)** is an architectural style for designing APIs over a client-server model, based on resources, unique URIs and HTTP verbs. A **RESTful API** is the practical implementation of that style.

Core ideas:

- Each resource has a unique identifier (URI), e.g. `/books/1`.
- Communication happens through HTTP verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
- Requests are **stateless**: each request must contain all the information needed to be processed.
- Client and server are decoupled: the client doesn't need to know the server's internal implementation.

### Common Anti-Patterns
- Action-based endpoints (e.g. `/deleteUser`) instead of resource-based ones.
- Relying on session state between requests.
- Reusing the same endpoint without clear semantics.
- Tightly coupling client and server implementations.

---

## HTTP Methods and Status Codes

| Method | Purpose | Typical Status Code |
|---|---|---|
| `GET` | Retrieve a resource representation (safe, idempotent) | 200 OK |
| `POST` | Create a new resource | 201 Created |
| `PUT` | Replace a resource entirely | 200 / 204 |
| `PATCH` | Partially update a resource | 200 / 204 |
| `DELETE` | Remove a resource | 200 / 204 |
| `OPTIONS` | Describe communication options (used in CORS preflight) | 204 No Content |

### Status Code Categories
- **1xx** Informational
- **2xx** Success
- **3xx** Redirection
- **4xx** Client errors
- **5xx** Server errors

---

## What is CORS?

**CORS (Cross-Origin Resource Sharing)** is a browser security policy that controls whether a frontend running on one origin can read responses from an API on a different origin.

Key concepts:

- An **origin** is the combination of protocol + domain + port.
- CORS doesn't necessarily stop the request from reaching the server; it stops the browser's JavaScript from reading the response if the server hasn't authorized that origin.
- It is a browser-side protection, not an authentication/authorization system.

### Simple vs Preflight Requests

| | Simple Request | Preflight Request |
|---|---|---|
| Example | Public `GET` without special headers | `POST` with JSON + `Authorization` header |
| First call | Direct real request | `OPTIONS` request sent first |
| Server response | Returns `Access-Control-Allow-Origin` | Responds to `OPTIONS`, then to the real request |

### Key Response Headers
- `Access-Control-Allow-Origin` — which origin can read the response
- `Access-Control-Allow-Methods` — allowed cross-origin methods
- `Access-Control-Allow-Headers` — allowed headers
- `Access-Control-Allow-Credentials` — allows sending cookies/credentials
- `Access-Control-Max-Age` — how long the preflight response is cached

---

## Building a REST API with Express

Express is the most popular Node.js framework for building REST APIs, simplifying routing and middleware handling compared to the native `http` module.

### Basic Server Example
```js
import express from 'express';

const app = express();
app.use(express.json());
app.disable('x-powered-by');

app.get('/movies', (req, res) => {
  res.json(movies);
});

app.post('/movies', (req, res) => {
  const newMovie = { id: crypto.randomUUID(), ...req.body };
  movies.push(newMovie);
  res.status(201).json(newMovie);
});

app.listen(1234, () => {
  console.log('Server listening on port 1234');
});
```

### CORS Middleware Example
```js
import cors from 'cors';

const ACCEPTED_ORIGINS = ['http://localhost:8080', 'http://localhost:1234'];

export const corsMiddleware = ({ acceptedOrigins = ACCEPTED_ORIGINS } = {}) =>
  cors({
    origin: (origin, callback) => {
      if (acceptedOrigins.includes(origin) || !origin) {
        return callback(null, true);
      }
      return callback(new Error('Not allowed by CORS'));
    }
  });
```

### Schema Validation with Zod
```js
import { z } from 'zod';

const movieSchema = z.object({
  title: z.string(),
  year: z.number().int().min(1900).max(2024),
  director: z.string(),
  genre: z.array(z.enum(['Action', 'Drama', 'Comedy']))
});

export function validateMovie(input) {
  return movieSchema.safeParse(input);
}
```

---

## Architecture: Model - Controller - Router

A common pattern used to keep a REST API maintainable is separating concerns into layers:

- **Model**: handles direct interaction with the data source (JSON file, SQL database, etc.).
- **Controller**: contains the request-handling logic and calls the model.
- **Router**: defines the HTTP routes and connects them to controller methods.

This pattern uses **dependency injection**, allowing the same controller/router to work with different models (e.g. switching from a local JSON file to a MySQL database) without changing the business logic.

---

## Async Patterns in Node.js

Node.js offers different ways to handle asynchronous operations, each with different performance implications:

- **Synchronous**: blocking; each task must finish before the next line runs.
- **Asynchronous with callbacks**: operations run in the background, and a callback executes once each finishes.
- **Asynchronous sequential (`async`/`await`)**: operations don't block the main thread but wait for each other in sequence.
- **Asynchronous parallel (`Promise.all`)**: multiple operations start at once, and the code waits for all to finish together — the most efficient approach when tasks are independent.

---

## Environment Variables

Environment variables let you separate configuration values (ports, secrets, connection strings) from source code. Node.js exposes them natively through `process.env`, without needing extra dependencies, although the `dotenv` package is commonly used to load them from a `.env` file during development.

---

## Authentication Basics (JWT)

JSON Web Tokens (JWT) are commonly used to handle authentication in REST APIs:

- On login, the server verifies credentials and issues a signed token.
- The token is usually stored in a cookie or sent via the `Authorization` header.
- On each request, the server verifies the token's signature to identify the user without needing server-side session storage.

---

## Testing and Documentation

- **Unit testing** (e.g. Jest, Vitest) verifies isolated logic such as validations.
- **Integration testing** (e.g. Supertest) verifies how modules interact, including actual HTTP endpoints.
- **OpenAPI / Swagger** is the industry standard for documenting REST APIs, enabling interactive docs and automatic client generation.

---

## Current Level

This module reflects a **working/fundamental** level: I understand what Node.js is and why it's used, I can explain REST principles and HTTP verbs/status codes, I understand what CORS is and why it exists, and I can build and structure a basic REST API with Express, including validation, CORS configuration, and a layered architecture (model-controller-router). I am still building deeper experience with authentication systems, real-time communication (WebSockets), deployment/CI-CD and production-level observability (logging, monitoring).

## Next Steps

- Practice implementing JWT-based authentication end to end
- Explore WebSockets for real-time features (e.g. Socket.io)
- Learn containerization basics with Docker
- Practice setting up CI/CD pipelines (e.g. GitHub Actions)
