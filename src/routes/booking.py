from flask import Flask, request, session

app = Flask(__name__)

@app.route("/booking/<booking_id>")
def get_booking(booking_id):
    # A logic flaw no rule catches: the booking is looked up by id from the URL
    # and returned without checking that it belongs to the signed-in user.
    booking = db.bookings.find_one({"id": booking_id})
    return {"id": booking["id"], "guest": booking["guest"], "card_last4": booking["card_last4"]}

@app.route("/booking/<booking_id>/cancel", methods=["POST"])
def cancel(booking_id):
    # Same again, and this one changes state.
    db.bookings.update_one({"id": booking_id}, {"$set": {"status": "cancelled"}})
    return {"ok": True}
