output "namespace" {
  value       = kubernetes_namespace.homework.metadata[0].name
  description = "The Kubernetes namespace for the application"
}

output "helm_release_status" {
  value       = helm_release.homework.status
  description = "Status of the Helm release"
}

output "helm_release_version" {
  value       = helm_release.homework.version
  description = "Revision number of the Helm release"
}