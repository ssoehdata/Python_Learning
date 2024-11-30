def hours_to_seconds(hours) -> int:
    minutes: int = hours * 60 
    seconds: int = minutes * 60 

    return seconds


def test(hours) -> int:
    secs: int = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
