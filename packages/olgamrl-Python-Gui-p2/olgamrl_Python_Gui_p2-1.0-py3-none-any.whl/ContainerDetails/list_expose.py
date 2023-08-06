import docker
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    containerName = request.args.get("containerName", "")
    if containerName:
        status, name = container_status(containerName)
    else:
        status, name = "", ""
    return (
            """<form action="" method="get">
                    Container Name: <select name="containerName">""" + containers_names_list() + """</select>
                                     
                    <input type="submit" value="What is my docker status">
                </form>"""
            + "Container Status: "
            + status
            + "<br><br>Name: "
            + name
    )


def container_status(containerName):
    try:
        client = docker.from_env()
        container = client.containers.get(containerName)
        status = container.attrs['State']['Status']
        name = container.attrs['Name']
        print(f'container.attrs: {container.attrs}')
        print(f'Status: {status}')
        return status, name
    except(Exception):
        return "Invalid input", containerName


def containers_names_list():
    client = docker.from_env()
    containerlist = client.containers.list(all)
    names = ""
    for container1 in containerlist:
        names = names + "<option value=\"" + container1.attrs['Name'] + "\">" + container1.attrs['Name'] + "</option>"
    return names


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)