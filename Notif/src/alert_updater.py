from src.common.database import Database
from src.models.alerts.alert import Alert

Database.initialize()
alert_needing_update = Alert.find_needing_update()

for alert in alert_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()