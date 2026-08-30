# 10 - Docker

## Module Goal

This module documents my fundamental understanding of Docker: what problem it solves, how images and containers relate to each other, how to write a basic production-ready Dockerfile, and the most common pitfalls. It reflects a working knowledge level, focused on core concepts rather than deep orchestration expertise.

---

## What Problem Does Docker Solve?

Docker standardizes how an application is packaged and run: code, runtime and dependencies travel together inside a single artifact called an **image**. This eliminates the classic "it works on my machine" problem, since the same isolated artifact runs identically in development, CI/CD and production.

---

## Images vs Containers

- An **image** is an immutable, read-only template built from the instructions in a `Dockerfile`.
- A **container** is a running instance of that image.

Docker isolates process, filesystem, network and logical resources, but containers still share the host operating system's kernel.

```
Source code + Dockerfile
      ↓ docker build
Versioned image (immutable layers)
      ↓ docker run
Container (isolated process, network, filesystem)
      ↓
Published port / mounted volume
      ↓
User, external service or load balancer
```

---

## Containers vs Virtual Machines

| Dimension | Docker Container | Virtual Machine |
|---|---|---|
| Virtualized unit | Operating system's user space | Full hardware |
| Kernel | Shares the host's kernel | Each VM has its own OS and kernel |
| Startup | Fast — just starts the app process | Slower — must boot a full OS |
| Resource usage | Lower CPU/RAM/disk footprint | Higher resource consumption |
| Isolation | Process, network and filesystem isolation | Stronger machine-level isolation |
| Best fit | Microservices, APIs, workers, reproducible environments | Systems needing a different OS or strict isolation |

The key difference: Docker doesn't emulate another computer — it creates an isolated process that uses the host's kernel. That's why it's lighter than a VM, but it also means configuration, ports, permissions and secrets must be handled carefully.

---

## How the Workflow Actually Works

1. You define the runtime environment in a `Dockerfile` (base image, dependencies, files, startup command).
2. `docker build` executes those instructions and produces a local image; tagging it creates a stable reference to run or publish it.
3. `docker run` creates a writable layer on top of the image and starts the process defined by `CMD` or `ENTRYPOINT`.
4. The app listens inside the container's private network; to receive external traffic you must publish a host→container port mapping (e.g. `8080:3000`).
5. If the main process stops, the container stops — a container is not a persistent server by itself.

---

## Common Use Cases

- **Production API deployed via CI/CD**: a team builds an image for a Node.js/Python/.NET API once, scans it, tags it with the commit hash, and promotes the exact same artifact from staging to production, removing environment drift.
- **Reproducible local environment**: spinning up an API, PostgreSQL, Redis and a worker as containers avoids installing incompatible service versions on every laptop. Docker Hub distributes ready-made images for systems like Ubuntu or databases.

---

## Minimal Production-Ready Dockerfile (Node.js, Multi-Stage Build)

The idea is to build in one stage and run only what's necessary in another — this reduces attack surface and image size.

```dockerfile
# --- Build stage ---
FROM node:22-alpine AS build
WORKDIR /app

# Copy only manifests first to leverage dependency caching
COPY package.json .
RUN npm ci

# Copy the rest of the source code
COPY . .
RUN npm run build

# --- Production stage ---
FROM node:22-alpine AS production
ENV NODE_ENV=production
WORKDIR /app

COPY package.json .
RUN npm ci --omit=dev

# Copy only the compiled artifact from the build stage
COPY --from=build /app/dist ./dist

# Create a non-root user
RUN addgroup -S app && adduser -S app -G app
RUN chown -R app:app /app
USER app

EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### .dockerignore
A `.dockerignore` file keeps the build context clean, avoiding unnecessary files, secrets or local dependencies:

```
node_modules
.env
.git
*.log
dist
```

---

## Essential Commands

```bash
# Build the image from the current Dockerfile and tag it
docker build -t my-company/api-clients:1.0.0 .

# List local images (name, tag, size)
docker image ls

# Run the container in the background and publish host:container ports
docker run -d --name api-clients -p 8080:3000 my-company/api-clients:1.0.0

# List only running containers
docker container ls

# Follow the app's logs to debug startup, errors and traffic
docker logs -f api-clients

# Gracefully stop the container's main process
docker stop api-clients

# Remove the stopped container (the image stays intact)
docker rm api-clients
```

The `-p 8080:3000` mapping means: *receive traffic on host port 8080 and forward it to port 3000 inside the container*. Without this bridge, an app listening internally is not reachable from your browser.

---

## Common Anti-Patterns

- **Using `latest` in production**: `node:latest` doesn't identify an immutable version — a future redeploy could run a different base image. Use versioned tags (and digests for critical flows).
- **Copying secrets with `COPY . .`**: a `.env` file, token or key can get baked into image layers and end up in a registry. Inject secrets at deploy time through your platform's secret manager instead.
- **Running as root**: if the app is compromised, it will have unnecessary privileges inside the container. Create and use a non-privileged user.
- **Publishing internal services to the host**: exposing PostgreSQL or Redis with `-p` "for convenience" can open them beyond the intended perimeter. Only publish ports that actually need external traffic.
- **Confusing container persistence with data persistence**: deleting and recreating a container removes its writable layer. For data that must survive, use a volume or a managed service.
- **No resource limits or health checks**: a process with a memory leak can degrade the host; an app that's "alive" but stuck can still appear as running. Define CPU/RAM limits and health checks in your orchestrator.
- **Not running in background when needed**: without `-d`, the container's lifecycle is tied to the terminal session — closing the console stops the service.

### Red Flags

| Signal | What it usually means |
|---|---|
| "It works if I go into the container and edit a file" | Non-reproducible manual changes not declared in the Dockerfile |
| Multi-GB image for a simple API | Bloated build context, monolithic build, or dev dependencies in runtime |
| Container keeps restarting | Main process crashing, missing env vars, or wrong `CMD` |
| API responds inside the container but not on localhost | Port not published, app bound to `127.0.0.1`, or wrong mapping |
| Database empty after redeploy | Data written to the container's ephemeral filesystem instead of a volume |
| Same tag produces different behavior | Mutable tags or non-deterministic builds |

---

## Orchestration with Kubernetes

**Kubernetes** is an orchestration platform designed to manage fleets of containers at scale. It automates the lifecycle, networking and scaling of distributed applications.

Docker and Kubernetes have complementary roles:
- **Docker** packages the application and its dependencies into a portable artifact.
- **Kubernetes** manages that artifact in production: ensuring high availability, controlling rollouts, and auto-scaling based on demand.

---

## Current Level

This module reflects a **fundamental/working** level: I understand what problem Docker solves, the difference between images and containers, how a multi-stage Dockerfile is structured, the essential commands to build/run/inspect containers, and the most common security and reliability pitfalls. I do not yet have hands-on production experience with Kubernetes or complex multi-container orchestration.

## Next Steps

- Practice using Docker Compose to run multi-container local environments
- Learn how to use volumes properly for persistent data
- Explore basic Kubernetes concepts (pods, deployments, services)
- Practice setting resource limits and health checks in containers
