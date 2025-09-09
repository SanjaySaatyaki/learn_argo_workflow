from hera.workflows import Workflow,WorkflowsService,script

@script()
def hello(s: str):
    print("Hello, {s}!".format(s=s))

with Workflow(generate_name="hello-world-",
               namespace="argo",
               entrypoint="hello",
               arguments={"s":"World"},
    workflows_service=WorkflowsService(host="https://localhost:2746",verify_ssl=False)) as w:
        hello()

w.create()