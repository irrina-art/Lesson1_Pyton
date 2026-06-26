from adress import Adress
from mailing import Mailing

adress_from = Adress("630075", "Novosibirsk", "Lenina", "12", "23")
adress_to = Adress("750693", "Moscow", "Nagatinskaya", "35", "176")
mailing = Mailing(to_adress=adress_to, from_adress=adress_from,
                  track="RU653498757", cost=980)

print(f"Отправление {mailing.track} из {mailing.from_adress.index}",
      f"{mailing.from_adress.city}, {mailing.from_adress.street}, "
      f"{mailing.from_adress.house} - {mailing.from_adress.app} "
      f"в {mailing.to_adress.index}, {mailing.to_adress.city}, "
      f"{mailing.to_adress.street}, "
      f"{mailing.to_adress.house} - {mailing.to_adress.app}. "
      f"Стоимость {mailing.cost} рублей.")
