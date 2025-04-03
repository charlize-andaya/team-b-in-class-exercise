import random
import time

# Dictionary to store messages with delay times
message_dict = {}

def send_msg(msg: str, delay: int, units: str):
    """Stores a message with the delay time before it can be accessed."""
    if not isinstance(delay, int):
        raise Exception("Delay must be an integer")
    
    # Converts all delay to seconds
    unit_conversion = {"seconds": 1, "minutes": 60, "hours": 3600}
    
    if units not in unit_conversion:
        raise Exception("Invalid time unit. Allowed values: 'seconds', 'minutes', 'hours'")
    
    delay_seconds = delay * unit_conversion[units] 

    # Generate a random 6-digit ID (within this range)
    msg_id = random.randint(100000, 999999)
    
    # Storing the message with delay time to unlock message
    message_dict[msg_id] = {
        "message": msg,
        "unlock_time": time.time() + delay_seconds
    }
    
    print(f"Message stored with ID: {msg_id}")
    return msg_id

def get_msg(msg_id: int):
    """Retrieves the message if the allotted time has passed."""
    if msg_id not in message_dict:
        print("Cannot retrieve your message. The message may not exist or more time may need to pass.")
        return False

    msg_data = message_dict[msg_id]
    if time.time() < msg_data["unlock_time"]:
        print("Cannot retrieve your message. The message may not exist or more time may need to pass.")
        return False
    
    print(msg_data["message"])
    return True

# Test Cases
def test_send_msg():
    msg_id = send_msg("Test message", 1, "seconds")
    assert isinstance(msg_id, int) and 100000 <= msg_id <= 999999
    assert msg_id in message_dict

def test_get_msg():
    msg_id = send_msg("Hello, World!", 2, "seconds")
    assert not get_msg(msg_id)  # Should fail cause of delay
    
    time.sleep(3)  # Wait for the delay to pass
    assert get_msg(msg_id)  # Should pass and print the message

def test_invalid_units():
    try:
        send_msg("Invalid test", 2, "days")
    except Exception as e:
        assert str(e) == "Invalid time unit. Allowed values: 'seconds', 'minutes', 'hours'"

def test_invalid_delay():
    try:
        send_msg("Invalid delay", "5", "seconds")
    except Exception as e:
        assert str(e) == "Delay must be an integer"

# Run Tests
test_send_msg()
test_get_msg()
test_invalid_units()
test_invalid_delay()

print("All tests passed.")

