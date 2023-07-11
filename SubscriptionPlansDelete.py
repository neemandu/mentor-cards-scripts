import requests
import base64

# Set your PayPal API credentials
client_id = "ATexiLPVEXofyqzisU9MT2NxlUum2Xvup6KZwHUskUj99T4snVB-Ny3xd1L851PMV48BhUI-JFXnNzkt"
client_secret = "ELOwzd8Vt3IBXupC0K02arAalCiF_yYoGMj4roBTEyJNo-6q5pMtHNa3YcquchRYl1e1hb4LsYsJOGXB"

# Encode the credentials
auth = base64.b64encode(f"{client_id}:{client_secret}".encode())

# Set the headers
headers = {
  "Authorization": f"Basic {auth.decode()}",
  "Content-Type": "application/json"
}


# Set the billing plan ID
plan_id = "P-6PK681201P780412AMOVPKXY"

# Set the headers
headers = {
  "Authorization": f"Basic {auth.decode()}",
  "Content-Type": "application/json"
}

# Make the request
response = requests.post(f"https://api.paypal.com/v1/billing/plans/{plan_id}/deactivate ", headers=headers)
print(response)
# Check the status code
if response.status_code == 204:
  print("Billing plan deleted successfully")
else:
  print("Error deleting billing plan")
  print(response.json())
