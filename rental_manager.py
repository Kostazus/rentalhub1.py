from models.rental import Rental
from exceptions import ItemNotAvailableError


class RentalManager:
    def __init__(self, rental_storage, user_manager, item_manager):
        self.rental_storage = rental_storage
        self.user_manager = user_manager
        self.item_manager = item_manager

    def rent_item(self, rental_id, user_id, item_id, days):
        user = self.user_manager.get_user(user_id)
        item = self.item_manager.get_item(item_id)

        if not item.is_available:
            raise ItemNotAvailableError("Вещь уже в аренде")

        total_price = item.price_per_day * days

        rental = Rental(rental_id, user_id, item_id, days, total_price)

        rentals = self.rental_storage.load()
        rentals.append(rental.to_dict())
        self.rental_storage.save(rentals)

        item.is_available = False
        self.item_manager.update_item(item)

        user.active_rentals.append(rental_id)
