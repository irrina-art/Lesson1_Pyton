from address import Address
from mailing import Mailing

address_from = Address("630075", "Novosibirsk", "Lenina", "12", "23")
address_to = Address("750693", "Moscow", "Nagatinskaya", "35", "176")
mailing = Mailing(to_address=address_to, from_address=address_from,
                  track="RU653498757", cost=980)

print(f"Отправление {mailing.track} из {mailing.from_address.index}",
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.app} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.app}. "
      f"Стоимость {mailing.cost} рублей.")
