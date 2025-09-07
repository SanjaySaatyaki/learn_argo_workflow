## Detailed Architecture Overview

### Argo Namespace
- workflow contoller
    Brain of Argo Workflow
- Argo UI
    Access GUI to run workflows and check status

### Use Namespace
Where the whole exection happens
It has its own pods and have 3 containers
- Init
- Wait
- Main Container
A workflow can have its own pod

## Workflow Controller Detailed Overview

### Components
Queues
- Pod Informer 
    - Keeps eye on Changes to pod in k8s. Listens to pods part of argo workflows. 
    - For the Pod in workflow
- Workflow CDE Informer 
    - Keeps eye on Argo workflows resources.
    - For the entrie workflow
- Workflow Queue
    - Both Pod Informer and Workflow CDE Sends information to pods.
    - It will be buffer for the workers to get the data from the both
- Worker
    - handling single workflow item
        - Process WF item
        - Create WF Pod
        - Pod Reconcilling 