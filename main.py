from pyscript import document

# Menu Foods and Costs
document.getElementById("F1").innerHTML = "🍝 Silly Spagetti "
document.getElementById("P1").innerHTML = "₱250.00"

document.getElementById("F2").innerHTML = "🍗 Gervacio Chicken"
document.getElementById("P2").innerHTML = "₱300.00"

document.getElementById("F3").innerHTML = "🥩 Burger Steak"
document.getElementById("P3").innerHTML = "₱200.00"

document.getElementById("F4").innerHTML = " 🥗 Kid Salad"
document.getElementById("P4").innerHTML = "₱400.00"


def create_order(e):
    name = document.getElementById("cust_name").value.strip()
    address = document.getElementById("cust_address").value.strip()
    contact = document.getElementById("cust_contact").value.strip()

    total = 0
    summary = f"""🧑‍🍳 Order Summary <br>
    Name    : {name} <br>
    Address : {address} <br> 
    Contact : {contact}<br><br>"""

    if document.getElementById("food1").checked:
        summary += "🍝 Silly Spagetti = ₱250<br>"
        total += 250
    if document.getElementById("food2").checked:
        summary += "🍗 Gervacio Chicken = ₱300<br>"
        total += 300
    if document.getElementById("food3").checked:
        summary += "🥩 Burger Steak = ₱200<br>"
        total += 200
    if document.getElementById("food4").checked:
        summary += "🥗 Kid Salad = ₱400<br>"
        total += 400

    if total == 0:
        summary += "No food selected.<br>"

    summary += f"<br>💵 Total: ₱{total}"
    document.getElementById("order_result").innerHTML = summary


def refresh_order(e):
    document.getElementById("cust_name").value = ""
    document.getElementById("cust_address").value = ""
    document.getElementById("cust_contact").value = ""
    document.getElementById("food1").checked = False
    document.getElementById("food2").checked = False
    document.getElementById("food3").checked = False
    document.getElementById("food4").checked = False
    document.getElementById("order_result").innerHTML = "No order yet."