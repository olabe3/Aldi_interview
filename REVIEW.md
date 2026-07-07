# Code Review

Issues listed in order of criticality.

## 1. Terraform syntax errors prevent any deployment
- `main.tf` line 14: `value` is empty, `terraform plan` will fail
- `main.tf` line 19: `prod` syntax error
- `providers.tf`: missing `required_providers` block, no provider version pinning, builds are not reproducible

## 2. Networking is completely broken across the Helm chart
- `deployment.yaml`: containerPort is 5000, but the app listens on default port 8000
- `service.yaml`: selector typo Service will never find the pods
- `service.yaml`: targetPort should match containerPort
- `ingress.yaml`: references service name is `myapp`

## 3. No health probes in the deployment
The app implements a `/health` endpoint but the deployment does not use it for liveness or readiness probes.

## 4. Security: container runs as root
No non-root user in the Dockerfile, no `securityContext` in the deployment. If a vulnerability in the app or its dependencies allows remote code execution, the attacker has root privileges inside the container, increasing the risk of container escape.

## 5. CI pipeline has no real functionality
Both stages only contain echo statements. The pipeline needs: a test, a build, validate, plan and a deploy stage. Without this, there is no automated path from code to deployment.