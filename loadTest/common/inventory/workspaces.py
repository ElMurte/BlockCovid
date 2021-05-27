from json import JSONDecodeError
import random
from common.utils import random_word

workspaces_base_url = '/api/inventory/workspaces'

def list_workspaces(self):
    return self.client.get(catch_response=True)


def get_workspace_by_id(self):
    with self.client.get(workspaces_base_url, catch_response=True) as response:
        try:
            workspace = random.choice(response)
            return self.client.get(
                f'{workspaces_base_url}/{workspace._id}', name=f"{workspaces_base_url}/workspace_id", catch_response=True)
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key workspace.id")


def get_workspace_by_rfid(self):
    with self.client.get(workspaces_base_url, catch_response=True) as response:
        try:
            workspace = random.choice(response)
            return self.client.get(
                f'{workspaces_base_url}/{workspace.rfid}', name=f"{workspaces_base_url}/workspace_id", catch_response=True)
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key workspace.id")


def add_workspace(self):
    workspace_data = get_random_workspace_data()
    self.client.post(workspaces_base_url,
                     json={"name": workspace_data['name'], "rfid": workspace_data['rfid']})


def patch_workspace(self):
    with self.client.get(workspaces_base_url, catch_response=True) as response:
        try:
            workspace = random.choice(response)
            patch_data = get_random_workspace_data()
            self.client.patch(
                f'{workspaces_base_url}/{workspace._id}', data=patch_data, name=f"{workspaces_base_url}/workspace_id")
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key workspace.id")


def delete_workspace(self):
    with self.client.get(workspaces_base_url, catch_response=True) as response:
        try:
            workspace = random.choice(response)
            self.client.delete(
                f'{workspaces_base_url}/{workspace._id}', name=f"{workspaces_base_url}/workspace_id")
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key workspace.id")


def get_random_workspace_data():
    name = random_word(30)
    rfid = random_word(30)
    enabled = bool(random.getrandbits(1))

    return {"name": name, "rfid": rfid, "enabled": enabled}
