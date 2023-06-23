from fabric import task

@task
def hello(c):
    """
    Prints a hello message.
    """
    print("Hello, Fabric!")


