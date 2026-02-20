#!/usr/bin/env python3
def print_status(player_health):
	if player_health <= 0:
		return "dead"
	return "status check complete"


# Don't edit below this line


def test(health):
	print(f"Player_health: {health}")
	print("checking status...")
	print((f"Result: {print_status(health)}"))
	print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)

main()
