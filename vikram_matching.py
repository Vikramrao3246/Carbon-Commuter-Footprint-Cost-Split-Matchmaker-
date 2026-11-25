
from datetime import datetime


# Match commuters based on route and departure time
def match_commuters(commuters):

    matched_groups = []
    ungrouped = commuters.copy()

    while ungrouped:

        current = ungrouped.pop(0)
        group = [current]

        for other in ungrouped[:]:

            # Check same source and destination
            same_route = (
                current["source"].strip().lower()
                == other["source"].strip().lower()
                and
                current["dest"].strip().lower()
                == other["dest"].strip().lower()
            )

            # Convert departure times
            time1 = datetime.strptime(
                current["time"], "%H:%M"
            )

            time2 = datetime.strptime(
                other["time"], "%H:%M"
            )

            # Calculate time difference
            time_diff = abs(
                (time1 - time2).total_seconds()
            ) / 60

            # Match if time difference is within 15 minutes
            if same_route and time_diff <= 15:

                group.append(other)
                ungrouped.remove(other)

        matched_groups.append(group)

    return matched_groups
