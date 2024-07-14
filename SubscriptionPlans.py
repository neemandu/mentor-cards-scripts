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

subs = ["MENTOR10"]

for sub in subs:
    company = sub
    frequency = "YEAR"
    name = company + " - 1 " + frequency
    description = name + " subscription for " + company
    price = 400

    # Set the request payload
    data = {
    "product_id": "Mentor-Cards-Monthly",
    "name": name,
    "description": description,
    "status": "ACTIVE",
    "billing_cycles": [{
        "frequency": {
            "interval_unit": frequency,
            "interval_count": 1
        },
        "tenure_type": "REGULAR",
        "sequence": 1,
        "total_cycles": 0,
        "pricing_scheme": {
            "fixed_price": {
            "value": price,
            "currency_code": "ILS"
            }
        }
    }],
    "payment_preferences": {
        "auto_bill_outstanding": True,
        "setup_fee": {
        "value": "0",
        "currency_code": "ILS"
        },
        "setup_fee_failure_action": "CONTINUE",
        "payment_failure_threshold": 1
    },
    "taxes": {
        "percentage": "0",
        "inclusive": False
    }
    }

    # Make the request
    response = requests.post("https://api.paypal.com/v1/billing/plans", headers=headers, json=data)

    # Check the status code
    if response.status_code == 201:
        # Get the billing plan ID
        plan_id = response.json()["id"]
        print(f"{name} - {plan_id}")
    else:
        print("Error creating billing plan")
        print(response.json())




    company = sub
    frequency = "MONTH"
    name = company + " - 1 " + frequency 
    description = name + " subscription for " + company
    price = 40

    # Set the request payload
    data = {
    "product_id": "Mentor-Cards-Monthly",
    "name": name,
    "description": description,
    "status": "ACTIVE",
    "billing_cycles": [{
        "frequency": {
            "interval_unit": frequency,
            "interval_count": 1
        },
        "tenure_type": "REGULAR",
        "sequence": 1,
        "total_cycles": 0,
        "pricing_scheme": {
            "fixed_price": {
            "value": price,
            "currency_code": "ILS"
            }
        }
    }],
    "payment_preferences": {
        "auto_bill_outstanding": True,
        "setup_fee": {
        "value": "0",
        "currency_code": "ILS"
        },
        "setup_fee_failure_action": "CONTINUE",
        "payment_failure_threshold": 1
    },
    "taxes": {
        "percentage": "0",
        "inclusive": False
    }
    }

    # Make the request
    response = requests.post("https://api.paypal.com/v1/billing/plans", headers=headers, json=data)

    # Check the status code
    if response.status_code == 201:
        # Get the billing plan ID
        plan_id = response.json()["id"]
        print(f"{name} - {plan_id}")
    else:
        print("Error creating billing plan")
        print(response.json())

    ## MC subs  
    """  
    company = sub
    frequency = "YEAR"
    name = company + " - 1 " + frequency + " MC Subs"
    description = name + " subscription for " + company
    price = 118.8

    # Set the request payload
    data = {
    "product_id": "Mentor-Cards-Monthly",
    "name": name,
    "description": description,
    "status": "ACTIVE",
    "billing_cycles": [{
        "frequency": {
            "interval_unit": frequency,
            "interval_count": 1
        },
        "tenure_type": "REGULAR",
        "sequence": 1,
        "total_cycles": 0,
        "pricing_scheme": {
            "fixed_price": {
            "value": price,
            "currency_code": "ILS"
            }
        }
    }],
    "payment_preferences": {
        "auto_bill_outstanding": True,
        "setup_fee": {
        "value": "0",
        "currency_code": "ILS"
        },
        "setup_fee_failure_action": "CONTINUE",
        "payment_failure_threshold": 1
    },
    "taxes": {
        "percentage": "0",
        "inclusive": False
    }
    }

    # Make the request
    response = requests.post("https://api.paypal.com/v1/billing/plans", headers=headers, json=data)

    # Check the status code
    if response.status_code == 201:
        # Get the billing plan ID
        plan_id = response.json()["id"]
        print(f"{name} - {plan_id}")
    else:
        print("Error creating billing plan")
        print(response.json())




    company = sub
    frequency = "MONTH"
    name = company + " - 1 " + frequency + " MC Subs"
    description = name + " subscription for " + company
    price = 13.9

    # Set the request payload
    data = {
    "product_id": "Mentor-Cards-Monthly",
    "name": name,
    "description": description,
    "status": "ACTIVE",
    "billing_cycles": [{
        "frequency": {
            "interval_unit": frequency,
            "interval_count": 1
        },
        "tenure_type": "REGULAR",
        "sequence": 1,
        "total_cycles": 0,
        "pricing_scheme": {
            "fixed_price": {
            "value": price,
            "currency_code": "ILS"
            }
        }
    }],
    "payment_preferences": {
        "auto_bill_outstanding": True,
        "setup_fee": {
        "value": "0",
        "currency_code": "ILS"
        },
        "setup_fee_failure_action": "CONTINUE",
        "payment_failure_threshold": 1
    },
    "taxes": {
        "percentage": "0",
        "inclusive": False
    }
    }

    # Make the request
    response = requests.post("https://api.paypal.com/v1/billing/plans", headers=headers, json=data)

    # Check the status code
    if response.status_code == 201:
        # Get the billing plan ID
        plan_id = response.json()["id"]
        print(f"{name} - {plan_id}")
    else:
        print("Error creating billing plan")
        print(response.json())
    """