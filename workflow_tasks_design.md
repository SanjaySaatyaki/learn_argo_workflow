## Types of Tasks
### Container Template
    - Execute in single container with specific command and arguments
    - Execute single script and perfect for standalone tasks
###  Script Template
    - Allow users to run scripts directly in container like bash or python
### Resource Template
    - Interacts directly with Kubernetes
    - Used to provision resources on the fly
### DAG Template
    - Best for complex workflows. Good for tasks which have order of execution
### Steps Template
    - Design a task one after another
    - Data pipeline or Data handling
### Suspend Template
    - Manual Intervention
    - Like approval activity

## Container Template
    - Details of Container, image name and etc
    - Can pass different arguments
    - Volume mount, Working dir
    - Image Pull policy, etc

## Script Template
    - Ideal for execute light weight tasks

## Resource Template
    - Setting up and tearing down of environments
    - Allow direct manipulation of resources in k8s
    - key action as create
        -  manifest kind as deployment to provision it
