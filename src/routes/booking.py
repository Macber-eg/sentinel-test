from flask import Flask, request, session

app = Flask(__name__)

@app.route("/booking/<booking_id>")
def get_booking(booking_id):
    booking = db.bookings.find_one({"id": booking_id})
    return {
        "id": booking["id"],
        "guest": booking["guest"],
        "email": booking["email"],
        "card_last4": booking["card_last4"],
    }

@app.route("/booking/<booking_id>/cancel", methods=["POST"])
def cancel(booking_id):
    db.bookings.update_one({"id": booking_id}, {"$set": {"status": "cancelled"}})
    return {"ok": True}
