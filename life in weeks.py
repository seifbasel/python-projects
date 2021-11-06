your_age_now=int(input("enter your age now :"))
your_expexted_age= int(input("enter your expected age :"))

age_now_in_days=(your_age_now*365)
expected_age_in_days=(your_expexted_age*365)

still_to_live = (expected_age_in_days-age_now_in_days)
print(f"you have {still_to_live} days to live")
