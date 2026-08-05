# `students` is a queue. `students[0] is the front student`.
# `sandwiches` is a stack. `sandwiches[0] is the top sandwich.
# `0` = circular
# `1` = square

# Rules
## At each step:

# - Look at the front student.
# - Look at the top sandwich.
# - If they match:
#   - student takes the sandwich
#   - both leave
# - If they don’t match:
#   - student goes to the back of the queue
#   - sandwich stays on top

# go through the sandwiches from top to bottom, and each time take one if a student wants it; if nobody wants the current sandwich, stop and count the remaining students as unable to eat.

from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count how many students want each type of sandwich
        count = Counter(students)

        # Serve sandwiches from top to bottom
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                # No student wants this sandwich, so the process stops here
                break
            count[sandwich] -= 1
        
        # Remaining students are unable to eat
        return count[0] + count[1]
        