import time
from locust import HttpUser, task, between
import common.inventory.rooms as inventory_rooms
import common.inventory.workspaces as inventory_workspaces
import common.booking.booking as booking

class User(HttpUser):
    wait_time = between(1, 2.5)

    #### ROOMS ####
    @task
    def list_rooms(self):
        inventory_rooms.list_rooms(self)

    @task
    def get_room_by_id(self):
        inventory_rooms.get_room_by_id(self)

    @task
    def get_room_by_rfid(self):
        inventory_rooms.get_room_by_rfid(self)

    @task
    def patch_room(self):
        inventory_rooms.patch_room(self)

    @task
    def delete_room(self):
        inventory_rooms.delete_room(self)

    #### WORKSPACES ####
    @task
    def list_workspaces(self):
        inventory_workspaces.list_workspaces(self)

    @task
    def get_workspace_by_id(self):
        inventory_workspaces.get_workspace_by_id(self)

    @task
    def get_workspace_by_rfid(self):
        inventory_workspaces.get_workspace_by_rfid(self)

    @task
    def patch_workspace(self):
        inventory_workspaces.patch_workspace(self)

    @task
    def delete_workspace(self):
        inventory_workspaces.delete_workspace(self)

    #### BOOKINGS ####
    @task
    def list_bookings(self):
        booking.list_bookings(self)

    @task
    def get_booking_by_id(self):
        booking.get_booking_by_id(self)
    
    @task
    def add_booking(self):
        booking.add_booking(self)

    @task
    def delete_booking(self):
        booking.delete_booking(self)

    @task
    def get_bookings_history(self):
        booking.get_bookings_history(self)

    @task
    def check_in(self):
        booking.check_in(self)
    
    @task
    def check_out(self):
        booking.check_out(self)
