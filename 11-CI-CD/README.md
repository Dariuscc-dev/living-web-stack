# 11 - CI/CD (Continuous Integration / Continuous Delivery)

## Module Goal

This module documents my fundamental understanding of CI/CD: what problem it solves, how a pipeline actually flows from a code change to a deployable artifact, the difference between Continuous Delivery and Continuous Deployment, and how to write a basic GitHub Actions workflow. It reflects a working knowledge level focused on core concepts.

---

## What Problem Does CI/CD Solve?

CI/CD automates the path from a code change to a deployable artifact and, depending on policy, all the way to production. Its purpose is to reduce the risk and cost of integrating work from multiple developers, turning manual, non-repeatable releases into a traceable, validated and repeatable process — avoiding the classic "integration hell".

---

## How the Pipeline Actually Works

CI/CD is not a single tool — it's a chain of automated checks, typically triggered by a `git push` or by opening/updating a Pull Request.

```
Developer (git push / Pull Request)
      ↓
CI: install → lint → test → build
      ↓ (failure blocks merge)
Immutable artifact (Docker image / binary package)
      ↓
Artifact registry
      ↓
CD: deploy to staging → smoke tests → optional approval
      ↓
Production (rolling / blue-green / canary)
      ↓
Metrics, logs, alerts → rollback if it fails
```

### Step by Step
1. **Trigger**: GitHub Actions detects a `push` or a Pull Request.
2. **Ephemeral environment**: a clean runner checks out exactly the commit to be validated.
3. **CI**: installs locked dependencies, runs static analysis, tests, and build.
4. **Artifact**: if everything passes, a versioned result is produced (e.g. `my-app:<commit-sha>`) — this exact artifact must be the one promoted later.
5. **Registry**: the image or package is published to a registry; it is not rebuilt for each environment.
6. **CD**: a process deploys that artifact to staging and then, with automation or approval, to production.
7. **Operational verification**: health checks, smoke tests, metrics and alerts determine whether to keep or roll back the new version.

---

## CI vs Continuous Delivery vs Continuous Deployment

| Model | What happens after tests pass | Advantage | Trade-off |
|---|---|---|---|
| **CI only** | Code is validated and integrable | Detects incompatibilities early | Deployment is still manual |
| **Continuous Delivery** | A deployable artifact is built and published | Business/compliance control before production | Requires a human approval step |
| **Continuous Deployment** | The validated artifact is deployed automatically | Fastest possible feedback and delivery | Requires very reliable tests, observability and rollback |
| **Manual deploy (FTP/SSH)** | Someone manually copies files to the server | Feels fast at first | Not reproducible; drifts between servers; human error |

### Key Principle: Build Once, Deploy Many
If you rebuild the project for production, you might deploy different dependencies than the ones that passed the tests. The value of CI/CD comes from promoting the **same immutable artifact** across environments.

---

## Common Use Cases

- **Multi-tenant B2B SaaS platform**: every Pull Request runs unit tests, integration tests and security scans. Merging into `main` publishes a Docker image and deploys it to staging automatically. Promotion to production can use a **canary deployment**: 5% of users receive the new version first, errors and latency are observed, and only then is it rolled out further.
- **Data pipeline for enterprise clients**: CI runs tests against sample datasets, validates the output schema, and checks that metrics don't contain impossible values. CD publishes the validated container/package version and schedules the pipeline in production — if a quality check fails, the deployment is blocked before it can affect real data.

---

## Minimal Example: Python App with Tests, Docker and GitHub Actions

### Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home appuser
USER appuser

CMD ["python", "app.py"]
```

### GitHub Actions Workflow (`.github/workflows/ci.yml`)
```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read
  packages: write

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pip install pytest ruff
      - run: ruff check .
      - run: pytest -q

  build-and-publish:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

### What Each Part Does
- `on.pull_request` / `on.push`: defines which events trigger the pipeline.
- `permissions`: grants the minimum access needed for the temporary GitHub token.
- `test` job: runs on a clean Ubuntu runner, installs dependencies, runs linting and tests — any failure stops the pipeline.
- `build-and-publish` job: only runs if `test` succeeds (`needs: test`) and only from `main`, preventing unfinished work from being published as a real image.
- Tagging with `github.sha` ensures the image is tied to an exact, immutable commit.

---

## Branch Protection for `main`

Configured in GitHub under **Settings → Branches → Add branch protection rule**:

- Require a pull request before merging.
- Require status checks to pass before merging.
- Require branches to be up to date before merging.
- Select the `test` check as required.

This prevents a direct push or a Pull Request with failing tests from introducing unvalidated code into the branch that represents the integrated version.

---

## Common Anti-Patterns

| Anti-pattern | What breaks in production | Red flag |
|---|---|---|
| Deploying via FTP or editing files directly on the server | No reliable history, no deterministic rollback, no environment equivalence | "It works on my machine, I'll fix it by hand on the server" |
| Allowing merges with failing CI | `main` stops being a reliable, deployable reference | Failed checks ignored or marked as optional |
| Using `latest` as the only Docker tag | You don't know exactly which version is running or what to roll back to | `docker pull my-app:latest` as a release strategy |
| Rebuilding per environment | Staging and production may run different binaries | Deploy runs `npm install` / `pip install` / `docker build` in production |
| Secrets in YAML or committed to the repo | Credential exposure and possible infrastructure access | API keys, tokens or `.env` files pushed to Git |
| No health checks or rollback | A "successful" deploy can serve errors to users for hours | The only validation is "the deploy command exited with code 0" |
| Slow or flaky tests | The team stops trusting CI and avoids running it | Retrying failed pipelines until they pass |
| Direct deploy to production from a personal branch | Unreviewed, unintegrated code reaches customers | Feature branches holding deployment credentials |

**Important**: a pipeline automates repeatable checks, but it doesn't replace good engineering practices. To safely deploy automatically you still need meaningful tests, environment-specific configuration, observability, and a real rollback mechanism.

---

## Current Level

This module reflects a **fundamental/working** level: I understand what CI/CD solves, the difference between CI, Continuous Delivery and Continuous Deployment, the "build once, deploy many" principle, how to write a basic GitHub Actions workflow with test and build/publish jobs, and the most common anti-patterns to avoid. I am still building deeper experience with deployment strategies (canary, blue-green), production observability, and rollback automation.

## Next Steps

- Practice implementing a canary or blue-green deployment strategy
- Add automated smoke tests after deployment to staging
- Explore approval gates for production deployments
- Learn how to integrate monitoring/alerting into a CD pipeline
