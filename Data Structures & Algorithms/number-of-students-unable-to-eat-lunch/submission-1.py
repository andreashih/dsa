class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circular = 0
        square = 0

        # Count how many students want each type
        for student in students:
            if student == 0:
                circular += 1
            else:
                square += 1
        
        # Serve sandwiches from top to bottom
        for sandwich in sandwiches:
            if sandwich == 0:
                if circular == 0:
                    break
                circular -= 1
            else:
                if square == 0:
                    break
                square -= 1
            
        return circular + square
        