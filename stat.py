import argparse
from functools import lru_cache

main_chances = {
    0: 0.35, 1: 0.35, 2: 0.35,
    3: 0.20, 4: 0.20, 5: 0.20, 6: 0.20,
    7: 0.15, 8: 0.10, 9: 0.05
}

def compute_probabilities(start_main, start_n1, start_n2, total_levels=20):
    remaining_levels = total_levels - (start_main + start_n1 + start_n2)
    if remaining_levels < 0:
        raise ValueError("Sum of current stats cannot exceed 20 total level-ups")

    @lru_cache(None)
    def dp(m, n1, n2):
        used = m + n1 + n2

        if used == total_levels:
            p_main_10 = 1.0 if m == 10 else 0.0
            p_normal_10 = 1.0 if (n1 == 10 or n2 == 10) else 0.0
            p_main_8_or_more = 1.0 if m >= 8 else 0.0
            return p_main_10, p_normal_10, p_main_8_or_more

        pm = main_chances[m] if m < 10 else 0.0
        remaining = 1 - pm

        total_main_10 = 0.0
        total_normal_10 = 0.0
        total_main_8_or_more = 0.0

        # Main stat
        if m < 10:
            a, b, c = dp(m + 1, n1, n2)
            total_main_10 += pm * a
            total_normal_10 += pm * b
            total_main_8_or_more += pm * c

        # Normal stats
        normals = []
        if n1 < 10: normals.append(1)
        if n2 < 10: normals.append(2)

        if normals:
            p_each = remaining / len(normals)
            if n1 < 10:
                a, b, c = dp(m, n1 + 1, n2)
                total_main_10 += p_each * a
                total_normal_10 += p_each * b
                total_main_8_or_more += p_each * c
            if n2 < 10:
                a, b, c = dp(m, n1, n2 + 1)
                total_main_10 += p_each * a
                total_normal_10 += p_each * b
                total_main_8_or_more += p_each * c
        else:
            # Both normals maxed, leftover probability wasted
            a, b, c = dp(m, n1, n2)
            total_main_10 += remaining * a
            total_normal_10 += remaining * b
            total_main_8_or_more += remaining * c

        return total_main_10, total_normal_10, total_main_8_or_more

    return dp(start_main, start_n1, start_n2)


def main():
    parser = argparse.ArgumentParser(description="Stat level-up probability calculator")
    parser.add_argument("--main", type=int, default=0, help="Current main stat level (0–10)")
    parser.add_argument("--n1", type=int, default=0, help="Current normal stat 1 level (0–10)")
    parser.add_argument("--n2", type=int, default=0, help="Current normal stat 2 level (0–10)")

    args = parser.parse_args()

    p_main_10, p_normal_10, p_main_8_or_more = compute_probabilities(args.main, args.n1, args.n2)

    print(f"Main stat hits level 10: {p_main_10 * 100:.2f}%")
    print(f"At least one normal stat hits level 10: {p_normal_10 * 100:.2f}%")
    print(f"Main stat hits level 8 or higher: {p_main_8_or_more * 100:.2f}%")


if __name__ == "__main__":
    main()
