#!/usr/bin/env python3
"""
This module checks and prints the player's health status.
"""


def print_status(player_health):
    """Return 'dead' if health is 0 or less, otherwise return complete."""
    if player_health <= 0:
        return "dead"
    return "status check complete"


def test(health):
    """Print the health and the resulting status for testing."""
    print(f"Player_health: {health}")
    print("checking status...")
    print(print_status(health))
    print("=====================================")


def main():
    """Run the test suite with various health values."""
    test(0)
    test(5)
    test(-1)
    test(3)


if __name__ == "__main__":
    main()
