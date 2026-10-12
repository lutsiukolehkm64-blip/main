expected_serials = ["A101", "A102", "A103", "A104", "A105"]
scanned_serials = ["A101", "A102", "A104", "X900", "A101"]
damaged_serials = ["A104", "X900"]


expected_set = set(expected_serials)
scanned_set = set(scanned_serials)
damaged_set = set(damaged_serials)


verified_set = (expected_set & scanned_set) - damaged_set
missing_set = expected_set - scanned_set
unexpected_set = scanned_set - expected_set


if len(missing_set) == 0 and len(damaged_set) == 0 and len(unexpected_set) == 0:
    status = "ACCEPTED"
else:
    status = "REVIEW"

def format_output(items):
    if len(items) == 0:
        return "-"
    else:
        return " ".join(sorted(list(items)))

print(f"STATUS: {status}")
print(f"VERIFIED: {format_output(verified_set)}")
print(f"MISSING: {format_output(missing_set)}")
print(f"DAMAGED: {format_output(damaged_set)}")
print(f"UNEXPECTED: {format_output(unexpected_set)}")
