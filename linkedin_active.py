from linkedin_api import Linkedin

# Authenticate with LinkedIn
api = Linkedin('starman112003@gmail.com', 'starwars135')

# Get the profile data for a specific person
profile = api.get_profile('thiruparan-ravikkumar-ab598017a')

# Print the keys in the profile dictionary
print(profile.keys())

# Check if the person is active based on the available keys
if 'summary' in profile:
    active_status = profile['summary']
    print(active_status)
    if active_status:
        print(f"{profile['firstName']} {profile['lastName']} is active on LinkedIn.")
    else:
        print(f"{profile['firstName']} {profile['lastName']} is not active on LinkedIn.")
else:
    print(f"Unable to determine the active status for {profile['firstName']} {profile['lastName']}")