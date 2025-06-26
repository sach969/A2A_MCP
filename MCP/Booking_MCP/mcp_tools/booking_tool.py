def book_railway(params: dict) -> dict:
    name = params.get("name", "Guest")
    source = params.get("source")
    destination = params.get("destination")
    date = params.get("date")

    if not source or not destination or not date:
        return {"error": "Missing required fields: source, destination, or date"}

    return {
        "confirmation": f"Railway ticket booked from {source} to {destination} on {date} for {name}."
    }

def book_hotel(params: dict) -> dict:
    name = params.get("name", "Guest")
    city = params.get("city")

    if not city:
        return {"error": "Missing required fields: city and checkin date"}

    return {
        "confirmation": f"Hotel booked in {city} for {name}."
    }

def book_cab(params: dict) -> dict:
    name = params.get("name", "Guest")
    pickup = params.get("pickup")
    time = params.get("time")

    if not pickup or not time:
        return {"error": "Missing required fields: pickup, drop, or time"}

    return {
        "confirmation": f"Cab booked from {pickup} at {time} for {name}."
    }
