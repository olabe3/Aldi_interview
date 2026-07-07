# DevOps Engineer Homework

## Overview

The goal of this assignment is to evaluate how you approach a typical DevOps engineering task involving:

- Application development / scripting
- Containerization
- Kubernetes
- Helm
- Terraform
- CI/CD
- Code review

The repository contains intentionally incomplete and imperfect components.
Your task is to complete, improve and document the solution.

You are not expected to produce a perfect production-ready system. We are more interested in your engineering approach, decision-making and ability to balance quality with the time constraints.

Time limit: approximately **3 hours**

## Repository Contents

The repository contains:

- An incomplete application skeleton
- Terraform configuration requiring review and improvement
- An incomplete Helm chart
- An incomplete CI/CD pipeline

Your task is to complete and improve these components. Our goal is to understand your engineering approach, and we will build the upcoming technical interview on this project.

## Goal 1

Complete and improve the provided project.

The repository contains the following files:

- Incomplete application code
- Broken/incomplete terraform configuration
- Incomplete Helm Chart
- Incomplete Gitlab CI pipeline

### Requirements

#### Application

Implement a simple application in either:

- Go
- Python

The application must expose the following endpoints:

##### `GET /health`

**Response:**

```json
{
    "status": "ok"
}
```

##### `GET /version`

**Response:**

```json
{
    "version": "1.0.0"
}
```

##### `GET /env`

**Response:**

```json
{
    "environment": "<value from ENVIRONMENT variable>"
}
```

##### `POST /config`

**Request:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `GET /config/{name}`

**Example:**

```bash
GET /config/database_url
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `DELETE /config/{name}`

**Response:**

```json
{
    "deleted": true
}
```

#### Containerization

- Create the necessary Dockerfile with minimal setup
- The image should:
  - build successfully
  - run locally
  - expose the application endpoint

#### Terraform

- Review and fix/complete the Terraform code
- The Terraform code contains several issues and areas for improvement
- In case you don't get time to implement changes describe what would you still improve and why
- Document any changes you make

#### Helm

- Review and fix/complete the Helm Chart
- The chart should deploy the application to Kubernetes
- Document any change you make

#### Gitlab CI

- Complete the pipeline so it becomes capable of building and deploying the application
- The pipeline should support the workflow required to build and deploy the application
- The pipeline should be logically complete and demonstrate how you would automate the process
- Add any other necessary jobs to the pipeline

#### Documentation

Update the project README with following information.

##### What You Changed

###### Terraform
provider.tf
1. required_providers block added for K8s and Helm with pinned version

main.tf
1.  namespace resource hardcoded "production" removed and replaced with terraform variable for configuration reasons
2.  image.tag variable set with environment variable name
3.  environment variable set with environment variable name

variables.tf
1. Default values added for every variables for less critical failure chanches (less operator intervention less chance to fail)

outputs.tf
1. Creating namespace, helm_release_status and helm_release_version outputs

###### Helm

values.yaml
1. Ports are separated to port and containerPort for clearer allocation

deployment.yaml
1. containerPort replaced from 5000 to environment value
2. replicas replaced from 1 to environment value
3. Liveness and readiness probe created under the /health endpoint on the pods for health check reason and for restart process
4. securityContext added for basic security

service.yaml
1. Selector type fixed from myapps to myapp
2. port and targetPort linked from values.yaml

ingerss.yaml
1. Service name fixed from homeworks to myapp
2. port linked form values.yaml

##### Assumptions

1. Application language: python. Reason: Fast and easy apply for a basic RestAPI. Well supported ecosystem for faster development.
2. API: FastAPI. Reason: Basic RestAPI framework, easier input validation and error handling than Flask.
3. Main.py: only one script. Reason: Overcomplicating if separating to more script. This much endpoint can be read in a file. Improvement option: separating if more and complex endpoints come in the future.
4. Ports: to 8000 and 80. Reason: Set to basic ports for simplification.
5. Local cluster (Minikube). Reason: No cloud provider required, widespread solution with inbuilt support.

##### Known Limitations

###### app
1. Basic validation for input, detailed checks are required.
2. Logging missing, debug options are limited.

###### Container / CI
1. Image available only locally, no repository attahced.


##### Production Improvements

1. If cloud providers are availabled new terraform variables should be created and separated per environments.
2. Introduce container artifactiory (JFrog, Cloud Provider) for storing the image.
3. Adding K8s features for the deployment: Scaling, Limitations, Secrets.
4. Add monitoring, logging options (ELK, Prometheus, Grafana).

### Deliverables

- Source Code of the Go/Python application
- Dockerfile
- Terraform changes
- Helm changes
- CI pipeline changes
- README describing decisions, assumptions and user guide for the project.

### Notes

You are not expected to deploy to a cloud provider.
The solution should work with a local Kubernetes cluster such as:

- Kind
- Minikube
- K3d

### Timing

Timebox yourself to approximately **3 hours**. If you can't finish the work within the timebox, describe in the README.md what is left and how you would approach it.

Out of time: Unit tests and Documentation

## Goal 2

You get this half-baked project from one of your colleagues who is a Junior and asking for your guidance.

Provide a short code review in `REVIEW.md` where you address the **top 5 most important things** to fix so the colleague can move forward.

### Review Timing

Spend no more than **30 minutes** on review and feedback.

### Evaluation Criteria

We will evaluate:

- Code quality
- Terraform quality
- Kubernetes and Helm knowledge
- CI/CD design and implementation
- Documentation quality
- Code review quality
- Maintainability and operational thinking

### Use of AI

The use of AI-assisted tools is permitted. However, we encourage you to complete the assignment primarily based on your own knowledge, experience and reasoning. During the interview, we will discuss your implementation choices, trade-offs and decision-making process, so it is important that you fully understand and can explain every part of your solution.

### Unit Test

#### App

cd /path/to/project/app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

#### Endpoints

curl http://localhost:8000/health

curl http://localhost:8000/version

curl http://localhost:8000/env

curl -X POST http://localhost:8000/config \
  -H "Content-Type: application/json" \
  -d '{"name":"db_url","value":"postgres://example"}'

curl http://localhost:8000/config/db_url

curl -X DELETE http://localhost:8000/config/db_url

curl http://localhost:8000/config/db_url

OR Swagger: http://localhost:8000/docs

#### Image build

docker build -t myapp:test .
docker run -p 8000:8000 -e ENVIRONMENT=production myapp:test

#### Terrafrom

terraform init -backend=false
terraform validate
terraform plan -var="image_tag=test" -var="environment=dev" -var="namespace=homework"

#### Helm

helm template myapp . --values values.yaml

#### Minikube

minikube start
eval $(minikube docker-env)
docker build -t myapp:test .
cd terraform
terraform init
terraform apply -var="image_tag=test" -var="environment=dev" -var="namespace=homework"
kubectl get pods -n homework
kubectl port-forward -n homework svc/myapp 8000:80
curl http://localhost:8000/health