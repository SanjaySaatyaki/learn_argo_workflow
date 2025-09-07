# learn_argo_workflow

Port forward `kubectl -n argo port-forward deployment/argo-server 2746:2746`


Apply Patch kubectl `patch deployment argo-server --namespace argo --type json --patch-file argo-server-patch.json`